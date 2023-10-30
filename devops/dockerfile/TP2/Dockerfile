# distribution
FROM ubuntu:jammy

# installation de git et d'un serveur nginx
RUN apt update &&\
    apt install -y git nginx

WORKDIR /mon-projet

RUN git clone https://github.com/sadofrazer/static-website-example.git /mon-projet

RUN cp -r /mon-projet/* /usr/share/nginx/html

EXPOSE 80
