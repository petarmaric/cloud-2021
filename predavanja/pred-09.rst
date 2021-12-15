=============
Predavanja 09
=============


Šta je to virtuelizacija i motivacija za upotrebu? [nastavak]
=============================================================

Motivacija sa strane operations-a, tj. service/server provider-a [nastavak]
---------------------------------------------------------------------------

- FaaS (Function As A Service), kao alternativni "serverless"

  - sve prednosti i mane kako kod "serverless" container-a
  - event-driven "serverless" funkcija (event ne mora biti samo HTTP zahtev)
  - uopšte (skoro da) ne moramo da razmišljamo o horizontalnom skaliranju (automatski scale-out i scale-in-to-zero)
  - neverovatno isplativa stvar za slabije popularne servise
  - sada možemo da merimo (i naplaćujemo) vreme izvršavanja i za ispod sekunde (obično 1ms)
  - proći kroz https://aws.amazon.com/lambda/pricing/ i objasniti specifičnosti

- primer upotrebe/cena FaaS, na bazi use-case sajta sa dostavu hrane u Novom Sadu (``predavanja/pred-09-use-case.ods``)


Uvod u rešenja za kontejnerizaciju
==================================

- šta su kontejneri
- kontejneri vs virtuelne mašine

Uvod u Docker
-------------

- osnove rada sa docker container-ima
- poređenje načina rada docker container-a i "slične" virtuelne mašine
- osnove rada sa docker image-ima i njihovim layer-ima
- osnove rada sa Dockerfile-ovima i pravljenje sopstvenog Docker image-a
