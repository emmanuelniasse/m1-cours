# Docker

## C'est quoi ?

-   Plateforme de virtualisation par conteneur, permet d'embarquer une app dans un ou plusiers containers qui pourra s'exécuter sur n'importe quel serveur machine

## Avantages et bénéfices

-   Un conteneur n'a besoin que de quelques centaines Mo d'espace disque dur contrairement à une VM
-   Possibilité d'exploiter directement une app sans être contraint de modifier les librairies installées sur la machine hôte
-   Gain de temps non négligeable, n'a plus autant à s'accorder avec les adminsys pour être sur du versionning etc
-   Conteneurs rapides et simples à mettre en oeuvre
-   Conteneurs portables sur tout type d'env
-   Optimisation des coûts (moins de ram / stockage ...)
-   Résoût les problèmes de dépendances

## Dockerhub

Permet de télécharger et mettre en ligne des images

## Container

-   Une surcouche d'**écriture** sur une image
    Une image (téléchargée en **lecture** uniquement)
-   Pour créer un container :
    -   Télécharger l'image
    -   Créer un container

## Commande docker

**Crée un container disponible au port 8080 de la machine hôte -tid (terminal interactiv d...(ravoir la main sur le terminal)) nom et image-disponible-sur-docker-hub**

> docker run -p 8080:80 -tid --name my-web nginx
> docker stop my-web

Pour changer la page d'accueil aller dans `/usr/share/nginx/html` et modifier la page html

## Volume

Les 3 types de volumes :

-   TMPFS (charge ?)
-   Data (Editable par docker etc. Donner un nom et docker s'occupe de tout)
-   Bind (Donner un chemin et docker fera le lien entre le volume et le conteneur)

Permet :

-   La persistance des données (stocker les données dans un volume qui se trouve dans la machine)
    -   Indiquer le chemin de mon volume (où il y a mes datas) dans mon conteneur
-   Eviter les problèmes de surchage (dédoubler les serveurs dans le cas où il y aurait trop de charge)

Créer un volume en cli

> `docker run -p 8082:80 -tid --name my-web-3 -v dataweb:/usr/share/nginx/html nginx`

Le chemin est dispo dans le dockerhub

## Docker compose

-   Créer des stacks
    -   Permet de lancer des piles:
        En micro services, on souhaite avoir un conteneur par service (back front bdd)
        Lancer d'abord la bdd, puis le back et le front
-
