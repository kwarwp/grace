# grace.natalia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE['width']= 450

urlAlice = "https://images-na.ssl-images-amazon.com/images/I/81J63h8ddfL._SL1500_.jpg"
urlCastelo = "https://img.elo7.com.br/product/zoom/1504DB8/painel-sublimado-tecido-0x3-0-castelo-sublimacao.jpg"
urlBarraco = "http://www.casadamaepobre.org/wp/wp-content/uploads/2013/10/barraco.jpg"
urlsininho = "https://i.pinimg.com/originals/60/69/c3/6069c395a8a96c7c7260b833195b4c39.png"


def historia():
	castelo = Cena(img = urlCastelo)
	alice = Elemento(img = urlAlice, tit = "menina bandida", style = dict (top = 200,left = 200, width = 100 ) )
	
	alice.entra(castelo)
	texto = Texto(castelo, 'Olá, vamos para o baile hoje!')
	alice.vai = texto.vai
	Barraco = Cena(img = urlBarraco)
	sininho = Elemento(img = urlsininho, tit = "Fada magica", style = dict (top = 200, left = 300, width = 300))
	castelo.direita = Barraco
	castelo.vai()
historia()


      
