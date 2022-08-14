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

from random import choice, shuffle 

class Camara: 
    """ Uma camara do templo que contem um tesouro ou perigo 
    
        :param: conteudo: o descritor do conteúdo da camara, perigo ou tesouro
        :param:valor: o número de tesouros que estão na câmara
    """
    def __init__(self, conteudo, valor=0):
       self.conteudo = conteudo
       self.valor = valor
    
    def revela(self):
       """ Mostra o conteúdo que estava oculto na câmara"""
       return self.conteudo
    
    def resgata(self, jogadores):
       """ Divide o conteúdo que estava oculto na câmara por um grupo de aventureiros
        
            :param: jogadores: o número de aventureiros que vão dividir o tesouro
            :return: o número de tesouros que cabe a cada aventureiro
        """
        butim, sobra = self.valor // jogadores, self.valor % jogadores
       # butim = self.valor // jogadores
       # sobra = self.valor % jogadores
       self.valor = sobra
       return butim
     
     def __repr__(self):
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
       """Camaras já reveladas pelos aventureiros """
       camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
       self.camaras = [camara(contem) for contem in self.camaras] * 3
       """Camaras contidas no Templo """
       os_tesouros = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 12, 13, 14, 15, 17]
       self.os_tesouros = [camara(valor, valor) for valor in os_tesouros]
       self.camaras += os_tesouros
       shuffle(self.camaras)
    
    def joga(self):
        """Executa uma jogada, revelando uma câmara 
        
           :return: Se o jogo continua, retorna "s"
        """
        # camara = choice(self.camaras)
        #camara = choice(self.camaras)  # sortear os perigos
        camara = self.camaras.pop()
        tinha_monstro = (camara not in self.os_tesouros) and (camara in self.criptas)
        self.criptas.append(camara)
        revela = [cam.revela() for cam in self.criptas]
        cam= camara.revela()
        if tinha_monstro:
            input(f"Ja existia {cam} na {self.criptas}. Você abandonou correndo")
            return "n"
        return input(f"Você visitou {self.criptas} achou {cam}. Continua(s)")

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