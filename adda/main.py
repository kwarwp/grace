# grace.adda.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900

HOMEM_ARANHA = "https://http2.mlstatic.com/adesivo-decorativo-recortado-infantil-parede-homem-aranha-D_NQ_NP_14090-MLB4095351091_042013-F.jpg"
ALICE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV0qG3TevJ2fNO4KblVuGlqxf1cH3kH-54QMEZ1QHwjmPLbNgy"
YODA = "http://obviousmag.org/renato_collyer/yoda2.jpg"
FLORESTA = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
PANTANO = "https://abrilmundoestranho.files.wordpress.com/2017/09/pantano-facebook.jpg?quality=70&strip=info"
FINAL = "https://img.elo7.com.br/product/main/1790FA1/vela-ponto-de-interrogacao-vela-cerveja.jpg"

def tale():
    floresta = Cena(img=FLORESTA)
    homem_aranha = Elemento (img=HOMEM_ARANHA, tit="Homem_Aranha", style=dict(left=400, top=300, width=100, higth=100, bottom=100))
    homem_aranha_text = Texto(floresta, "Sensor de Aranha")
    homem_aranha.vai = homem_aranha_text.vai 
    homem_aranha.entra(floresta)
    
    pantano = Cena (img=PANTANO)
    floresta.direita=pantano
    alice = Elemento(img=ALICE, tit="Cachinhos_dourados", style=dict(left=400, top=300, width=100, higth=100, bottom=100))
    alice_text = Texto(pantano, "oh! e agora, quem poderá me defender?")
    alice.vai = alice_text.vai
    alice.entra(pantano)
    
    yoda = Elemento(img=YODA, tit="Mestre dos Mestres", style=dict(left=400, top=300, width=100, higth=100, bottom=100))
    yoda_text = Texto(pantano, "Homem aranha e alice procurem o lado negro da força!!")
    yoda.vai = yoda_text.vai
    yoda.entra(pantano)
        
    floresta.vai()
    
tale()