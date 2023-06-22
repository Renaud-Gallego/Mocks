import pyautogui
import time
import keyboard

# Fonction pour bouger la souris
def move_mouse():
    pyautogui.moveRel(0, 10)

# Boucle pour bouger la souris toutes les 10 secondes pendant 10 minutes
for i in range(60):
    if keyboard.is_pressed('space'):
        break
    else:
        move_mouse()
        time.sleep(10)