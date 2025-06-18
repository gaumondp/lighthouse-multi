[Version français de la documentation](#FR)

# Installation documentation for `lh-runmultiurls.sh` and `lh-createcsv.py` scripts

## Prerequisites
- Operating system: **MacOS**, **Linux** or **Windows with WSL**
- Required tools: **Node.js** (for Lighthouse), **Conda** (for Python), and a terminal

## Installation steps

### 1. Installing Node.js and Lighthouse
- Check if Node.js is installed:
  ```bash
  node -v
  ```
- If Node.js is not installed, download and install it from [nodejs.org](https://nodejs.org).
- Install Lighthouse globally:
  ```bash
  npm install -g lighthouse
  ```

### 2. Setting up the Conda environment
- Download and install **Miniconda** or **Anaconda** from [conda.io](https://conda.io).
- Create a new Conda environment for the project:
  ```bash
  conda create -n lighthouse python=3.9
  ```
- Activate the environment:
  ```bash
  conda activate lighthouse
  ```

### 3. Installing Python modules
- The modules used in `lh-createcsv.py` are **standard** Python modules (`json`, `os`, `glob`, `csv`, `datetime`).
- No additional Python module installation is required.

### 4. Configuring the shell script (`lh-runmultiurls.sh`)
- Make the script executable:
  ```bash
  chmod +x lh-runmultiurls.sh
  ```
- Ensure that the `urls.txt` file exists in the same directory as `lh-runmultiurls.sh`. This file must contain the list of URLs to test, one URL per line.

## Format of the urls.txt file and advanced options

The `urls.txt` file and the `lh-runmultiurls.sh` script support the following features:

**Comments in urls.txt**: You can add comments to your `urls.txt` file by prefixing the line with the `#` character. These lines will be ignored by the script. Example (urls.txt):

```
# Main sites section
https://www.example.com
# Blog section (to test later)
# https://www.example.com/blog
https://www.another-example.com
```

**Basic Authentication Support**: For sites protected by basic authentication, you can provide credentials to the script via command line options:

```
-u <username> or --username <username>: To specify the username.
-p <password> or --password <password>: To specify the password.
-h or --help: To display the help message.
```

The `urls.txt` file can contain a mix of URLs requiring authentication and public URLs. Important: All URLs protected by basic authentication during the same script execution must use the same credentials. The script only supports one set of credentials per call.

Example script call with authentication:

```./lh-runmultiurls.sh -u myusername -p mypassword```

### 5. Running the scripts
- Run the shell script to generate Lighthouse reports:
  ```bash
  ./lh-runmultiurls.sh
  ```
- JSON reports will be generated in the `results` folder.
- Run the Python script to transform JSON reports into CSV:
  ```bash
  python lh-createcsv.py
  ```

### 6. Using the CSV report
- **File location**: The CSV file is generated in the `results` folder with a name like `lh-results-YYYY-MM-DD_HH-MM-SS.csv`.
- **Opening the file**:
  - Use a spreadsheet application like **Microsoft Excel**, **Google Sheets**, or **LibreOffice Calc** to open the CSV file.
  - Import the file into Google Sheets via "File > Import" or open it directly in Excel/Calc.
- **Data analysis**:
  - The CSV contains the columns: `date`, `url`, `source_file`, `performance_percent`, `fcp`, `lcp`, `total_byte_weight`.
  - **performance_percent**: Performance score (0-100). A score > 90 is excellent.
  - **fcp** (First Contentful Paint): Time (in ms) for the first content display. Aim for < 1800 ms.
  - **lcp** (Largest Contentful Paint): Time (in ms) for rendering the largest element. Aim for < 2500 ms.
  - **total_byte_weight**: Total weight of resources (in bytes). Reduce to improve speed.
- **Usage**:
  - Sort URLs by `performance_percent` to identify pages to optimize.
  - Compare `fcp` and `lcp` to detect loading issues.
  - Export data to charts (via Excel/Sheets) to visualize performance.
  - Archive CSVs to track performance evolution over time.

## Notes
- Ensure that the `results` folder exists or will be created automatically by `lh-runmultiurls.sh`.
- The scripts must be run in a terminal under **MacOS** or **Linux**.
- If you encounter errors, verify that Node.js, Lighthouse, and Conda are properly installed.

<a id="FR"></a>
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
