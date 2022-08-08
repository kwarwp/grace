# grace.parisa.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Art Adriel <art.adriel@gmail.com>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
""" O Jogo do Tesouro Inca

    Um grupo de aventureiros se arrisca em uma escavação antiga de um templo inca.
    
    Changelog
    ---------
    * função tesouro_inca - executa o jogo.
    * função _joga_tesouro - avança na cripta.
"""
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
MONSTRO = "https://i.imgur.com/lcvvL1B.png"
PERIGOS = "p2jHT5d ho6ZMAL G2u6KB1 awwkaBO hZ0ohTz"

from random import choice 

class Camara: 
    def __init__(self, conteudo, valor=0):
       self.conteudo = conteudo
       self.valor = valor
    def revela(self):
       return self.conteudo
    def resgata(self, jogadores):
       butim, sobra = self.valor // jogadores, self.valor % jogadores
       # butim = self.valor // jogadores
       # sobra = self.valor % jogadores
       self.valor = sobra
       return butim
     def __str__(self):
        return self.conteudo
class Incursao:
    pass 

class Tumba: 
    pass   

class Jogador: 
    pass

class JogaTesouro():
    """Incia o jogo do tesouro Inca"""
    def __init__(self):
       self.criptas=[]
       self.camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
       self.camaras = [camara(contem) for contem in self.camaras]
    
    def joga(self):
        camara = choice(self.camaras)  # sortear os perigos
        tinha_monstro = camara in self.criptas
        self.criptas.append(camara)
        if tinha_monstro:
            input(f"Ja existia {camara} na {self.criptas}. Você abandonou correndo")
            return "n"
        return input(f"Você visitou {self.criptas} achou {camara}. Continua(s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Parisa {__name__}. Quer jogar? (s ou n)")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala) 
    joga_tesouro = JogaTesouro()
    while joga_tesouro.joga() == "s":
      pass
    fala = "que pena"
    input(fala)
    
if __name__== "__main__": 
  tesouro_inca()