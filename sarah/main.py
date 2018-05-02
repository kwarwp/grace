# grace.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900

ALICE = "https://vignette.wikia.nocookie.net/disney/images/1/1a/Alice_KH.png"
cinderela = "http://pt-br.disneyprincesas.wikia.com/wiki/Arquivo:Tumblr_o1xpveBV601v56ooio1_500.png"
HOMEM_ARANHA = "https://vignette.wikia.nocookie.net/marvel/images/1/17/Homem-Aranha_Artigo_Destaque.png"
CIDADE = "https://png.pngtree.com/element_origin_min_pic/16/09/02/1657c93c84ebd71.jpg"
PAIS_DE_ALICE = "https://png.pngtree.com/element_origin_min_pic/16/07/21/235790ef252fe67.jpg"

def texto():
    cidade = Cena(img = CIDADE)
    pais_de_alice = Cena(img = PAIS_DE_ALICE)
    Alice = Elemento(img= ALICE, tit= "Alice", style=dict(left=150, top=290, width=150, bottom=100))
    Alice_t = Texto(cidade, "Alice foi visitar a vovó.")
    Alice.vai = Alice_t.vai
    Alice.entra(cidade)

    cidade.direita=pais_de_alice
    homem_aranha = Elemento(img= HOMEM_ARANHA, tit= "homem aranha", style=dict(left=150, top=290, width=150, bottom=100))
    cidade.vai()
    
    
    
texto()