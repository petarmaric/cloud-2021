=============
Predavanja 05
=============


Uvod u Django [nastavak]
========================

- quick glance over the Django tutorial docs

- browse through the Django docs during the entire lectures

- play around with Django's API and models in (i)python shell::

    $ poetry run python manage.py shell

- run the Django project::

    $ poetry run python manage.py runserver
    $ xdg-open http://127.0.0.1:8000/
    $ xdg-open http://127.0.0.1:8000/admin/

- add the health check Django app to our Django project:

    - https://github.com/KristianOellegaard/django-health-check

- start the ``visits`` Django app, and do the necessary Django setup::

    $ poetry run python manage.py startapp visits

    ...

    $ poetry run python manage.py makemigrations
    $ poetry run python manage.py migrate
