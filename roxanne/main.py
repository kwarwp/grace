from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900

CASTELO = "https://1.bp.blogspot.com/-TF5IKOFRG8I/VXwrZjVbx6I/AAAAAAAAK3A/rU7ZlMlCF8Y/s1600/PF-Potterish_04309.jpg"
#GROOT ="https://www.sideshowtoy.com/wp-content/uploads/2017/04/marvel-guardians-of-the-galaxy-groot-life-size-figure-hot-toys-silo-903025.png225702297.jpg"
MASMORRA = "https://i0.wp.com/www.fatosdesconhecidos.com.br/wp-content/uploads/2018/03/8a249fb00ad32fc700ba706c605ed6b6-1.jpg"
KEYS = "https://vignette.wikia.nocookie.net/disneyprincesas/images/c/c3/Aladdin.png/revision/latest?cb=20140726185701&path-prefix=pt-br"
EXIT = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtldd07IZLptjIFajrfOBN1YKcv--QOtZwQ13MUO5RvKZluWNd"
#ESTRADA = "https://sobreluzesepaisagens.files.wordpress.com/2011/09/josef-koldelka-exils-37.jpg"
ESTRADA = "https://oespirita.files.wordpress.com/2013/03/eueavida.jpg?w=240&h=180"

def exilio():
   castelo = Cena(img=CASTELO)
   masmorra = Cena(img=MASMORRA)
   exit= Cena(img=EXIT)
   estrada=Cena(img=ESTRADA)
   #groot = Elemento(img = GROOT, tit='Im GROOOOOOT', style = dict(left=90,top=100, widht=30, hight=50,bottom=50))
   keys = Elemento(img= KEYS, tit="Maior prisioneiro de todos ", style = dict(left=90, top=100, widht=100, hight=100,bottom=100))
   aladt = Texto(masmorra, "Há!! E eles achando que podem me manter aqui por muito tempo!")
   
   aladt.vai = keys.vai
   castelo.meio = masmorra  
   masmorra.direita = exit
   keys.entra(masmorra)
   
   exit.meio = estrada
   
    
   castelo.vai()
    
exilio()
    