# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
jogar = input ("Quer jogar o tesouro Inca?")
tumba = list("AMCDI"*3)
corredor = []
if jogar == 's':
    input("simbora!")
    for camara in tumba:
        corredor.append(camara)
        input(f"Você já encontrou {corredor}")
else:
    input("pena!")