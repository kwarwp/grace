# grace.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900

FLORESTA = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
NAVE = "http://4.bp.blogspot.com/_DRY6NerN11s/TOkTDeFZTNI/AAAAAAAAATs/YqBrhd6BZXs/s1600/nave.png"
MESTRE_YODA = "https://www.allcenter.com.br/wp-content/uploads/2017/03/star-wars-yoda-sixth-scale-hot-toys-silo-902738.png"
CASINHA_AMARELA = "https://cdn.clipte.com/u/boiperc0/14057-1xok/14057-mwaj/g1.jpg"
CINDERELA = "https://vignette.wikia.nocookie.net/disneyprincesas/images/9/9d/Tumblr_o1xpveBV601v56ooio1_500.png/revision/latest?cb=20160710162330&path-prefix=pt-br"
BELA_ADORMECIDA = "https://i.pinimg.com/originals/7d/ed/98/7ded98f455349d5da9bb67bea5282e78.png"

def tale():
    floresta = Cena(img = FLORESTA)
    nave = Elemento(img=NAVE, tit= "nave", style=dict(right=100, top=100, width=100, hight=100, bottom=100))
    
    floresta.vai()
    
tale()  