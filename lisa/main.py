# grace.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900

FLORESTA = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
NAVE = "https://ugc.kn3.net/i/origin/http://servidordeimagenes1.files.wordpress.com/2013/09/flyingsaucer_zps6e5151b4.png"
MESTRE_YODA = "https://www.allcenter.com.br/wp-content/uploads/2017/03/star-wars-yoda-sixth-scale-hot-toys-silo-902738.png"
CASA_AMARELA = "https://cdn.clipte.com/u/boiperc0/14057-1xok/14057-mwaj/g1.jpg"
CINDERELA = "https://vignette.wikia.nocookie.net/disneyprincesas/images/9/9d/Tumblr_o1xpveBV601v56ooio1_500.png/revision/latest?cb=20160710162330&path-prefix=pt-br"
BELA_ADORMECIDA = "http://3.bp.blogspot.com/-e4HhX75lSnQ/UCxBDhEOA2I/AAAAAAAAVWI/AEga-sVj7ic/s1600/pngbrave03.png"

def tale():
    floresta = Cena(img = FLORESTA)
    nave = Elemento(img=NAVE, tit= "nave", style=dict(left=250, top=150, width=300, hight=300, bottom=300))
    mestre_yoda = Elemento(img=MESTRE_YODA, tit= "mestre_yoda", style=dict(left=340, top=350, width=100, hight=100, bottom=100))
    nave_t = Texto(floresta, "Desce uma nave na floresta.")
    nave.vai = nave_t.vai
    mestre_yoda.entra(floresta)
    nave.entra(floresta)
    
    
    casa_amarela = Cena(img=CASA_AMARELA)
    floresta.direita=casa_amarela
    mestre_yoda = Elemento(img=MESTRE_YODA, tit= "mestre_yoda", style=dict(left=340, top=450, width=100, hight=100, bottom=100))
    mestre_yoda.entra(casa_amarela)
    mestre_yoda_t = Texto(casa_amarela, "Mestre Yoda avista uma casa amarela.")
    mestre_yoda.vai = mestre_yoda_t.vai
    casa_amarela.vai()
    
    cinderela = Elemento(img=CINDERELA, tit= "cinderela", style=dict(left=600, top=300, width=100, hight=100, bottom=100))
    cinderela.entra(casa_amarela)
    cinderela.vai
    cinderela_t = Texto(casa_amarela, "Cinderela se assusta com o Mestre Yoda!")
    cinderela.vai = cinderela_t.vai
    
    
    casa2 = Cena(img=CASA_AMARELA)
    casa_amarela.direita=casa2
    mestre_yoda = Elemento(img=MESTRE_YODA, tit= "mestre_yoda", style=dict(left=340, top=450, width=100, hight=100, bottom=100))
    mestre_yoda.entra(casa2)
    mestre_yoda_t = Texto(casa2, "Mestre Yoda avista uma casa amarela.")
    mestre_yoda.vai = mestre_yoda_t.vai
    casa2.vai()
    
    
    cinderela = Elemento(img=CINDERELA, tit= "cinderela", style=dict(left=600, top=300, width=100, hight=100, bottom=100))
    cinderela.entra(casa2)
    cinderela.vai
    bela = Elemento(img=BELA_ADORMECIDA, tit= "bela", style=dict(left=420, top=330, width=100, hight=100, bottom=100))
    bela.entra(casa2)
    bela_t = Texto(casa2, "Valente aparece sorateiramente para salvar Cinderela.")
    bela.vai = bela_t.vai
    
    
    floresta.vai()
    
tale()  