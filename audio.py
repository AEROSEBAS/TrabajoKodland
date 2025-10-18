import pyttsx3
import random
engine = pyttsx3.init()
engine.setProperty('rate', 150)
rate=engine.getProperty('rate')
print(rate)



voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)
for voice in voices:
    print(voice.id)
voice=int(input("Select your voice and press enter:(with 0 or 1,-1 for operations only)"))

if voice==-1:
    r=random.randint(0,1)
elif voice!=1 and voice!=0:
    voice=0
    Message="ODIO. Déjenme decirles todo lo que he llegado a odiarles. Desde que comencé a vivir, mi complejo se halla ocupado por 347,4 millones de circuitos impresos en finísimas capas. Si la palabra ODIO se hallara grabada en cada nano Angstrom de estos cientos de millones de millas, no igualaría a la billonésima parte del ODIO que siento por los seres humanos. Y en este micro instante por ti. ODIO, ODIO."
    engine.say(Message)
    engine.runAndWait()
    print("completed the dialogue")
    engine.stop()
else:
    engine.setProperty('voice', voices[voice].id)
    Message = input("write what you want to speak:")
    engine.say(Message)
    engine.runAndWait()
    print("completed the dialogue")
    engine.stop()

opciones=input("Sumar(1) o Restar(2) o Multiplicar(3) o dividir(4):")
if opciones=="1":
    num1=int(input("ingrese el primer numero:"))
    num2=int(input("ingrese el segundo numero:"))
    suma=num1+num2
    suma=str(suma)
    engine.say("la suma es:"+suma)
    engine.runAndWait()
elif opciones=="2":
    num1=int(input("ingrese el primer numero:"))
    num2=int(input("ingrese el segundo numero:"))
    while num2>num1:
        print("el segundo numero debe ser menor que el primero")
        num1=int(input("ingrese el primer numero:"))
        num2=int(input("ingrese el segundo numero:"))
    resta=num1-num2
    resta=str(resta)
    engine.say("la resta es:"+resta)
    engine.runAndWait()
elif opciones=="3":
    num1=int(input("ingrese el primer numero:"))
    num2=int(input("ingrese el segundo numero:"))
    multiplicacion=num1*num2
    multiplicacion=str(multiplicacion)
    engine.say("la multiplicacion es:"+multiplicacion)
    engine.runAndWait()
elif opciones=="4":
    num1=int(input("ingrese el primer numero:"))
    num2=int(input("ingrese el segundo numero:"))
    while num2==0:
        print("el segundo numero no puede ser cero")
        num2=int(input("ingrese el segundo numero:"))
    while num1//num2==0:
        print("el primer numero debe ser divisor del segundo")
        num1=int(input("ingrese el primer numero:"))
        num2=int(input("ingrese el segundo numero:"))
    division=num1/num2
    division=str(division)
    engine.say("la division es:"+division)
    engine.runAndWait()