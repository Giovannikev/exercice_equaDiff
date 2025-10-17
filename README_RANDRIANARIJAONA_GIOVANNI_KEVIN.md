
# Exercices Équations Différentielles

## Installation

```bash
# Entrer dans le dossier 
cd exercice_equaDiff

# Création de l'environnement virtuel
python -m venv .venv

# Activation de l'environnement virtuel
# Pour Windows
.venv\Scripts\activate
# Pour Linux/macOS
# source .venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt
```

## Exécution des scripts

Après avoir activé l'environnement virtuel et installé les dépendances, vous pouvez exécuter les scripts :

### Exécuter les exercices

```bash
python -m scripts.run_exercises
```

## Dépannage

### ModuleNotFoundError: No module named 'src' ou 'utils'

Si vous rencontrez des erreurs `ModuleNotFoundError`, assurez-vous que vous exécutez les scripts en tant que modules Python depuis la racine du projet, comme indiqué ci-dessus.

### ModuleNotFoundError: No module named 'numpy' (ou autre bibliothèque)

Assurez-vous que toutes les dépendances sont installées en exécutant `pip install -r requirements.txt` après avoir activé l'environnement virtuel.

### Erreur de nom de fichier

Vérifiez que les noms de fichiers correspondent exactement aux importations dans le code.
