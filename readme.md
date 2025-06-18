# Documentation d'installation des scripts `lh-runmultiurls.sh` et `lh-createcsv.py`

## Prérequis
- Système d'exploitation : **MacOS** , **Linux** ou **Windows avec WSL**
- Outils nécessaires : **Node.js** (pour Lighthouse), **Conda** (pour Python), et un terminal

## Étapes d'installation

### 1. Installation de Node.js et Lighthouse
- Vérifiez si Node.js est installé :
  ```bash
  node -v
  ```
- Si Node.js n'est pas installé, téléchargez et installez-le depuis [nodejs.org](https://nodejs.org).
- Installez Lighthouse globalement :
  ```bash
  npm install -g lighthouse
  ```

### 2. Configuration de l'environnement Conda
- Téléchargez et installez **Miniconda** ou **Anaconda** depuis [conda.io](https://conda.io).
- Créez un nouvel environnement Conda pour le projet :
  ```bash
  conda create -n lighthouse python=3.9
  ```
- Activez l'environnement :
  ```bash
  conda activate lighthouse
  ```

### 3. Installation des modules Python
- Les modules utilisés dans `lh-createcsv.py` sont des modules **standard** de Python (`json`, `os`, `glob`, `csv`, `datetime`).
- Aucune installation supplémentaire de modules Python n'est nécessaire.

### 4. Configuration du script shell (`lh-runmultiurls.sh`)
- Rendez le script exécutable :
  ```bash
  chmod +x lh-runmultiurls.sh
Assurez-vous que le fichier urls.txt existe dans le même répertoire que lh-runmultiurls.sh. Ce fichier doit contenir la liste des URLs à tester, une URL par ligne.
Format du fichier urls.txt et options avancées

Le fichier urls.txt et le script lh-runmultiurls.sh supportent les fonctionnalités suivantes :

Commentaires dans urls.txt : Vous pouvez ajouter des commentaires dans votre fichier urls.txt en faisant précéder la ligne du caractère #. Ces lignes seront ignorées par le script. Exemple (urls.txt) :

```
# Section des sites principaux
https://www.example.com
# Section des blogs (à tester plus tard)
# https://www.example.com/blog
https://www.another-example.com
```

**Support de l'Authentification de Base** (Basic Authentication) : Pour les sites protégés par une authentification de base, vous pouvez fournir les identifiants au script via les options en ligne de commande :

```
-u <nom_utilisateur> ou --username <nom_utilisateur> : Pour spécifier le nom d'utilisateur.
-p <mot_de_passe> ou --password <mot_de_passe> : Pour spécifier le mot de passe.
-h ou --help : Pour afficher le message d'aide.
```

Le fichier urls.txt peut contenir un mélange d'URLs nécessitant une authentification et d'URLs publiques. Important : Toutes les URLs protégées par authentification de base lors d'une même exécution du script doivent utiliser les mêmes identifiants. Le script ne prend en charge qu'un seul jeu d'identifiants par appel.

Exemple d'appel du script avec authentification :

```./lh-runmultiurls.sh -u monutilisateur -p monmotdepasse```

### 5. Exécution des scripts
- Exécutez le script shell pour générer les rapports Lighthouse :
  ```bash
  ./lh-runmultiurls.sh
  ```
- Les rapports JSON seront générés dans le dossier `results`.
- Exécutez le script Python pour transformer les rapports JSON en CSV :
  ```bash
  python lh-createcsv.py
  ```

### 6. Exploitation du rapport CSV
- **Localisation du fichier** : Le fichier CSV est généré dans le dossier `results` avec un nom comme `lh-results-YYYY-MM-DD_HH-MM-SS.csv`.
- **Ouverture du fichier** :
  - Utilisez un tableur comme **Microsoft Excel**, **Google Sheets**, ou **LibreOffice Calc** pour ouvrir le fichier CSV.
  - Importez le fichier dans Google Sheets via "Fichier > Importer" ou ouvrez-le directement dans Excel/Calc.
- **Analyse des données** :
  - Le CSV contient les colonnes : `date`, `url`, `source_file`, `performance_percent`, `fcp`, `lcp`, `total_byte_weight`.
  - **performance_percent** : Score de performance (0-100). Un score > 90 est excellent.
  - **fcp** (First Contentful Paint) : Temps (en ms) pour le premier affichage de contenu. Visez < 1800 ms.
  - **lcp** (Largest Contentful Paint) : Temps (en ms) pour le rendu du plus grand élément. Visez < 2500 ms.
  - **total_byte_weight** : Poids total des ressources (en octets). Réduisez pour améliorer la vitesse.
- **Utilisation** :
  - Triez les URLs par `performance_percent` pour identifier les pages à optimiser.
  - Comparez `fcp` et `lcp` pour détecter des problèmes de chargement.
  - Exportez les données dans des graphiques (via Excel/Sheets) pour visualiser les performances.
  - Archivez les CSV pour suivre l'évolution des performances au fil du temps.

## Remarques
- Assurez-vous que le dossier `results` existe ou sera créé automatiquement par `lh-runmultiurls.sh`.
- Les scripts doivent être exécutés dans un terminal sous **MacOS** ou **Linux**.
- Si vous rencontrez des erreurs, vérifiez que Node.js, Lighthouse et Conda sont correctement installés.
