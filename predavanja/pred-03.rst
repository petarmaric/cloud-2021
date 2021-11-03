=============
Predavanja 03
=============


Uvod u upravljanje zavisnostima u programskom jeziku Python
===========================================================

- operativni sistem::

    - ``sudo apt install ...``, za sve korisnike - a mozda i (blago) zastarele verzije paketa

- pip

    - ``sudo pip install ...``, za sve korisnike - *veoma* opasno!
    - ``pip install --user ...``, samo za mog unix korisnika
    - kako imati više verzija jednog istog Python dependency na računaru?

- virtualenv + virtualenvwrapper::

    mkvirtualenv --clear -a . cloud-computing

    deactivate

    workon cloud-computing
    pip install Django
    django-admin --version # instaliran Django u virtualenv

    deactivate
    django-admin --version # Django nije sistemstki instaliran, pa je nedostupan van virtualenv

- requirements.txt::

    pip install -r requirements.txt

- koji specifikator verzije koristiti?

    - ``Django==3.2.1``
    - ``Django``
    - ``Django>=3.2.0``
    - ``Django<4``
    - ``Django~=3.2.0``
