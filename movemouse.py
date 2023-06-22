import pyautogui
import time

# Temps en secondes pendant lequel la souris doit bouger
duree = 3600

# Obtient la position actuelle de la souris
position_actuelle = pyautogui.position()

# Bouge la souris pendant la durée spécifiée
temps_debut = time.time()
while (time.time() - temps_debut) < duree:
    pyautogui.moveTo(position_actuelle[0] + 10, position_actuelle[1] + 10)
    pyautogui.moveTo(position_actuelle[0] - 10, position_actuelle[1] - 10)

# Retourne la souris à sa position initiale
pyautogui.moveTo(position_actuelle[0], position_actuelle[1])
