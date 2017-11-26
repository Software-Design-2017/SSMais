# standard library
import abc

# Django
from django.shortcuts import render

# local django
from provider.models import Provider
from service.models import Service
from search.forms import SearchForm


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

    def get_queryset(self):
        search = SearchName(name=self.name, type_search=self.type_search)
        search.to_search()
        return search.get_list_itens()

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET or None)
        return render(request, self.template_name, {'providers': self.get_queryset(), 'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)
        if form.is_valid():
            self.name = form.cleaned_data.get('name')

        return render(request, self.template_name, {'providers': self.get_queryset(), 'form': form})
