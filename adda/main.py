# grace.adda.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900

HOMEM_ARANHA = "http://www.purarteadesivos.com.br/wp-content/uploads/2017/05/Homem-aranha-300x300.png"
ALICE = "https://3.bp.blogspot.com/-9TV8MKrd94M/V2YHE_KbLXI/AAAAAAAAGPA/iQwHwGeAucspu3Pp6UcchZQf3K2ce_g5wCLcB/s320/1e.png"
YODA = "http://pngimg.com/uploads/starwars/starwars_PNG8.png"
CASINHA ="http://bpic.588ku.com/element_pic/17/03/05/a867840a9f2d8557c1fbf2297a5b26a0.jpg"
PANTANO = "http://pt.clubpenguinwiki.info/static/images/cpwpt/thumb/4/4b/Festa_de_Halloween_2011_Labirinto_do_P%C3%A2ntano.png/250px-Festa_de_Halloween_2011_Labirinto_do_P%C3%A2ntano.png"
CASTELO = "https://i.pinimg.com/originals/10/a7/8a/10a78a8d28dcfc1999848a8815e23679.png"

def tale():
   casinha = Cena(img = CASINHA)
   homem_aranha = Elemento(img = HOMEM_ARANHA, tit = "homem_aranha", style = dict(left= 100, top= 100, width= 100, hight= 100))
   homem_aranha.entra(casinha)
   
   castelo = Cena(img = CASTELO)
   alice = Elemento(img = ALICE, tit="alice", style = dict(left= 100, top= 100, width= 100, hight= 100))
   alice.entra(castelo)
   
   pantano = Cena(img = PANTANO)
   yoda = Elemento(img = YODA, tit="yoda", style = dict(left= 100, top= 100, width= 100, hight= 100))
   yoda.entra(pantano)
   
   casinha.vai()

tale()