# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
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
#from parisa.main import tesouro_inca as art_tesouro
# from courtney.main import _joga_tesouro as art_joga
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
    """Inicia o jogo do tesouro inca"""
    def __init__(self):
        self.criptas = []
        self.camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
        self.camaras = [Camara(contem) for contem in self.camaras] * 3
        os_tesouros = [1,2,3,4,5,5, 7,7,9, 11,11,13,14, 15,17]
        self.os_tesouros = [Camara(valor, valor) for valor in os_tesouros]
        self.camaras += self.os_tesouros
        shuffle(self.camaras)
        
    def joga(self):
        # camara = choice(self.camaras)
        camara = self.camaras.pop()

        tinha_monstro = (camara not in self.os_tesouros) and (camara in self.criptas) 
        self.criptas.append(camara)
        revela = [cam.revela() for cam in self.criptas]
        cam= camara.revela()
        if tinha_monstro:
            input(f"Ja existia {cam} na {revela}. Você abandonou correndo")
            return "n"
        return input(f"Você visitou {revela} achou {cam}. Continua(s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Roxanne {__name__}.Quer jogar (s)?")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala)
    # while art_joga() == "s":
    _joga_tesouro = JogaTesouro()
    while _joga_tesouro.joga() == "s":
        pass
    fala = "que pena"
    input(fala)
    

if __name__ == "__main__":
    # art_tesouro()
    tesouro_inca()

