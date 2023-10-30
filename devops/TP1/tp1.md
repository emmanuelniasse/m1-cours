## Consigne : Créer et run un container pour un serveur apache + un volume

`docker run -dit --name my-apache-app -p 8080:80 -v "$PWD/docker-data":/usr/local/apache2/htdocs/ httpd:2.4`

## Détails

-   `-dit` lance le container en background
-   `-p 8080:80` correspond à l'association de mon port local au port de mon container
-   `-v "$PWD/docker-data":/usr/local/apache2/htdocs/` correspond au volume local associé à mon volume présent dans le container
-   `httpd:2.4` correspond à l'image pulled

## Pour lancer un deuxième container avec le même volume

-   Relancer la commande précédente avec un port (local) différent et un nom de container différent
    `docker run -dit --name my-apache-app-2 -p 8081:80 -v "$PWD/docker-data":/usr/local/apache2/htdocs/ httpd:2.4`
