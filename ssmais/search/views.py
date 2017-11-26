# standard library
import abc

# Django
from django.shortcuts import render


class Search:
    @abc.abstractmethod
    def get_type_search(self):
        return


class SearchName(Search):
    list_itens = None

    def __init__(self, name, type_search="provider", **kwargs):
         self.name = name
         self.type_search = type_search

    def get_type_search(self):
        if type_search is 'provider':
            # TODO Search
        elif type_search is 'service':
            # TODO Search


class SearchDecorator(Search):
    def __init__(self, search, **kwargs):
         self.search = search

    @abc.abstractmethod
    def get_type_search(self):
        return
