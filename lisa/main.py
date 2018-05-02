# grace.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900

FLORESTA = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
NAVE = "https://ugc.kn3.net/i/origin/http://servidordeimagenes1.files.wordpress.com/2013/09/flyingsaucer_zps6e5151b4.png"
MESTRE_YODA = "https://www.allcenter.com.br/wp-content/uploads/2017/03/star-wars-yoda-sixth-scale-hot-toys-silo-902738.png"
CASINHA_AMARELA = "https://cdn.clipte.com/u/boiperc0/14057-1xok/14057-mwaj/g1.jpg"
CINDERELA = "https://vignette.wikia.nocookie.net/disneyprincesas/images/9/9d/Tumblr_o1xpveBV601v56ooio1_500.png/revision/latest?cb=20160710162330&path-prefix=pt-br"
BELA_ADORMECIDA = "https://i.pinimg.com/originals/7d/ed/98/7ded98f455349d5da9bb67bea5282e78.png"

def tale():
    floresta = Cena(img = FLORESTA)
    nave = Elemento(img=NAVE, tit= "nave", style=dict(left=250, top=200, width=300, hight=300, bottom=300))
    nave_t = Texto(floresta, "Desce uma nave na floresta")
    nave_t.vai = nave.vai
    nave.entra(floresta)
    floresta.vai()
    
tale()  