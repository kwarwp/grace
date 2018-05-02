# grace.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900

ALICE = "http://disney.wikia.com/wiki/File:Alice_KH.png"
cinderela = "http://pt-br.disneyprincesas.wikia.com/wiki/Arquivo:Tumblr_o1xpveBV601v56ooio1_500.png"
Homem_aranha = "http://pt-br.marvel.wikia.com/wiki/Arquivo:Homem-Aranha_Artigo_Destaque.png"
CIDADE = "https://png.pngtree.com/element_origin_min_pic/16/09/02/1657c93c84ebd71.jpg"
pais_de_alice = "https://png.pngtree.com/element_origin_min_pic/16/07/21/235790ef252fe67.jpg"

def texto():
    cidade = Cena(img = CIDADE)
    Alice = Elemento(img= ALICE, tit= "Alice", style=dict(left=100, top=100, width=100, bottom=100))
    cidade.vai()
    

texto()