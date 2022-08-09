#grace.angie.main.py 
#_*_ coding: UTF8 _*_
#This file is part of program Jogo Inca
#Copyrigth c 2022 Vanessa Vianna <vanmvianna@gmail.com>,
#SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""Imagens"""
Templo = "https://i.imgur.com/DuyTTha.jpg"
Tesouro = "https://i.imgur.com/OuPgmla.jpg"
Aranha = "https://imgur.com/iCrJ46A"
Mumia = "https://imgur.com/a/KYT6HiQ"
Incendio = "https://imgur.com/xYv9YdG"
Cobra = "https://i.imgur.com/8VfAotu.jpg"
Desabamento = "https://i.imgur.com/OHmUIhz.jpg"

"""importacao de diretorio / biblioteca"""
#from parisa.main import tesouro_inca as art tesouro
#from courtney.main import _joga_tesouro as art_joga

from random import choice, shuffle 

"""classe / modulos"""
class Camara: 
    def __init__(self, conteudo, valor=0):
        self.conteudo = conteudo
        self.valor = valor
    def revela(self):
        return self.conteudo
    def resgata(self, jogadores):
        butim, sobra = self.valor // jogadores, self.valor % jogadores
        self.valor = sobra
        return butim 
    def __repr__(self):
        return self.conteudo
        
class JogaTesouro():
    def __init__(self):
        self.criptas = []
        camaras = ["Aranha", "Mumia", "Cobra", "Desabamento", "Incendio"]
        self.camras = [Camara(contem) for contem in camaras] * 3
        os_tesouros = [1,2,3,4,5,5,7,7,9,11,11,13,14,15,17]
        self.camaras += self.os_tesouros
        shuffle(self.camaras)
    def joga(self):
        camara = self.camaras.pop()
        tinha_monstro = (camara not in self.os_tesouros) and (camara in self.criptas)
        self.criptas.append(camara)
        revela = [cam.revela() for cam in self.criptas]
        cam= camara.revela()
        if tinha_monstro:
            input(f"ja existia {cam} na {revela}. Você abandonou correndo")
            return "n"
        return input(f"Você visitou {revela} achou {cam}. Continua(s)")
    def tesouro_inca():
        quer = input(f"Bem vindo ao Tesouro Inca - versão Angie {__name__}. Quer jogar (s)?")
        fala = "beleza" if quer == "s" else "que triste"
        input(fala)
        _joga_tesouro = JogaTesouro()
        while _joga_tesouro.joga() == "s":
            pass
        fala = "que pena"
        input(fala)
        if __name__ == "__main__":
            # art_tesouro()
            tesouro_inca()
        

     




