import os

# Spécifiez le chemin du dossier que vous voulez lister.
dossier = "C:/Users/renaud.gallego/Documents/perso"

# Utilisez la fonction listdir() pour obtenir une liste de tous les fichiers et dossiers dans le dossier spécifié.
fichiers = os.listdir(dossier)

# Parcourez la liste de fichiers et affichez leur nom.
for fichier in fichiers:
    # Vérifiez si l'élément est bien un fichier (et pas un répertoire) avant de l'afficher.
    if os.path.isfile(os.path.join(dossier, fichier)):
        print(fichier)