   # grace.lisa.main.py
MSG = ("Que j'aime à faire connaire un nombre utile aux sages Glorieux Archimède artiste ingeneux")
#SUBIR DUAS LETRAS
MSG = "map"
print (ord("g"))
for i in MSG:
   if i.isalpha():
      words = ord (i)+2
      print (chr(words),end="")
   else:
      print (i,end="")