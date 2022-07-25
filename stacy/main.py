# grace.stacy.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Claudia Motta <claudiam@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
jogar = input ("Quer jogar o Tesouro Inca?")
tumba = lis("AMCDI"*3)
if jogar == "s" or "S" or "sim"or "SIM":
    input ("Vamos nesta!")
     for camara in tumba:
        input(f"Você encontrou {camara}")
else:
    input ("fica para próxima")