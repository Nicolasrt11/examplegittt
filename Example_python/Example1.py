"""
    Fecha: 18/09/2023
    Autor: Nicolas
    Objetivo: Ejemplo de versionamiento
"""

import random

random_numer = random.randint(1,10)
print(random_numer)

for i in range(0, 10): 
    random_numer = random.randrange(20,100, 5)
    print(random_numer)

print("_----------------------------------------")

for i in range(0, 10): 
    random_numer = random.uniform(10.5, 20.6)
    print(random_numer)
 