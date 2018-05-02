# grace.adda.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["WIDTH"]= 900

#homem_aranha = "https://http2.mlstatic.com/adesivo-decorativo-recortado-infantil-parede-homem-aranha-D_NQ_NP_14090-MLB4095351091_042013-F.jpg"
#alice = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.khinsider.com%2FKingdom%2520Hearts%2520coded%2FRenders%2FWL01%2520-%2520Alice.png&imgrefurl=https%3A%2F%2Fwww.khinsider.com%2Fcharacters%2Falice3&docid=0Fc-gw7tTmWvXM&tbnid=WG_eft2WWhUAkM%3A&vet=10ahUKEwjA8KLKzOfaAhUEq1kKHaoRCEkQMwg7KAgwCA..i&w=2286&h=3780&client=firefox-b-ab&bih=786&biw=1440&q=alice&ved=0ahUKEwjA8KLKzOfaAhUEq1kKHaoRCEkQMwg7KAgwCA&iact=mrc&uact=8"
#yoda = "https://www.google.com/imgres?imgurl=http%3A%2F%2Fobviousmag.org%2Frenato_collyer%2Fyoda2.jpg&imgrefurl=http%3A%2F%2Fobviousmag.org%2Frenato_collyer%2F2015%2F06%2Fa-filosofia-do-mestre-yoda-em-8-frases.html&docid=jBOExU_s6E-udM&tbnid=MKQIwZPB1mR8wM%3A&vet=10ahUKEwj4orvhzOfaAhVls1kKHQy_ACkQMwi3ASgCMAI..i&w=898&h=635&client=firefox-b-ab&bih=786&biw=1440&q=mestre%20yoda&ved=0ahUKEwj4orvhzOfaAhVls1kKHQy_ACkQMwi3ASgCMAI&iact=mrc&uact=8"
FLORESTA = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
#pantano = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fabrilmundoestranho.files.wordpress.com%2F2017%2F09%2Fpantano-facebook.jpg%3Fquality%3D70%26strip%3Dinfo&imgrefurl=https%3A%2F%2Fmundoestranho.abril.com.br%2Fambiente%2Fcomo-se-forma-um-pantano-que-bichos-vivem-la%2F&docid=cVcuvrpVvCtYlM&tbnid=Obia1qL4wnHC5M%3A&vet=10ahUKEwjw_6z0zOfaAhVCwFkKHap9CwUQMwhnKAEwAQ..i&w=1200&h=627&client=firefox-b-ab&bih=786&biw=1440&q=pantano&ved=0ahUKEwjw_6z0zOfaAhVCwFkKHap9CwUQMwhnKAEwAQ&iact=mrc&uact=8"
#final = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjygOTKzefaAhUCw1kKHVwpDV4QjRx6BAgBEAU&url=https%3A%2F%2Fwww.elo7.com.br%2Fvela-interrogacao%2Fdp%2F95939D&psig=AOvVaw1N5uxszJhD-qtbyEdjQ0xU&ust=1525370361833842"

def tale():
    floresta = Cena(img=FLORESTA)
    floresta.vai()
    
tale()