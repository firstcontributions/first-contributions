# Odstranjevanje datoteke

Včasih si želiš odstraniti datoteko z Git-a, vendar je ne želiš odstraniti s svojega računalnika. To lahko storiš z uporabo naslednjega ukaza: 

``git rm <file> --cached``

## Kaj se je zgodilo?

Git ne bo več sledil spremembam v odstranjeni datoteki. Kar se tiče Git-a, ta datoteka ne obstaja več. Če poiščeš datoteko na svojem disku, vidiš da še vedno obstaja.

V zgornjem primeru smo uporabili zastavico `--cached`. Če je ne bi uporabili, bi Git odstranil datoteko tudi z našega diska.

Če sedaj ustvarimo commit z `git commit -m "Remove file1.js"` in ga pošljemo v oddaljeni repository z ukazom `git push origin master`, bo datoteka odstranjena tudi iz oddaljenega repository-ja.

## Dodatne možnosti

-   Če želiš odstraniti več datotek, jih lahko vse vljučiš v en ukaz:

    `git rm file1.js file2.js file3.js --cached`

-   Lahko uporabiš nadomestni znak (*) da odstraniš podobne datoteke. Na primer, če želiš odstraniti vse datoteke s končnico .txt s svojega repository-ja, uporabi ukaz:

    `git rm *.txt --cached`
