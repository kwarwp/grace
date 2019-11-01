# grace.kathryn.main.py
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
SAKU="http://www.dlf.pt/png/big/1/11494_soldado-png.png"
VEGETAL="https://i.pinimg.com/originals/e7/3b/2e/e73b2e5be3fa6db607b547707f48d83e.jpg"
class brulu():
    saku= Elemento(img=SAKU)
    vegetal= Cena(img=VEGETAL)
    saku.entra(vegetal)
    vegetal.vai()
brulu()
