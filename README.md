# Habit Tracker API - Backend

Ce projet est une solution intelligente de suivi d'habitudes. Contrairement à une simple liste de tâches, cette API connecte les actions quotidiennes à des objectifs de vie à long terme, tout en automatisant le feedback et l'analyse des progrès.

## Table des Matières

1. [Habit Tracker API - Backend](#habit-tracker-api---backend)
   - [Installation et Configuration](#installation-et-configuration)
     - [1. Environnement virtuel](#1-environnement-virtuel)
     - [2. Installation des dépendances](#2-installation-des-dépendances)
     - [3. Base de données et Serveur](#3-base-de-données-et-serveur)
   - [Fonctionnalités](#fonctionnalités)
     - [1. Authentification](#1-authentification)
     - [2. Habitudes (Tâches et Journal)](#2-habitudes-tâches-et-journal)
     - [3. Objectifs (Goals)](#3-objectifs-goals)
     - [4. Notifications](#4-notifications)
     - [5. Analytique](#5-analytique)
   - [Documentation Interactive (Swagger)](#documentation-interactive-swagger)
   - [Points d'entrée de l'API](#points-dentrée-de-lapi)
   - [Architecture du Projet](#architecture-du-projet)
   - [Travaux restants et Améliorations](#travaux-restants-et-améliorations)

---

## Installation et Configuration

### 1. Environnement virtuel

Exécutez les commandes suivantes dans le répertoire racine :

```bash
python -m venv venv
# Activation (Windows)
venv\Scripts\activate
# Activation (macOS/Linux)
source venv/bin/activate

```

### 2. Installation des dépendances

```bash
pip install -r requirements.txt

```

### 3. Base de données et Serveur

```bash
python manage.py migrate
python manage.py runserver

```

L'API est accessible à l'adresse : `http://127.0.0.1:8000/api/`

---

## Fonctionnalités

### 1. Authentification

- **Méthode Classique** : Inscription et connexion standard via un email et un mot de passe.
- **Connexion Google** : Intégration de Google OAuth2 permettant une connexion rapide. Le compte est automatiquement créé en base de données lors de la première connexion. Pour le déploiement, la configuration des clés Google est automatisée via le fichier `.env`.

### 2. Habitudes (Tâches et Journal)

Ce module gère le quotidien de l'utilisateur.

- **Tâches** : Création de listes d'actions quotidiennes à accomplir.
- **Journal** : Un espace pour consigner des réflexions quotidiennes, permettant de garder une trace écrite de son état d'esprit et de ses progrès.

### 3. Objectifs (Goals)

Cette fonctionnalité structure les ambitions à long terme en les liant aux actions quotidiennes.

- **Relation Goals/Tasks** : Un objectif est relié à une ou plusieurs tâches spécifiques.
- **Complétion Automatique** : La logique métier surveille l'avancement des tâches. Dès que toutes les tâches liées à un objectif sont marquées comme terminées, l'objectif est automatiquement validé par le système.

### 4. Notifications

Le système communique automatiquement avec l'utilisateur selon ses actions.

- **Création** : Une notification est générée instantanément lors de la création d'un nouvel "Goals" ou lorsqu'un "Goal" est atteint.
- **Gestion** : L'utilisateur peut consulter ses alertes et les marquer comme "lues" pour vider sa boîte de réception.

### 5. Analytique

- **Indicateurs de Performance** : Calcule le taux de réussite global des tâches en pourcentage.
- **Suivi par ID** : Pour une précision maximale, le système liste non seulement les compteurs (nombre de tâches finies), mais aussi les identifiants (IDs) précis des tâches et objectifs en cours ou terminés. Cela permet d'identifier exactement ce qui a été accompli.

---

## Documentation Interactive (Swagger)

L'API inclut une documentation complète et interactive accessible via Swagger UI. Cela permet de tester les fonctionnalités sans installer de logiciel tiers.

- **Accès** : `http://127.0.0.1:8000/api/docs/`
- **Usage** : Permet de visualiser tous les paramètres requis pour chaque requête (GET, POST, etc.) et de visualiser les réponses en temps réel.

---

## Points d'entrée de l'API

| Endpoint                  | Méthode   | Description                               |
| ------------------------- | --------- | ----------------------------------------- |
| `/api/auth/login/`        | POST      | Connexion session classique               |
| `/accounts/google/login/` | GET       | Connexion via Google OAuth2               |
| `/api/habits/tasks/`      | GET/POST  | Gestion des tâches quotidiennes           |
| `/api/goals/`             | GET/POST  | Gestion des objectifs à long terme        |
| `/api/analytics/`         | GET       | Vue d'ensemble des progrès (statistiques) |
| `/api/notifications/`     | GET/PATCH | Consultation et gestion des alertes       |
| `/api/habits/journals/`   | GET/POST  | Notes de réflexion et journal de bord     |

---

## Architecture du Projet

- **`apps.users`** : Sécurité, gestion des comptes et intégration Google.
- **`apps.habits`** : Gestion opérationnelle (Tâches et Journal).
- **`apps.goals`** : Vision stratégique et calculs de progression.
- **`apps.notifications`** : Système de communication interne automatisé.
