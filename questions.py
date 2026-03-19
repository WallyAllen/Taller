import random

categorias = {
    "Programacion": ["python", "programa", "variable", "funcion", "bucle"],
    "Animales": ["perro", "gato", "elefante", "jirafa"],
    "Comida": ["pizza", "hamburguesa", "fideos", "ensalada"]
}

print("¡Bienvenido al Ahorcado!")
print("Elegí alguna de nuestras categorias:")
for categoria in categorias.keys():
    print(categoria)  

eleccion = input("Ingresá tu seleccion: ")
if eleccion in categorias:
    words = random.sample(categorias[eleccion], k=3)        #la variable k selecciona la cantidad de palabras distintas que elige
for word in  words:
    print("empezando nueva ronda") 
    guessed = []                                     #cambie el lugar donde se definen las variables para que el bucle for las resetee
    attempts = 10
    score += 10                             #No sé si es correcto, pero ahora le sumo 10 por cada iteracion, asi mantiene un score final
    while attempts > 0:                                     #ahora este while esta dentro del for
                                          # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        
        print(progress)
        
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            score += 6       #se que puedo hacer directamente print(score + 6) pero de esta forma NO modificaria el valor
            print(score)
            break
            
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        
        if len(letter) > 1:
            print("Entrada no válida.")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
            
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0
        print(score)