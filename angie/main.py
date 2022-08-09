#grace.angie.main.py 
#_*_ coding: UTF8 _*_
#This file is part of program Jogo Inca
#Copyrigth c 2022 Vanessa Vianna <vanmvianna@gmail.com>,
#SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""Imagens"""
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
    """Uma camara do templo que contem um tesouro ou perigo
    Keyword arguments:
    :param: conteudo: o descritor do conteúdo da camara, perigo ou tesouro
    :param: valor: o número de tesouros que estão na câmara
    """
    def __init__(self, conteudo, valor=0):
        self.conteudo = conteudo
        self.valor = valor
    def revela(self):
        return self.conteudo
    def resgata(self, jogadores):
        """Divide o conteúdo que estava oculto na câmara por um grupo de aventureiros
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
class jogador: 
    pass

class JogaTesouro():

    def __init__(self):
        self.criptas = []
        camaras = ["Aranha", "Mumia", "Cobra", "Desabamento", "Incendio"]
        self.camaras = [Camara(contem) for contem in camaras] * 3
        os_tesouros = [1,2,3,4,5,5,7,7,9,11,11,13,14,15,17]
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
            tesouro_inca()