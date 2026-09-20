# DataStore360

> Transformer les ventes brutes en données fiables et exploitables.

DataStore360 est un projet de Data Engineering dont l'objectif est de transformer
un jeu de données de ventes brutes en données nettoyées, structurées,
pseudonymisées et exploitables pour l'analyse.

Le projet met en œuvre un pipeline de données automatisé permettant
d'extraire les données, les charger dans une zone de staging, les nettoyer,
les transformer, les charger dans le modèle core et enfin valider les données.

---

## 1. Présentation

Le projet DataStore360 part d'un jeu de données de ventes contenant
des informations sur les commandes, les clients et les produits.

Les données initiales peuvent contenir différents problèmes de qualité :

- valeurs manquantes.
- doublons.
- incohérences.
- dates invalides ou incohérentes.
- valeurs aberrantes.
- données personnelles non protégées.

L'objectif est donc de construire un pipeline Data Engineering permettant
de transformer ces données brutes en données fiables et exploitables.

Le pipeline permet notamment de :

- analyser la qualité des données.
- nettoyer les données.
- traiter les valeurs manquantes et les doublons.
- vérifier les incohérences.
- pseudonymiser les données personnelles.
- calculer des variables dérivées.
- stocker les données dans PostgreSQL.
- automatiser le traitement avec Apache Airflow.
- vérifier la qualité des données finales.
- permettre la relance du pipeline sans créer de doublons.

---

## 2. Objectifs

Les principaux objectifs du projet sont :

### Analyse et qualité des données

- Explorer le dataset avec une approche EDA.
- identifier les valeurs manquantes.
- détecter les doublons.
- identifier les incohérences.
- détecter les valeurs aberrantes.
- analyser les distributions et les relations entre les variables.
- générer un rapport de Data Profiling.

### Nettoyage et transformation

- supprimer les doublons.
- traiter les valeurs manquantes.
- standardiser les données.
- convertir les dates dans un format exploitable.
- vérifier la cohérence des dates.
- créer des variables dérivées.
- calculer le délai de livraison.
- calculer la marge bénéficiaire.

### RGPD

- identifier les données personnelles.
- anonymiser les noms des clients.
- éviter de conserver les noms des clients en clair dans le schéma `core`.

### Stockage et orchestration

- conserver les données brutes dans `staging`.
- stocker les données nettoyées et transformées dans `core`.
- utiliser PostgreSQL pour le stockage.
- automatiser le pipeline avec Apache Airflow.
- rendre le pipeline idempotent.
- valider les données après chargement.

---

## 3. Architecture

L'architecture du projet est organisée autour de deux zones principales
dans PostgreSQL :

- `staging` : conservation des données brutes.
- `core` : données nettoyées, transformées et anonymisées.

Le fonctionnement général du pipeline est :

```text
                 Dataset CSV
                     |
                     v
                Extraction
                     |
                     v
              +-------------+
              |   STAGING   |
              | données     |
              | brutes       |
              +-------------+
                     |
                     v
                  Cleaning
                     |
                     v
                Transformation
                     |
                     +------> Anonymisation
                     |
                     +------> Variables dérivées
                     |
                     v
                +----------+
                |   CORE   |
                +----------+
                /    |     \
               /     |      \
              v      v       v
         Customers Products Orders
                     |
                     v
                 Validation
                     |
                     v
                Statistiques
```

### 4. Technologies utilisées

| Technologie     | Utilisation                                  |
| --------------- | -------------------------------------------- |
| Python          | Développement du pipeline                    |
| Pandas          | Manipulation et nettoyage des données        |
| NumPy           | Calculs numériques                           |
| Matplotlib      | Visualisation des données                    |
| Seaborn         | Visualisation et analyse exploratoire        |
| ydata-profiling | Data Profiling                               |
| PostgreSQL      | Stockage des données                         |
| pgAdmin         | Administration et vérification de PostgreSQL |
| SQLAlchemy      | Connexion entre Python et PostgreSQL         |
| psycopg2        | Driver PostgreSQL                            |
| Apache Airflow  | Orchestration du pipeline                    |
| Docker          | Conteneurisation                             |
| Docker Compose  | Gestion des services                         |
| uv              | Gestion du projet Python et des dépendances  |
| Git / GitHub    | Versionnement du projet                      |


### 5. Structure du projet
```text
DataStore360/
│
├── data/
│   ├── raw/
│   │   └── store_data.csv
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_profiling.ipynb
│   └── 03_cleaning_rgpd.ipynb
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── cleaning.py
│   ├── transform.py
│   ├── load.py
│   ├── validation.py
│   └── statistics.py
│
├── dags/
│   └── datastore360_pipeline.py
│
├── include/
│   └── sql/
│       ├── 01_schemas.sql
│       └── 02_tables.sql
│
├── reports/
│   └── profiling_report.html
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
├── README.md
└── DOCUMENTATION.md
```

### 6. Data Quality

La qualité des données a été analysée pendant la phase d'EDA et
de Data Profiling.

Les principaux contrôles réalisés concernent :

   - les valeurs manquantes ;
   - les doublons ;
   - les types de données ;
   - les dates ;
   - les valeurs aberrantes ;
   - les incohérences ;
   - les contraintes métier.

### Principaux problèmes identifiés

| Problème                 | Traitement                                          |
| ------------------------ | --------------------------------------------------- |
| Valeurs manquantes       | Analyse et traitement selon le contexte             |
| Doublons                 | Détection et suppression                            |
| Dates                    | Conversion et contrôle de cohérence                 |
| `Ship Date < Order Date` | Détection et traitement                             |
| `Ship Mode` manquant     | Recherche d'une valeur cohérente lorsque disponible |
| Noms clients             | Nettoyage puis pseudonymisation                     |
| Valeurs aberrantes       | Identification et analyse                           |


### Contrôles métier

Les règles suivantes sont également vérifiées :

   - une commande est associée à un client ;
   - une commande est associée à un produit ;
   - un client peut avoir plusieurs commandes ;
   - un produit peut apparaître dans plusieurs commandes ;
   - la remise doit être dans une plage valide ;
   - la quantité ne doit pas être négative ;
   - la date d'expédition ne doit pas être antérieure à la date de commande.

### 7. RGPD et pseudonymisation

Le dataset contient des informations permettant d'identifier les clients,
notamment le nom du client.

Afin d'éviter de conserver les noms en clair dans la zone core,
une pseudonymisation avec SHA-256 a été appliquée.

### Exemple

Avant :
``` bash
Customer Name
John Doe
```

Après :
```bash
Customer Name
<hash SHA-256>

```


Cette transformation permet de limiter l'exposition directe des données
personnelles dans la couche `core`.


### 8. PostgreSQL

PostgreSQL est utilisé comme système de stockage des données.

Deux schémas principaux sont utilisés :

`Staging`

Le schéma staging permet de conserver les données brutes avant
transformation.

Table :

`staging.superstore_raw`

Cette table sert de copie des données sources.

`Core`

Le schéma core contient les données nettoyées, transformées et
pseudonymisées.

Les tables principales sont :

   - core.customers
   - core.products
   - core.orders

Relations
```bash
customers
    |
    | customer_id
    v
 orders
    ^
    | product_id
    |
products
```
Les clés primaires et étrangères permettent de garantir la cohérence
des relations entre les tables.

### 9. Pipeline Airflow

Apache Airflow est utilisé pour orchestrer les différentes étapes
du pipeline.

Le workflow est représenté sous forme de DAG.

Les principales tâches sont :
```bash
extract
   ↓
load_staging
   ↓
clean
   ↓
transform
   ↓
clear_core
   ↓
load_customers
   ↓
load_products
   ↓
load_orders
   ↓
validate
   ↓
statistics
```
Chaque tâche est exécutée dans l'ordre défini par ses dépendances.

Airflow permet également de :

   - planifier le pipeline.
   - exécuter les tâches.
   - visualiser leur état.
   - consulter les logs.
   - détecter les erreurs.
   - relancer les tâches.
### 10. Idempotence

Le pipeline a été conçu pour être idempotent.

Cela signifie qu'une nouvelle exécution du pipeline ne doit pas créer
de doublons dans les tables finales.

Avant de recharger les données dans core, les anciennes données du
core sont supprimées puis les données transformées sont rechargées.

L'ordre de chargement respecte les dépendances :
```bash
clear_core
    ↓
customers
    ↓
products
    ↓
orders
```
La table staging conserve quant à elle les données brutes.

Une deuxième exécution du pipeline peut ainsi être effectuée sans
créer de doublons dans les tables core.

### 11. Installation

#### 1. Cloner le projet
git clone <URL_DU_REPOSITORY>
#### 2. Accéder au projet
cd DataStore360
#### 3. Lancer les services Docker
docker compose up -d
#### 4. Vérifier les conteneurs
docker compose ps

Les principaux services utilisés sont :

PostgreSQL.
pgAdmin.
Airflow Webserver.
Airflow Scheduler.
PostgreSQL pour les métadonnées Airflow.
environnement applicatif DataStore360.
### 12. Exécution

Une fois les conteneurs démarrés, accéder à l'interface Airflow.

http://localhost:8080

Le DAG DataStore360 peut ensuite être activé et exécuté depuis
l'interface Airflow.

Le pipeline exécute automatiquement les différentes étapes :
```bash
Extraction
    ↓
Staging
    ↓
Nettoyage
    ↓
Transformation
    ↓
Chargement Core
    ↓
Validation
    ↓
Statistiques
```
Les logs de chaque tâche peuvent être consultés depuis l'interface
Airflow.

### 13. Validation

Après l'exécution du pipeline, plusieurs contrôles sont effectués.

Vérification des tables
```BASH
      SELECT COUNT(*) FROM core.customers;

      SELECT COUNT(*) FROM core.products;

      SELECT COUNT(*) FROM core.orders;
      Vérification des doublons
      SELECT customer_id, COUNT(*)
      FROM core.customers
      GROUP BY customer_id
      HAVING COUNT(*) > 1;
      Vérification des données personnelles
      SELECT customer_name
      FROM core.customers
      LIMIT 10;
```
Les noms des clients ne doivent pas apparaître en clair.

Vérification des relations

Les clés étrangères permettent de vérifier que les commandes
référencent des clients et des produits existants.

Vérification de l'idempotence

Le pipeline est exécuté une deuxième fois afin de vérifier que
les données ne sont pas dupliquées dans core.



