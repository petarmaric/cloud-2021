=============
Predavanja 04
=============


Uvod u upravljanje zavisnostima u programskom jeziku Python [nastavak]
======================================================================

- poetry - best thing since sliced bread! Njega cemo koristiti na predmetu

    Učinite sebi uslugu i instalirajte poetry kroz https://pypa.github.io/pipx/


Uvod u Django
=============

- create the webapp Django project::

    poetry run django-admin startproject webapp .

- setup the database, run Django migrations and create Django superuser::

    poetry run python manage.py migrate
    poetry run python manage.py createsuperuser
