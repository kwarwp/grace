# grace.courtney.main.py
from _spy.vitollino.main import Cena, STYLE
from random import shuffle
STYLE.update(width=500, height=200)
TEMPLO = "https://i.imgur.com/4WE57S9.jpg"
TESOURO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgi7SJv8ULst1EochqpGSACaNpOVasSYaAOQ&usqp=CAU"
COBRA = "https://static.vecteezy.com/ti/vetor-gratis/p3/4858121-desenho-cobra-cobra-zangado-vetor.jpg"
ARANHA = ""
DESABAMENTO = ""
templo = Cena(TEMPLO)
cenaTesouro = Cena(TESOURO)
cobra = Cena(COBRA)
aranha = Cena(ARANHA)
desabamento = Cena(DESABAMENTO)
jogar = input ("Quer jogar o tesouro Inca?")
tumba = list("AMCDI"*3)
tesouro = [1,2,3,4,5,6,7,8,9]*2
tumba += tesouro
shuffle(tumba)
corredor = []
mochila = 0
templo.vai()
if jogar == 's':
    input("Que legal, vamos jogar!")
    for camara in tumba:
        dois_monstros = (camara not in tesouro) and (camara in corredor)
        eh_tesouro = camara in tesouro
        if eh_tesouro:
            mochila += camara
            cenaTesouro.vai()
            corredor.append(camara)
        fica = input(f"Você já encontrou {corredor}, fica(s) ou sai(n)")
        if dois_monstros:
            input("você perdeu")
            mochila = 0
            break
        if fica != "s":
            input(f"Voce desistiu, mas ficou com {mochila} tesouros")
            break
else:
    input("Poxa, que pena")