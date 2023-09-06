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
