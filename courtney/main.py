# grace.courtney.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright 2022 Julia Barbosa <juliabarbosa@poli.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

TEMPLO = "https://i.imgur.com/4WE57S9.jpg"
TESOURO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgi7SJv8ULst1EochqpGSACaNpOVasSYaAOQ&usqp=CAU"
COBRA = "https://static.vecteezy.com/ti/vetor-gratis/p3/4858121-desenho-cobra-cobra-zangado-vetor.jpg"
ARANHA = ""
from parisa.main import tesouro_inca

def tesouro_inca():
    """O jogo do tesouro Inca"""
    input(f'Bem vindo ao Tesouro Inca - versão Courtney {__name__}')
    
if __name__ == "__main__":    
    tesouro_inca()