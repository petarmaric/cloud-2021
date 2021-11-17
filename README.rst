About
=====

Webapp demo for cloud computing predavanja.

Installation
============

This project doesn't require system wide installation, simply clone its
repository to get started::

    $ git clone https://github.com/petarmaric/cloud-2021
    $ cd cloud-2021
    $ poetry install

Quick start
===========

Setup the database, run Django migrations and create Django superuser::

    $ poetry run python manage.py migrate
    $ poetry run python manage.py createsuperuser

Run the webapp server, in development mode::

    $ poetry run python manage.py runserver
    $ xdg-open http://127.0.0.1:8000/
    $ xdg-open http://127.0.0.1:8000/admin/
