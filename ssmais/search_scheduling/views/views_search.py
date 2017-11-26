# standard library
import abc

# Django
from django.shortcuts import render
from django.views.generic import ListView

# local django
from ..models import Provider
from ..models import Service
from ..forms import SearchForm


class Search:
    @abc.abstractmethod
    def to_search(self):
        return

    @abc.abstractmethod
    def get_list_itens(self):
        return

    @abc.abstractmethod
    def set_list_itens(self, list_itens):
        return


class SearchName(Search):
    def __init__(self, name, type_search="provider", **kwargs):
         self.name = name
         self.type_search = type_search
         self.list_itens = None

    def to_search(self):
        if self.type_search is 'provider':
            self.list_itens = Provider.objects.filter(name__icontains=self.name)
        elif self.type_search is 'service':
            self.list_itens = Service.objects.filter(name__icontains=self.name)
            pass

    def get_list_itens(self):
        return self.list_itens

    def set_list_itens(self, list_itens):
        self.list_itens = list_itens


class SearchDecorator(Search):
    def __init__(self, search, **kwargs):
         self.search = search

    def get_list_itens(self):
        return self.search.get_list_itens()

    def set_list_itens(self, list_itens):
        self.search.set_list_itens(list_itens)

    def to_search(self):
        # Search base or higher priority
        self.search.to_search()

        # Refine search using decorator
        self.refine_search()

    @abc.abstractmethod
    def refine_search(self):
        """
        Use list_itens as a basis for refinement.
        get_list_itens and set_list_itens
        """
        return


class ProviderSearchAndList(ListView):
    model = Provider
    template_name = None
    context_object_name = 'providers'
    paginate_by = 10
    type_search='provider'
    name = ''
    form_request = None

    def get_queryset(self):
        search = self.define_researches()
        search.to_search()
        return search.get_list_itens()

    def get(self, request, *args, **kwargs):
        form = self.form_request(request.GET or None)
        return render(request, self.template_name, {'providers': self.get_queryset(), 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_request(request.POST or None)
        if form.is_valid():
            self.get_fields(form)

        return render(request, self.template_name, {'providers': self.get_queryset(), 'form': form})

    def get_fields(self, form):
        self.name = form.cleaned_data.get('name')

    def define_researches(self):
        search = SearchName(name=self.name, type_search=self.type_search)
        return search
