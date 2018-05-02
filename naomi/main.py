# grace.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900


HOMEM_ARANHA = "https://2.bp.blogspot.com/-Sx288TzGsV0/V5E7WpC1S2I/AAAAAAAALNE/46iReRzHSMslkQKxOgLr6jb5Pl4LTXEnwCLcB/s1600/B78144.jpg"
CASINHA = "http://www.meriti.rj.gov.br/iptu2018/img/casinha.png"
ALICE = "https://2.bp.blogspot.com/-gbvgbBcZsIg/V2YHCoD6yMI/AAAAAAAAGOk/RevcsxQgQ7YhqyL5j8gDx-zrRq8MriNzACLcB/s320/1b.png"
CASTELO = "https://vignette.wikia.nocookie.net/ouat/images/a/af/Castelo.png/revision/latest?cb=20121027032937&path-prefix=pt-br"
YODA = "https://4.bp.blogspot.com/-lOTaIzHeQus/V1LnhUc4HfI/AAAAAAAAEuU/xobsFnVFnycvEGErN6Fdes_EIbzxlt8HQCLcB/s640/Yodatrur.png"
PANTANO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW2c7m2GcvUpqgc8Yc3fsag7-HvtHpWF0SRx1L0LhInfsBeYMz3g"

def nos():
   casinha = Cena(img = CASINHA)
   pantano = Cena(img = PANTANO)   
   castelo = Cena(img = CASTELO)
   
   homem_aranha = Elemento(img =HOMEM_ARANHA, tit= "homem_aranha", style=dict(left=190, top=100, width=160, higth=100))
   homem_aranha1 = Elemento(img =HOMEM_ARANHA, tit= "homem_aranha", style=dict(left=190, top=100, width=160, higth=100))
   alice = Elemento(img= ALICE, tit= "alice", style=dict(left=340, top=180, width=80, higth=300))
   alice1 = Elemento(img= ALICE, tit= "alice1", style=dict(left=340, top=180, width=80, higth=300))
   alice2 = Elemento(img= ALICE, tit= "alice2", style=dict(left=340, top=180, width=80, higth=300))
   yoda = Elemento(img= YODA, tit= "yoda", style=dict(left=290, top=180, width=80, higth=100))
   
   
   homem_aranha_t = Texto(casinha, "tem alguém aí???")
   homem_aranha.vai = homem_aranha_t.vai
   homem_aranha1_t = Texto(castelo, "Entregue!")
   homem_aranha1.vai = homem_aranha1_t.vai
   alice_t = Texto(casinha, "Estou perdida! Por favor, leve-me para o Castelo!")
   alice.vai = alice_t.vai
   alice1_t = Texto(pantano, "Socorro, Homem-Aranha!!!")
   alice1.vai = alice1_t.vai
   alice2_t = Texto(castelo, "Muito obrigada!!!")
   alice2.vai = alice2_t.vai
   yoda_t = Texto(pantano, "Alice, você ficará presa neste pantano!")
   yoda.vai = yoda_t.vai
   
   casinha.direita = pantano
   homem_aranha.entra(casinha)
   homem_aranha1.entra(castelo)
   homem_aranha_t.vai = homem_aranha.vai
   alice.entra(casinha)
   alice.vai = alice_t.vai
   alice1.entra(pantano)
   alice2.entra(castelo)
   yoda.entra(pantano)
   pantano.direita= castelo
   
   
   
   
   casinha.vai()
   
   
nos()