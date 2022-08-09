# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
""" O Jogo do Tesouro Inca """
#Templo = "https://i.imgur.com/DuyTTha.jpg"
#Tesouro = "https://i.imgur.com/OuPgmla.jpg"
#A = "https://imgur.com/iCrJ46A"
#M = "https://imgur.com/a/KYT6HiQ"
#I = "https://imgur.com/xYv9YdG"
#C = "https://i.imgur.com/8VfAotu.jpg"
#D = "https://i.imgur.com/OHmUIhz.jpg"

"""importacao de diretorio / biblioteca"""
from random import choice, shuffle

"""classe / modulos"""
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
        """Camaras já reveladas pelos aventureiros """
        camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
        self.camaras = [Camara(contem) for contem in camaras] * 3
        """Camaras contidas no Templo """
        os_tesouros = [1,2,3,4,5,5, 7,7,9, 11,11,13,14, 15,17]
        self.os_tesouros = [Camara(valor, valor) for valor in os_tesouros]
        """Camaras contidas no Templo que contêm tesouros"""
        self.camaras += self.os_tesouros
        shuffle(self.camaras)
        
    def joga(self):
        """Executa uma jogada, revelando uma câmara 
        
           :return: Se o jogo continua, retorna "s"
        """
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
    _joga_tesouro = JogaTesouro()
    while _joga_tesouro.joga() == "s":
        pass
    fala = "que pena"
    input(fala)
    

if __name__ == "__main__":
    tesouro_inca()

