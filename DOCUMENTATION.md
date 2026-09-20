# Documentation DataStore360

## 1. Concepts étudiés

### 1.1 Dataset

Un **dataset** est un ensemble de données organisé, généralement sous forme de lignes et de colonnes lorsqu'il est structuré. Il peut contenir différentes informations utilisées pour l'analyse, la visualisation ou la modélisation.

Dans DataStore360, le dataset utilisé contient principalement des informations concernant :
- les commandes.
- les clients.
- les produits.
- les ventes.
- les dates de commande et d'expédition.
- les remises.
- les bénéfices.

**Source :**  
https://www.geeksforgeeks.org/data-science/what-is-dataset/

### 1.2 Data Engineer

Le **Data Engineer** est chargé de construire et maintenir les systèmes permettant de collecter, extraire, transformer, nettoyer, stocker et rendre disponibles les données pour l'analyse.

Dans DataStore360, le pipeline suit notamment ce flux :

```text
Extraction
    ↓
Staging
    ↓
Nettoyage
    ↓
Transformation
    ↓
Core
    ↓
Validation
```

### 1.3 Data Quality

La **Data Quality** correspond à la capacité des données à être suffisamment correctes, complètes, cohérentes et fiables pour l'utilisation prévue.

Dans DataStore360, les contrôles concernent notamment :
- la complétude ;
- l'unicité ;
- la cohérence ;
- la validité ;
- les valeurs manquantes ;
- les doublons ;
- les dates ;
- les valeurs aberrantes ;
- les contraintes métier.

**Source :**  
https://www.geeksforgeeks.org/data-science/what-is-data-quality-and-why-is-it-important/

### 1.4 EDA — Exploratory Data Analysis

L'**EDA (Exploratory Data Analysis)** consiste à explorer, résumer et visualiser les données afin d'identifier les tendances, distributions, anomalies, relations entre variables, valeurs manquantes et valeurs aberrantes.

Dans DataStore360, l'EDA a permis de comprendre la structure du dataset avant le nettoyage.

#### Étapes principales

1. **Comprendre le problème et les données** : contexte, objectifs, variables et règles métier.
2. **Importer et examiner les données** avec Pandas.
3. **Analyser les valeurs manquantes** et choisir une stratégie adaptée.
4. **Explorer les caractéristiques des données** : diversité, fréquences et distributions.
5. **Transformer les données** lorsque nécessaire.
6. **Visualiser les relations** avec Matplotlib et Seaborn.
7. **Analyser les valeurs aberrantes**, notamment avec l'IQR.
8. **Communiquer les résultats et observations**.

Exemple d'exploration :

```python
import pandas as pd

df = pd.read_csv("store_data.csv")

df.shape
df.info()
df.head()
df.describe()
df.isna().sum()
```

Pour l'IQR :

```text
IQR = Q3 - Q1

Borne inférieure = Q1 - 1.5 × IQR
Borne supérieure = Q3 + 1.5 × IQR
```

Une valeur aberrante n'est pas automatiquement une erreur : elle doit être interprétée selon le contexte métier.

**Source :**  
https://www.geeksforgeeks.org/data-analysis/steps-for-mastering-exploratory-data-analysis-eda-steps/

### 1.5 Data Profiling

Le **Data Profiling** consiste à analyser automatiquement la structure et la qualité d'un dataset.

Il permet notamment d'obtenir des informations sur :
- les types de données ;
- les valeurs manquantes ;
- les valeurs uniques ;
- les distributions ;
- les statistiques descriptives ;
- les corrélations ;
- certaines anomalies.

Dans DataStore360, **ydata-profiling** a été utilisé pour générer un rapport HTML de profiling.

**Source :**  
https://www.geeksforgeeks.org/data-analysis/understanding-data-profiling/

### 1.6 Skewness

La **skewness**, ou coefficient d'asymétrie, permet de mesurer l'asymétrie d'une distribution.

```text
Skewness ≈ 0
→ distribution relativement symétrique

Skewness > 0
→ asymétrie à droite

Skewness < 0
→ asymétrie à gauche
```

Elle permet de mieux comprendre la forme des distributions et d'identifier certaines situations nécessitant une analyse complémentaire.

---

# 2. Technologies étudiées

## 2.1 uv

**uv** est un outil de gestion des projets Python et de leurs dépendances.

Il permet notamment de :
- gérer les dépendances ;
- gérer l'environnement du projet ;
- installer les packages ;
- gérer `pyproject.toml` ;
- générer `uv.lock`.

Dans DataStore360, uv est utilisé pour gérer l'environnement Python et les dépendances du projet.

uv est développé en Rust.

## 2.2 Apache Airflow

**Apache Airflow** est une plateforme open source permettant d'orchestrer des workflows.

Elle permet de :
- définir des pipelines ;
- organiser les tâches ;
- définir leurs dépendances ;
- planifier leur exécution ;
- surveiller leur état ;
- consulter les logs.

Dans DataStore360, Airflow automatise l'exécution du pipeline de données.

## 2.3 Docker

**Docker** permet d'exécuter les différents composants du projet dans des conteneurs.

DataStore360 utilise notamment des conteneurs pour :
- PostgreSQL ;
- pgAdmin ;
- Airflow Webserver ;
- Airflow Scheduler ;
- la base de métadonnées Airflow ;
- l'environnement du projet.

**Docker Compose** permet de gérer ces services ensemble.

## 2.4 PostgreSQL

**PostgreSQL** est utilisé comme système de gestion de base de données relationnelle.

Il permet de stocker les données structurées et de définir des contraintes comme :
- clés primaires (**PK**) ;
- clés étrangères (**FK**) ;
- types de données ;
- contraintes d'intégrité.

DataStore360 utilise les schémas :

```text
staging
core
```

---

# 3. Architecture des données

## 3.1 Pourquoi `staging` ?

Le schéma `staging` permet de conserver une copie des données brutes avant leur transformation.

Table utilisée :

```text
staging.superstore_raw
```

Cette zone conserve une référence aux données sources avant les opérations de nettoyage et de transformation.

## 3.2 Pourquoi `core` ?

Le schéma `core` contient les données finales destinées à être exploitées.

Les données y sont :
- nettoyées ;
- transformées ;
- structurées ;
- pseudonymisées.

Tables principales :

```text
core.customers
core.products
core.orders
```

## 3.3 Différence entre `staging` et `core`

| Staging | Core |
|---|---|
| Données brutes | Données transformées |
| Copie du dataset source | Modèle structuré |
| Peu ou pas de contraintes | PK / FK |
| Avant nettoyage | Après nettoyage |
| Données personnelles potentiellement présentes | Données pseudonymisées |

```text
CSV brut
   ↓
STAGING
   ↓
Cleaning + Transformation
   ↓
CORE
```

---

# 4. Qualité des données

## 4.1 Valeurs manquantes

Les valeurs manquantes ont été identifiées pendant l'EDA avec :

```python
df.isna().sum()
```

Le traitement dépend du contexte. Lorsqu'une valeur pouvait être récupérée de manière fiable à partir d'autres observations cohérentes, elle a été récupérée. Lorsqu'aucune information fiable n'était disponible, la valeur n'a pas été inventée.

## 4.2 Doublons

Les doublons ont été recherchés avec :

```python
df.duplicated().sum()
```

Les doublons identifiés comme réels ont été supprimés lors de la phase de nettoyage.

Le nombre de doublons supprimés est utilisé dans les statistiques finales du projet.

## 4.3 Valeurs aberrantes

Les valeurs aberrantes ont été identifiées pendant l'analyse exploratoire, notamment à l'aide de l'IQR.

Une valeur élevée ou faible n'est pas nécessairement une erreur et doit être comparée aux règles métier.

## 4.4 Incohérences

Plusieurs contrôles de cohérence ont été réalisés.

### Dates

```text
Ship Date >= Order Date
```

### Quantité

La quantité ne doit pas être négative.

### Discount

La remise doit rester dans une plage valide.

### Relations métier

Une commande doit être associée à un client et à un produit.

Les données finales sont chargées dans des tables relationnelles avec des clés primaires et étrangères.

---

# 5. RGPD

## 5.1 Données personnelles

Le champ :

```text
Customer Name
```

contient des informations permettant d'identifier directement un client.

Il nécessite donc une attention particulière lors du traitement du dataset.

## 5.2 Anonymisation

Pour éviter de conserver les noms des clients en clair dans `core`, une anonymisation a été appliquée.

```text
Customer Name
      ↓
SHA-256
      ↓
Hash
      ↓
core.customers.customer_name
```

Ainsi, `core.customers` ne contient pas les noms des clients en clair.

## 5.3 Pourquoi SHA-256 ?

SHA-256 est une fonction de hachage cryptographique produisant une empreinte de taille fixe.

Dans DataStore360, elle est utilisée pour remplacer les noms des clients par une valeur pseudonymisée.

La anonymisation ne signifie pas que les données deviennent anonymes au sens juridique. Elle constitue une mesure de protection visant à réduire l'exposition directe des données personnelles.

---

# 6. Pipeline Data Engineering

## 6.1 Extraction

La première étape consiste à lire :

```text
data/raw/store_data.csv
```

Le fichier est chargé avec Pandas.

## 6.2 Staging

Les données extraites sont chargées dans :

```text
staging.superstore_raw
```

Cette étape conserve les données brutes dans PostgreSQL avant leur transformation.

## 6.3 Cleaning

La phase de nettoyage permet notamment de :
- supprimer les doublons.
- traiter les valeurs manquantes.
- nettoyer les chaînes de caractères.
- convertir les dates.
- vérifier les incohérences.
- appliquer les règles métier.

## 6.4 Transformation

La transformation prépare les données pour leur utilisation finale.

### Anonymisation

```text
Customer Name → SHA-256
```

### Délai de livraison

```text
delivery_time = Ship Date - Order Date
```

### Marge bénéficiaire

```text
profit_margin = Profit / Sales
```

## 6.5 Loading

Les données transformées sont réparties dans :

```text
core.customers
core.products
core.orders
```

Les relations entre les tables sont assurées par les clés étrangères.

## 6.6 Validation

Après le chargement, plusieurs contrôles sont réalisés :
- nombre de lignes.
- doublons.
- valeurs manquantes.
- clés primaires.
- clés étrangères.
- cohérence des dates.
- validité des valeurs.
- présence de données personnelles en clair.

## 6.7 Statistiques

Une étape de restitution produit les statistiques finales :
- nombre de clients.
- nombre de produits.
- nombre de commandes.
- ventes par catégorie.
- ventes par région.
- ventes par segment.
- doublons supprimés.
- taux de complétude final.
- techniques RGPD appliquées.

---

# 7. Airflow

## 7.1 DAG

Un **DAG (Directed Acyclic Graph)** représente les tâches d'un workflow et leurs dépendances.

Dans DataStore360 :

```text
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
load_core
   ↓
validate
```

## 7.2 Dépendances

Une dépendance définit l'ordre d'exécution entre les tâches.

Par exemple :

```python
extract >> load_staging
```

signifie que `load_staging` doit être exécutée après `extract`.

## 7.3 Tasks

Chaque étape du pipeline est représentée par une tâche Airflow.

Exemples :

```text
extract
load_staging
clean
transform
load_customers
load_products
load_orders
validate
statistics
```

## 7.4 Logs

Airflow permet de consulter les logs de chaque tâche afin de :
- suivre l'exécution.
- afficher le nombre de lignes traitées.
- identifier les erreurs.
- vérifier les connexions.
- suivre les chargements.

---

# 8. Idempotence

## 8.1 Pourquoi l'idempotence ?

Un pipeline idempotent peut être relancé sans provoquer d'accumulation indésirable de données.

Dans DataStore360, cette propriété est importante car le pipeline peut être relancé par Airflow.

Sans mécanisme d'idempotence, une deuxième exécution pourrait provoquer des doublons ou des erreurs de clés primaires.

## 8.2 Comment elle est implémentée ?

Avant de recharger les données dans `core`, les tables sont vidées puis rechargées à partir des données transformées.

```text
Données staging
      ↓
Cleaning
      ↓
Transformation
      ↓
TRUNCATE core
      ↓
Reload core
```

Les tables sont chargées dans l'ordre permettant de respecter les dépendances :

```text
customers
    ↓
products
    ↓
orders
```

Le `staging` n'est pas supprimé car il doit conserver les données brutes.

Une deuxième exécution du pipeline permet ainsi de reconstruire le `core` sans créer de doublons.

---

# 9. Pourquoi ces choix ?

## Pourquoi `staging` ?

Conserver les données brutes avant transformation et disposer d'une référence aux données sources.

## Pourquoi `core` ?

Stocker les données nettoyées, transformées, structurées et pseudonymisées.

## Pourquoi PostgreSQL ?

Stocker les données structurées et garantir les relations grâce aux PK et FK.

## Pourquoi Airflow ?

Orchestrer les différentes étapes du pipeline, gérer leurs dépendances et suivre leur exécution.

## Pourquoi Docker ?

Isoler et reproduire l'environnement d'exécution des différents services.

## Pourquoi uv ?

Gérer les dépendances et l'environnement du projet Python.

## Pourquoi SHA-256 ?

Pseudonymiser les noms des clients afin de ne pas conserver les noms en clair dans le `core`.

## Pourquoi l'idempotence ?

Permettre de relancer le pipeline sans créer de doublons indésirables dans les tables finales.

---

# 10. Sources

- Dataset — GeeksforGeeks :  
  https://www.geeksforgeeks.org/data-science/what-is-dataset/
- EDA — GeeksforGeeks :  
  https://www.geeksforgeeks.org/data-analysis/steps-for-mastering-exploratory-data-analysis-eda-steps/
- Data Quality — GeeksforGeeks :  
  https://www.geeksforgeeks.org/data-science/what-is-data-quality-and-why-is-it-important/
- Data Profiling — GeeksforGeeks :  
  https://www.geeksforgeeks.org/data-analysis/understanding-data-profiling/
