# grace.kathryn.main.py
"""#]Como pagamento de um pequeno lote de carneiros,
3 muçulmanos receberam uma partida de vinho,
composta de 21 vasos iguais, sendo 7cheios, 7 meio-cheios e 7 vazios.
Querem, agora, dividir os 21 vasos de modo que cada um deles receba a mesma quantidade de vinho.
os mercadores tem que receber a mesma quantidade de vasos
os vasos estão selados e não podem ser abertos"""

def vasos_vinhos():
    vazios = 7 
    meio_cheio = 7 
    cheios = 7 
    #muculmano1 = 0 
    #muculmano2 = 0 
    #muculmano3 = 0 
    #muculmano = [vazio, meio_cheio, cheios] # vinho 
    
    muculmano_3vinhos = []
    
    for vazios in range(0,7):          #vazios de 0 a 7 
        for meio_cheio in range(0,7): #meio cheio de 0 a 7 
            for cheios in range(0,7): #cheios de 0 a 7 
                if cheios + meio_ceio + vazios == 7:
                    muculmano = [vazios, meio_cheio, cheios]
                    muculmano_3vinhos.append(muculmano)
                    
    print (muculmano_3vinhos)
            
    
    
    #return (muculmano1, muculmano2, muculmano3) #vasos 
    #assert vasos_vinhos
vasos_vinhos()