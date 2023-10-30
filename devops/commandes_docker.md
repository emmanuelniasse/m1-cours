# Les commandes docker-file de base

-   Supprimer une image
    `> docker image rm [id ou nom de l'image]`

-   Lister les containers, des images docker, qui sont en cours d'exécution
    `> docker container ls`
    Raccourci : `> docker ps`

-   Lister tous les containers des images docker
    `> docker container ls -a`
    Raccourci : `> docker ps -a`

-   Supprimer tous les containers de la machine
    `> docker container prune`

-   Lister toutes les images
    `> docker image ls -a`

-   Supprimer une image
    `> docker image rm [nom_image]`

-   Créer un container
    `> docker create ubuntu bash`

    -   `docker create` va créer un container mais pas l'exécuter
    -   `ubuntu` est une image publique disponible dans le docker hub
    -   `bash` commande qui sera exécutée lorsque le container sera démarré.
        Ici un shell BASH intérractif sera lancé l'intérieur du container, on aura accès à un terminal

-   Exécuter un container
    `> docker container start [id_container]`

-   Créer un container avec les options `-it`
    `i` pour la session intéractive
    `t` pour créer un terminal dans le container

    `> docker container create -it ubuntu bash`

Un container sera démarré "UP" sans avoir exécuter le terminal qu'il contient
Pour lancer son terminal, il faut lier (attacher) notre terminal local à celui du container.

(Pour plus d'infos : `> docker container start --help`)

-   Démarrer le container et lancer le terminal contenu à l'intérieur
    `> docker container start [4_premiers_caracteres_de_l_id_container]`

    -   Le STATUS est maintenant UP

    -   Attacher notre terminal au container
        `> docker container attach [4_premiers_caracteres_de_l_id_container]`

    -   Relancer mon container
        `> docker container -ai [4_premiers_caracteres_de_l_id_container]`
        `a` : attach
        `i` : mode intérractif

    Après avoir quitter mon container en faisant `exit` et en le relançant par la suite `> docker container -ai [4_premiers_caracteres_de_l_id_container]`, si je fais la commande `ls` je retrouve les fichiers qui sont dans ce container.
