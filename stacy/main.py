# grace.stacy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900


BARBIE = "https://i.pinimg.com/originals/d1/e5/89/d1e589ccc516cbec88da10415a77c947.png"
HOMEM_ARANHA = "https://2.bp.blogspot.com/-Sx288TzGsV0/V5E7WpC1S2I/AAAAAAAALNE/46iReRzHSMslkQKxOgLr6jb5Pl4LTXEnwCLcB/s1600/B78144.jpg"
CASA = "https://png.pngtree.com/element_origin_min_pic/17/03/05/a867840a9f2d8557c1fbf2297a5b26a0.jpg"
PANTANO = "https://i2.wp.com/cromossomonerd.com.br/wp-content/uploads/2017/02/MP-CN.png"
HM2 = "https://3.bp.blogspot.com/-K-yKC18mGqo/V5E7ldaI3yI/AAAAAAAALOQ/gwt8RnEds5kx7OAfLPOynERFe07DWLWJwCLcB/s1600/marvel%2Bpng%2B%252820%2529.png"
PANTANO2 = "https://poltronanerd.com.br/wp-content/uploads/2017/01/poltrona-monstro-do-pantano.jpg"

def tale():
   pantano = Cena(img = PANTANO)
   pantano2 =Cena(img = PANTANO2)
   casa = Cena(img = CASA)
   barbie = Elemento(img =BARBIE, tit = "barbie", style=dict(left=290, top=220, width=160, higth=100, bottom=100))
   barbie_t = Texto(pantano, "socorro!!!!!!!!!")
   barbie.vai = barbie_t.vai
   barbie.entra(pantano)
   
   
   pantano.direita=casa
   homem_aranha = Elemento(img=HOMEM_ARANHA, tit = " homem-aranha", style=dict(left=290, top=220, width=160, higth=100, bottom=100))
   homem_aranha_t = Texto(casa, "eu escutei gritos de uma donzela em perigo")
   homem_aranha.vai = homem_aranha_t.vai
   homem_aranha.entra(casa)
   casa.direita= pantano
   hm2 =Elemento(img=HM2, tit = "salvador", style=dict(left=290, top=220, width=160, higth=100, bottom=100))
   hm2.entra(pantano2)
   
   pantano.vai()
   
tale()

