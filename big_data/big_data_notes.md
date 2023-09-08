# BIG DATA

## Qu'est ce que la BIG DATA ?

### Les composantes de la big data sont les 4 VÉRITÉS :

-   **Volume de l'information** :
    Quantité de données générées, collectées et stockées.

-   **Vélocité / Vitesse** :
    Vitesse de traitement de l'information en temps réel.
    Le temps réel est un **temps donné**(le traitement est réalisé en dans un temps alloué précis, ni plus ni moins !).

    L'avalanche de données produites par les capteurs, les réseaux sociaux, les appareils connectés, etc.. doivent souvent être analysées en temps réel.

-   **Variété** :
    La variété concerne la diversité des types de données.

    Les données sont hétérogènes, elles peuvent être de nature :

    -   Structurées (ex: bases de données traditionnelles)
    -   Semi-structurées (ex: les fichiers XML ou JSON)
    -   Non structurées (ex: les textes, les images, les vidéos...).

    La big data doit être capable de gérer cette variété de formats de données.

-   **Valeur**
    L'importance de l'information, sa véracité, son profit, est-ce que la valeur est pertinente et correspond au besoin de l'utilisateur

---

## Les architectures BIG DATA

Une architecture Big Data est conçue pour gérer le traitement et l’analyse de données trop volumineuses ou complexes pour les systèmes de base de données traditionnels.

**Les architectures optimales** :

-   Batch, le traitement par lot
-   Stream, le traitement de flux
-   Lambda, mix des deux

La BIG DATA "travail" en mode distribué / décentralisé (les informations ne sont pas stockées dans les mêmes bases de données), avec un système de réplication sur d'autre DB.

Ce mode permet de récupérer les datas en cas de crash d'une des DB.

---

## Les frameworks populaires utilisés pour la BIG DATA

### Apache Hadoop

-   Hadoop est principalement conçu pour le traitement en mode Batch.
-   Il est utilisé depuis plus longtemps, c'est le premier à avoir été découvert.

### Apache Spark

-   Spark lui, traite les données en temps reel ET mode batch
-   Il est plus rapide que Hadoop en raison de son traitement en mémoire

---

## Définitions

### Les RDD (Resilient Distributed Dataset)

-   Le RDD définit la structure de stockage des données
-   C'est une distribution IMMUABLE
-   Cela permet de restituer des données perdues (car c'est un système distribué)

### HDFS (Hadoop Distributed Files System)

-   Permet de faire évoluer un cluster en plusieurs pour les traiter plus facilement

### MapReduce :

-   Permet de créer des applications qui s'éxecute en parallèle et traiter des grands volumes de données stockées sur les clusters

### Datawarehouse

-   Une **Datawarehouse** est une base de données "secondaire" **CENTRALISÉE** avec comme tables des données orientées par **sujet**.
-   Contient par exemple, les tables : `clients_reguliers`, `clients_etrangers`
-   On alimente ces tables via injection SQL de données provenant de la base de données de l'app et / ou de plusieurs autres sources
