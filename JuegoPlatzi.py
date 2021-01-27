import requests
import json
import pprint
import random
import html
import os
import time



url="https://opentdb.com/api.php?amount=1&category=21&difficulty=medium&type=multiple"
numerovalido = False
while numerovalido == False:
    numparticipantes = (input("\nEscribe el numero de personas que participaran el dia de hoy:   "))
    try:
        numparticipantes = int(numparticipantes)
        numerovalido = True
    except:
        print("La respuesta debe contener solo con numeros..........")

numerovalido=False
while numerovalido == False:
    ronda = (input("\nEscribe el numero de rondas que vas a jugar:   "))
    try:
        ronda = int(ronda)
        numerovalido = True
    except:
        print("La respuesta debe ser solo con numeros..........")

participantes =[]
j=1
i=1

while j <= numparticipantes:
    x = input("\nNombre participante numero"+str(j) + ":  ")
    participantes.append(x)
    correctas = [0] * len(participantes)
    incorrectas = [0] * len(participantes)
    j+=1
os.system("cls")
while i <= ronda:
        print("RONDA: "+str(i))
        res = 0
        for participant in participantes:
            r= requests.get(url)
            if (r.status_code != 200):
                error = input('Oooops something went wrong, please try to load it again....')
                i = i
            else:
                os.system("cls")

            numerovalido = False
            num_opciones = 1
            data = json.loads(r.text) 
            preguntas = data['results'][0]['question']
            respuestas = data['results'][0]['incorrect_answers']
            respcorrecta = data['results'][0]['correct_answer']
            respuestas.append(respcorrecta)
            random.shuffle(respuestas)

            print("\nPregunta numero "+str(i)+" para: "+participant)
            print('\n*****************************************************************')
            print('*****************************************************************')
            print(html.unescape(preguntas) + "\n")
            print('*****************************************************************')
            print('*****************************************************************\n')


            for respuesta in respuestas:
                print(str(num_opciones)+'-' +html.unescape(respuesta))
                num_opciones += 1
            while numerovalido == False:
                respuestaUsuario = input("\nEscriba el numero de la respuesta correcta:   ")
                try:
                    respuestaUsuario = int(respuestaUsuario)
                    if respuestaUsuario > len(respuestas) or respuestaUsuario <=0:
                        print("Porfavor utilice un numero que este entre el rango de los numeros de las opciones de respuesta")
                    else:
                        numerovalido = True
                except:
                    print("La respuesta debe ser solo con numeros..........")
            
            respuestaUsuario = respuestas[int(respuestaUsuario)-1]

            if respuestaUsuario == respcorrecta:
                print("\nFelicidades, tienes buenos conocimientos en este tema, efectivamente la respuesta era: "+ html.unescape(respcorrecta))
                correctas[res] += 1
            else:
                print("\nPam Pam Pam Pam, respondiste mal, tu elegiste "+html.unescape(respuestaUsuario) +". Pero la respuesta correcta era: "+html.unescape(respcorrecta))
                incorrectas[res] += 1
            time.sleep(2)
            os.system("cls")
            res +=1
        i+=1
k=0
for par in participantes:
    print("#######################################################")
    print("#########################SCORE#########################")    
    print("#######################################################")
    print(par+" tuvo: "+str(correctas[k])+" preguntas correctas")
    print(par+" tuvo: "+str(incorrectas[k])+" preguntas incorrectas")
    print("#######################################################")
    print("#######################################################\n\n")
    k+=1

input("Presione ENTER para terminar con el juego.......................")
