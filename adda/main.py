# grace.adda.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900

HOMEM-ARANHA = "https://www.bemcolar.com/media/catalog/product/cache/1/image/1800x/040ec09b1e35df139433887a97daa66f/a/d/xadesivo-de-parede-infantil-homem-aranha.png.pagespeed.ic.s6_hi3U3pZ.png"
ALICE = "https://3.bp.blogspot.com/-9TV8MKrd94M/V2YHE_KbLXI/AAAAAAAAGPA/iQwHwGeAucspu3Pp6UcchZQf3K2ce_g5wCLcB/s320/1e.png"
YODA = "http://pngimg.com/uploads/starwars/starwars_PNG8.png"
CASINHA ="https://cdn.pixabay.com/photo/2016/06/08/21/39/house-1444716_960_720.png"
PANTANO = "http://pt.clubpenguinwiki.info/static/images/cpwpt/thumb/4/4b/Festa_de_Halloween_2011_Labirinto_do_P%C3%A2ntano.png/250px-Festa_de_Halloween_2011_Labirinto_do_P%C3%A2ntano.png"
CASTELO = "https://i.pinimg.com/originals/10/a7/8a/10a78a8d28dcfc1999848a8815e23679.png"

def tale():
   pantano = Cena(img = PANTANO)
   pantano.vai()

tale()