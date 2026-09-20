### Documentation du jour 1
      -  uv: un outil qui permet def gerer les projets python et leurs dependances et aussi creer des environnement virtuels dévloppé en Rust.
      - Apatche Airflow : plateforme open source d'orchestration des workflow. Elle permet de definir des piplines sous forme de DAGs , de les planifier, d'ecxecuter les taches dans le bon ordre et de surveiller leur etat et log
      - dependance :   une tache doit attendre qu'une autre tache soit terminer
      - DAGs : (Directed Acyclic Graph) representation des taches et de leurs dependances
      - les caracteristiques du airflow est dynamic( le workflow peut etre generer et configure avec du code), Exatensible ( on peut l'adapter et l'etendre), Scalable (pouvoir gerer une charge qui augmente)


      - les pricipes de qualites : pas encore 
      - RGPD : pas encore 
      - Architecture de donnes (staging/core) : pas encore 
      - Data profiling : pas encore 
      - y-data-profiling : pas encore 
      - EDA : pas encore 
      - Dataset :  une collection de donnees dtrucures ou non structure contenant des lignes et des colonnes e, utiliser pour l’analyse ou la modelisation

      - https://www.geeksforgeeks.org/data-science/what-is-dataset/

      - Data Engineer : consiste a construire les systems et les piplines qui permettent de colecter , transformer, stocker et rendre disponible les donnes pour l’analyse et l’AI.

      - EDA : Exploratory Data Analysis  ,  une procedure iterative qui consiste a resumer, visualiser et explorer les informations affin de deceler des tendances, des anomalies et des relations qui ne sont pas immediatement apparente

      - faite en 8 etapes  : 

            - Comprendre le probleme et les donnees : voir le probleme a resoudre et comprendre sur quoi tu va faire vos analyses

            - Importer et examiner les donnees :  importe rles donnes en utilisant pandas (read_csv …), voir la strucure, les lignes les colonnes, les types et formats des donnes oiur chaque variable, chercher les valeurs invalides , aberrantes

            - Gestion des valeurs manquantes leur nombre pour chaque variable et reflechie comment vous traiter ce cas le rembplacer par median ou mode ou bin 0 ou bien les supprime 

            - Explorer les caracteristiques des donnes : la diversite, la repartision , la distrubiton 

            - Effecture la transformation des donnees: 

            - Mise à l'échelle ou normalisation des variables numériques selon une norme (par exemple, **mise à l'échelle min-max, standardisation**).
    
            - Encodage des variables catégorielles à utiliser dans les méthodes d'apprentissage automatique (par exemple, encodage one-warm, encodage par étiquettes)
            - Appliquer des différences mathématiques aux variables numériques (par exemple, logarithmiques, racine carrée) pour corriger l'asymétrie ou la non-linéarité
            - Création de variables ou de capacités dérivées principalement basées sur les variables actuelles (par exemple, calcul de ratios, combinaison de variables)
            - Regroupement ou agrégation d'enregistrements principalement en fonction de variables ou de situations uniques

      - Visualiser les relation entre donnees:

      - analyses univariées, bivariées et multivariées à partir de l'ensemble de données (Matplotlib, seaborn)

      - Gestion des valeurs aberrantes : 

      - Une **valeur aberrante** est une donnée qui s'écarte significativement des autres données (dites normales).

      - utiliserons la méthode de l'écart interquartile ( **EIQ** ) pour identifier les valeurs aberrantes de ces variables. Cette méthode est robuste car elle définit les valeurs aberrantes en fonction de la dispersion statistique des données.

      -     Communiquer les resultats et les observations

      -     https://www.geeksforgeeks.org/data-analysis/steps-for-mastering-exploratory-data-analysis-eda-steps/#step-1-understand-the-problem-and-the-data

      - Data Quality : https://www.geeksforgeeks.org/data-science/what-is-data-quality-and-why-is-it-important/

      - Data Profiling :  méthode permet d’évaluer la qualité et le contenu des données afin de les filtrer efficacement et d’en produire une version synthétisée.https://www.geeksforgeeks.org/data-analysis/understanding-data-profiling/


      - Skewness : oefficient d'asymétrie
      - Skewness = 0 : La distribution est symétrique (comme la loi normale). 
      - Skewness > 0 : La distribution est asymétrique à droite (queue positive plus longue, moyenne souvent supérieure à la médiane). 
      - Skewness < 0 : La distribution est asymétrique à gauche (queue négative plus longue, moyenne souvent inférieure à la médiane). 
      - Ce coefficient est crucial pour évaluer la normalité des données et comprendre si les valeurs extrêmes sont concentrées d'un côté spécifique de la moyenne. 


Pourquoi staging ?

Conserver une copie des données brutes avant transformation.

Pourquoi core ?

Stocker les données nettoyées, transformées et pseudonymisées.

Pourquoi SHA-256 ?

Remplacer le nom client en clair par une valeur pseudonymisée.

Pourquoi Airflow ?

Orchestrer les différentes étapes du pipeline.

Pourquoi PostgreSQL ?

Stocker les données structurées avec des contraintes PK/FK.

Pourquoi l'idempotence ?

Permettre de relancer le pipeline sans créer de doublons.

# Documentation DataStore360

## 1. Concepts étudiés

### 1.1 Dataset
...

### 1.2 Data Engineer
...

### 1.3 Data Quality
...

### 1.4 EDA
...

### 1.5 Data Profiling
...

### 1.6 Skewness
...

---

## 2. Technologies étudiées

### 2.1 uv
...

### 2.2 Apache Airflow
...

### 2.3 Docker
...

### 2.4 PostgreSQL
...

---

## 3. Architecture des données

### 3.1 Pourquoi staging ?
...

### 3.2 Pourquoi core ?
...

### 3.3 Différence staging / core
...

---

## 4. Qualité des données

### 4.1 Valeurs manquantes
...

### 4.2 Doublons
...

### 4.3 Valeurs aberrantes
...

### 4.4 Incohérences
...

---

## 5. RGPD

### 5.1 Données personnelles
...

### 5.2 Pseudonymisation
...

### 5.3 Pourquoi SHA-256 ?
...

---

## 6. Pipeline Data Engineering

### 6.1 Extraction
...

### 6.2 Staging
...

### 6.3 Cleaning
...

### 6.4 Transformation
...

### 6.5 Loading
...

### 6.6 Validation
...

### 6.7 Statistiques
...

---

## 7. Airflow

### 7.1 DAG
...

### 7.2 Dépendances
...

### 7.3 Tasks
...

### 7.4 Logs
...

---

## 8. Idempotence

### Pourquoi l'idempotence ?
...

### Comment elle est implémentée ?
...

---

## 9. Sources

- ...
- ...