# standard library
import abc

# Django
from django.shortcuts import render


class Search:
    @abc.abstractmethod
    def get_type_search(self):
        return


class SearchName(Search):
    def __init__(self, name, **kwargs):
         self.name = name

    def get_type_search(self):
        search_name = {'name': self.name}
        return search_name


class SearchDecorator(Search):
    def __init__(self, search, **kwargs):
         self.search = search

    @abc.abstractmethod
    def get_type_search(self):
        return
