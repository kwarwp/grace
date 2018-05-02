# grace.anastasia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900

HOMEM_ARANHA = "http://4.bp.blogspot.com/-RJm2iY2ETNc/T9eVS0j1frI/AAAAAAAAFpE/BV5ZIE-UHxA/s1600/Homem-Aranha-png-Queroimagem.com+(7).png"
ALICE = "http://3.bp.blogspot.com/_fJ0FoIoxICw/TUNaZtVvdWI/AAAAAAAAAn8/riQcXQuGZJI/s1600/Alice+01.png"
YODA = "https://2.bp.blogspot.com/-V8V5RPZUD1M/V1LnlY7xeOI/AAAAAAAAEu4/lKAEq2C0z5Y1NUmrGvSdspKHiz6RiM9gACLcB/s1600/Yodauur.png"
FLORESTA = "http://pre04.deviantart.net/7608/th/pre/f/2016/163/6/8/forest_clearing_trees_png_background_stock_0069_by_annamae22-da5zwhu.png"
PANTANO = "http://img15.deviantart.net/cda6/i/2014/346/9/f/pantano_by_tetamonja-d89lzzs.png"
FINAL = "http://innhost.com.br/wp-content/uploads/2014/05/innhost_duvida.png"

def tale():
   pantano = Cena(img=PANTANO)
   pantano.vai()

tale()
   