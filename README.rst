=====
SSMais
=====

SSMais is a Django application that aims to perform reservation management of a service over the Web.
The main purpose of this application is to allow the reuse of features that are generally used in scheduling
software such as scheduling, searching and registering services.

Quick start
-----------

1. Add "ssmais" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ssmais.search_scheduling',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^ssmais/', include('ssmais.urls')),

3. Run `python3 manage.py migrate` to create the ssmais models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ssmais/ to participate in the ssmais.
