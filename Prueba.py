playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

y=0
x=0
larga = playlist[0]["title"]
largaDuracion = playlist[0]["duration"].split(":")
corta = playlist[0]["title"]
cortaDuracion = playlist[0]["duration"].split(":")
for cancion in playlist:
    partes = cancion["duration"].split(":")
    if int(partes[1]) + y > 60:
        y+= int(partes[1])-60
        x+=1
    else:
        y+= int(partes[1])
    x+= int(partes[0])
    
    if partes[0] > largaDuracion[0]:
        largaDuracion= partes
        larga= cancion["title"]
    elif partes[0] == largaDuracion[0]:
        if partes[1] > largaDuracion[1]:
            largaDuracion= partes
            larga= cancion["title"]
            
    if partes[0] < cortaDuracion[0]:
        cortaDuracion= partes
        corta= cancion["title"]
    elif partes[0] == cortaDuracion[0]:
        if partes[1] < cortaDuracion[1]:
            cortaDuracion= partes
            corta= cancion["title"]
    

print("La duracion de la playslist es: ", x,":",y)
print("La cancion mas corta es:", corta,"Con una duracion de: ", cortaDuracion)
print("La cancion mas larga es:", larga,"Con una duracion de: ", largaDuracion)