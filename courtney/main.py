# grace.courtney.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright 2022 Julia Barbosa <juliabarbosa@poli.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

TEMPLO = "https://i.imgur.com/4WE57S9.jpg"
TESOURO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgi7SJv8ULst1EochqpGSACaNpOVasSYaAOQ&usqp=CAU"
COBRA = "https://static.vecteezy.com/ti/vetor-gratis/p3/4858121-desenho-cobra-cobra-zangado-vetor.jpg"
ARANHA = "https://i.imgur.com/Dizbyyi.jpg"

from random import choice
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
        self.camaras = [Camara(contem) for contem in self.camaras]
        os_tesouros = [1,2,3,4,5,5, 7,7,9, 11,11,13,14, 15,17]
        os_tesouros = [Camara(valor, valor) for valor in os_tesouros]
        self.camaras += os_tesouros
        
    def joga(self):
        camara = choice(self.camaras)
        tinha_monstro = camara in self.criptas
        self.criptas.append(camara)
        revela = [cam.revela() for cam in self.criptas]
        cam= camara.revela()
        if tinha_monstro:
            input(f"Ja existia {cam} na {revela}. Você saiu correndo")
            return "n"
        return input(f"Você visitou {revela} achou {cam}. Continua(s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Courtney {__name__}.\nQuer jogar (s)?")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala)
    _joga_tesouro = JogaTesouro()
    while _joga_tesouro.joga() == "s":
        pass
    fala = "que pena"
    input(fala)
    

if __name__ == "__main__":

    tesouro_inca()