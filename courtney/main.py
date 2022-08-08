# grace.courtney.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright 2022 Julia Barbosa <juliabarbosa@poli.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

TEMPLO = "https://i.imgur.com/4WE57S9.jpg"
TESOURO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgi7SJv8ULst1EochqpGSACaNpOVasSYaAOQ&usqp=CAU"
COBRA = "https://static.vecteezy.com/ti/vetor-gratis/p3/4858121-desenho-cobra-cobra-zangado-vetor.jpg"
ARANHA = "https://i.imgur.com/Dizbyyi.jpg"
from parisa.main import tesouro_inca as art_tesouro
from random import choice
criptas = []

class Camara:
    def __init__(self, conteudo, valor = 0):
        self.conteudo = conteudo
        self.valor = valor
    def revela

class jogaTesouro():
    """Inicia o jogo do tesouro inca"""
    def __init__(self):
        self.criptas = []
        camaras = ['Aranha','Cobra', 'Mumia', 'Desabamento', 'Incendio']
    def joga(self):
        camara = choice(camaras)
        tinha_monstro = camara in self.criptas
        self.criptas.append(camara)
        if tinha_monstro:
            input(f'Já existia {camara} na {self.criptas}. Vocêsaiu correndo')
            return 'n'
        return input('Você visitou {self.criptas} e achou {camara}. Continua(s)?')


def tesouro_inca():
    """O jogo do tesouro Inca"""
    quer = input(f'Bem vindo ao Tesouro Inca - versão Courtney {__name__} \n Quer jogar(s)?')
    fala = 'beleza' if quer =='s' else 'que triste'
    input(fala)
    while _joga_tesouro() == 's':
        pass
    fala = 'poxa, que pena'
    input(fala)
    joga_tesouro = jogaTesouro()
if __name__ == "__main__":    
    #art_tesouro()
    tesouro_inca()