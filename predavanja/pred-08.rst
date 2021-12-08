=============
Predavanja 08
=============


Šta je to virtuelizacija i motivacija za upotrebu? [nastavak]
=============================================================

- poređenje KPI ``(CPU_CORES * RAM_GB) / cena`` za "slične" dedicated/vps/cloud
ponude, npr za EU region:

  - `Hetzner AX101 dedicated`_: cena 94 eur/mesečno, 16 CPU cores, 128 GB RAM (KPI ~21.79)
  - `Hetzner CPX51 VPS`_: cena 49.90 eur/mesečno, 16 CPU cores, 32 GB RAM (KPI ~10.26)
  - `AWS EC2 m5ad.4xlarge`_: cena 1.00 USD/sat tj. ~637.66 eur/mesečno, 16 CPU cores, 64 GB RAM (KPI ~1.61)

Obratite pažnju da ovo pojednostavljeno poređenje ignoriše razlike u
dostupnosti/cenama lokalnog smeštajnog prostora, mrežnog protoka/brzine ka/sa
internetu, ... - što može značajno uticati na **TCO**.

.. _`Hetzner AX101 dedicated`: https://www.hetzner.com/dedicated-rootserver/matrix-ax
.. _`Hetzner CPX51 VPS`: https://www.hetzner.com/cloud
.. _`AWS EC2 m5ad.4xlarge`: https://aws.amazon.com/ec2/pricing/on-demand/

Motivacija sa strane operations-a, tj. service/server provider-a [nastavak]
---------------------------------------------------------------------------

- možemo našem kupcu servera/servisa da iznajmimo jedan deo fizičkog servera - kao "serverless" container

  - *UVEK* postoji server/CPU na kome se izvršava kod, samo je pitanje da li to interesuje našeg krajnjeg kupca
  - zvuči "cool" što smo cloud-native
  - obično možemo da tražimo *JOŠ* veću cenu u odnosu na ranije, jer je ovo premium usluga
  - monogo je efikasnije pakovanje korisnika i njihovih "kontejnera", pošto kontejner sadrži samo lib/app a ostatak operativnog sistema dele svi korisnici
  - visoka efikasnost utroška diska na serveru, pošto Docker organizuje (i kešira) svoje container/image u tzv. slojeve - tako da se slojevi mogu deliti između svih korisnika na tom serveru
  - proći kroz https://aws.amazon.com/fargate/pricing/ i objasniti specifičnosti
