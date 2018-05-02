# grace.stacy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900


BARBIE = "https://i.pinimg.com/originals/d1/e5/89/d1e589ccc516cbec88da10415a77c947.png"
HOMEM_ARANHA = "https://2.bp.blogspot.com/-Sx288TzGsV0/V5E7WpC1S2I/AAAAAAAALNE/46iReRzHSMslkQKxOgLr6jb5Pl4LTXEnwCLcB/s1600/B78144.jpg"
CASA = "https://png.pngtree.com/element_origin_min_pic/17/03/05/a867840a9f2d8557c1fbf2297a5b26a0.jpg"
PANTANO = "https://i2.wp.com/cromossomonerd.com.br/wp-content/uploads/2017/02/MP-CN.png"

def tale():
   pantano = Cena(img = PANTANO)
   barbie = Elemento(img =BARBIE, tit = "barbie", style=dict(left=290, top=220, width=160, higth=100, bottom=100))
   
   barbie.entra(pantano)
   pantano.vai()
   
tale()

