import keyboard
import time
import random

DURATION = 60 * 120  # 120 minutes

def write_text():
    num = random.randint(1200, 2050)
    text = "UTAH-" + str(num) + "\n"
    keyboard.write(text)  # écrit le texte avec la valeur de num_str dans l'application active

for i in range(DURATION):
    if i == 0:
        time.sleep(5) # Ajout du délai de 5 secondes avant le premier appel à write_text()
    write_text()
    time.sleep(10)
