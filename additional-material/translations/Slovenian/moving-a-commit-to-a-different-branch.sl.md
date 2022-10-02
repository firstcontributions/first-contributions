# Premikanje commita v drugo vejo
Kaj storiti, če izvedeš commit svojih sprememb, in potem ugotoviš da si izvedel commit v napačni veji? Kako lahko to spremenimo? To je razloženo v tem vodiču.

## Premikanje zadnjega commita v obstoječo vejo
To storiš z naslednjimi ukazi:

```git reset HEAD~ --soft``` - Razveljavi zadnji commit, spremembe ostanejo na voljo.  
```git stash``` - Posname stanje direktorija in ga shrani v `stash`.  

```git checkout name-of-the-correct-branch``` - Prestavi v drugo vejo.
```git stash pop``` - Vzame zadno shranjeno stanje iz `stash-a`.  
```git add .``` - Ali dodaš posamezne datoteke.  
```git commit -m "your message here"``` - Shrani in izvede commit sprememb.  

Sedaj so tvoje spremembe na pravi veji.


### Premikanje zadnjih nekaj commitov v novo vejo
To storiš z naslednjimi ukazi:
```git branch newbranch``` -  Ustvariš novo vejo. Nova veja ima vse prej ustvarjene commite.
```git reset --hard HEAD~#``` - Premakni glavno vejo ( master ) nazaj za # commit-ov. Ti commit-i bodo izbrisani z glavne veje!
```git checkout newbranch``` - Prestaviš se v novo vejo, ki ima vse prej ustvarjene commit-e. 

Pomembno: Vse spremembe, ki niso bile commit-ane, bodo IZGUBLJENE!