# grace.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900


HOEM_ARANHA = "https://2.bp.blogspot.com/-Sx288TzGsV0/V5E7WpC1S2I/AAAAAAAALNE/46iReRzHSMslkQKxOgLr6jb5Pl4LTXEnwCLcB/s1600/B78144.jpg"
CASINHA = "http://www.meriti.rj.gov.br/iptu2018/img/casinha.png"
ALICE = "https://2.bp.blogspot.com/-gbvgbBcZsIg/V2YHCoD6yMI/AAAAAAAAGOk/RevcsxQgQ7YhqyL5j8gDx-zrRq8MriNzACLcB/s320/1b.png"
CASTELO = "https://vignette.wikia.nocookie.net/ouat/images/a/af/Castelo.png/revision/latest?cb=20121027032937&path-prefix=pt-br"
YODA = "https://4.bp.blogspot.com/-lOTaIzHeQus/V1LnhUc4HfI/AAAAAAAAEuU/xobsFnVFnycvEGErN6Fdes_EIbzxlt8HQCLcB/s640/Yodatrur.png"
PANTANO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW2c7m2GcvUpqgc8Yc3fsag7-HvtHpWF0SRx1L0LhInfsBeYMz3g"

def nos():
   casinha = Cena(img = CASINHA)
   casinha.vai()

nos()