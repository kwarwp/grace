from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE

STYLE = ["width"] = 900

GROOT ="https://banner.kisspng.com/20180417/oze/kisspng-baby-groot-ego-the-living-planet-rocket-raccoon-ga-guardians-of-the-galaxy-5ad6bd2a3810e6.0826339215240225702297.jpg"
MASMORRA = "https://i0.wp.com/www.fatosdesconhecidos.com.br/wp-content/uploads/2018/03/8a249fb00ad32fc700ba706c605ed6b6-1.jpg"
KEYS = "https://png.pngtree.com/element_pic/17/02/09/0447473297b79499f564fce3bdddb294.jpg"
EXIT = "http://2.bp.blogspot.com/-Itonglqj9vM/UfrjCGm3dBI/AAAAAAAAACw/943Vy6ccUDU/s1600/exilio.jpg"
ESTRADA = "https://sobreluzesepaisagens.files.wordpress.com/2011/09/josef-koldelka-exils-37.jpg"

def exilio():
   masmorra = Cena(img=MASMORRA)
   exit= Cena(img=EXIT)
   estrada=Cena(img=ESTRADA)
   groot = Elemento(img = GROOT, tit='Im GROOOOOOT', style = dict(left=90,top=100, widht=30, hight=50,bottom=50))
   keys = Elemento(img= KEYS, tit="Pra que serve uma chave mesmo?", style = dict(left=90, top=100, widht=100, hight=100,bottom=100))
   
   
  
   masmorra.direita = exit
   groot.entra(masmorra)
   #keys.entra(masmorra)
   exit.meio = estrada
   
   #groot.entra(estrada)
    
   masmorra.vai()
    
exilio()
    