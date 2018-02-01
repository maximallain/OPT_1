# Optimisation

Le fichier constraint_programming.py a été écrit par Mr Dürr, professeur de CentraleSupélec

### Explication du projet

Le but de ce projet est de réaliser un mot croisé avec une grille et une
liste de mot données.

Le programme réalise une lecture des fichiers .txt
issus du dossier Data. Il repère les positions des segments dans la grille,
puis retourne leur taille. C'est ainsi que nous définissons le domaine des variables
"segments", qui ne sont autres que les mots de la liste ayant la même taille.

Nous recherchons ensuite les intersections entre les mots horizontaux et verticaux.
Cette recherche nous renvoie une liste de nouvelles variables "lettres",
dont le domaine est représenté par les 26 lettres de l'alphabet.

Nous définissons ensuite les contraintes comme un triplet (segment, lettre,
{(mot issu du domaine de segment, lettre de ce mot placé à la position de
l'intersection})

Le solveur résoud alors le programme ainsi défini et nous revoie la grille complétée.

### Utilisation du projet

Run `main.py`
