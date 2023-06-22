import keyboard
import time

# Fonction pour écrire le texte "UTAH"
def write_utah():
    keyboard.press('u')
    keyboard.release('u')
    keyboard.press('t')
    keyboard.release('t')
    keyboard.press('a')
    keyboard.release('a')
    keyboard.press('h')
    keyboard.release('h')

# Boucle principale qui s'exécute pendant 10 minutes
for i in range(60 * 10):
    # Appel de la fonction pour écrire "UTAH"
    write_utah()
    # Attendre 10 secondes
    time.sleep(10)