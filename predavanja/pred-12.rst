=============
Predavanja 12
=============


Značaj praćenja metrika u kontekstu cloud computing-a
=====================================================

- ako nešto *ne merimo*, kako ćemo to *optimizovati* (data/metric driven workflow)?
- interesantne stvari za monitoring/praćenje:

  - utrošak računarskih/mrežnih resursa
  - odziv sistema, u normalnim okolnostima
  - odziv sistema, u vanrednim okolnostima (flash-sale, D/DOS napadi, memory/disk swapping, ...)
  - vremenski lag za elastični scale in/out
  - operativni troškovi, ako koristimo elastični scale in/out (a koliko će onda da nas košta D/DOS napad?)
  - maksimalni stepen opterećenja koje naš sistem može da izdrži

- jako je bitno pratiti ne samo sirove metrike - veći i njihov *istoriski kontekst*, tj. istoriju promena


Uvod u rešenja za kontejnerizaciju [nastavak]
=============================================

Django + Docker
---------------

- referentni primer: https://github.com/petarmaric/cloud-computing-predavanja-beleske/tree/2020/materijali/pred-10
- pakovanje naseg development workflow u Makefile
- pakovanje nase Django web aplikacije u Dockerfile, Docker image


Uvod u rešenja za orhestraciju kontejnera
=========================================

- jedan kontejner, jedan problem
- puno kontejnera, puno problema - kako će međusobno da pričaju?

Uvod u Docker Compose
---------------------

- referentni primer: https://github.com/petarmaric/cloud-computing-predavanja-beleske/tree/2020/materijali/pred-10
- pakovanje nase Django web aplikacije u Dockerfile, Docker image, Docker Compose


Uvod u Continuous Deployment, na cloud + serverless computing [nastavak]
========================================================================

- referentni primer: https://github.com/petarmaric/cloud-computing-predavanja-beleske/tree/2020/materijali/pred-10
