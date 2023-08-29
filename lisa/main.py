   # grace.lisa.main.py
MSG = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb"+
" gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
#SUBIR DUAS LETRAS
MSG = "map"
def pcn():
    print (ord("g"))
    for i in MSG:
        if i.isalpha():
            words = ord (i)+2
            print (chr(words),end="")
    else:
            print (i,end="")

"""#]Como pagamento de um pequeno lote de carneiros,
3 muçulmanos receberam uma partida de vinho,
composta de 21 vasos iguais, sendo 7cheios, 7 meio-cheios e 7 vazios.
Querem, agora, dividir os 21 vasos de modo que cada um deles receba a mesma quantidade de vinho.
"""
class Vaso:
    def __repr__(self):
        return 4
def mul0():
    m = [(i, j, k) for i in range(7) for j in range(7) for k in range(7) if i+j+k == 7]
    s = [(a, b, c) for a in m for b in m for c in m if sum(a) == sum(b) and sum(b) == sum(c)]
    st = [([a0, a1, a2], [b0, b1, b2], [c0, c1, c2]) for [a0, a1, a2], [b0, b1, b2], [c0, c1, c2] in s 
    if  sum([a0, b0, c0])==7 and sum([a1, b1, c1])==7 and sum([a2, b2, c2])==7 and sum([a0, a1, a2, b0, b1, b2, c0, c1, c2])==21
    and 2*b0+c0 == 2*b1+c1 and 2*b1+c1  == 2*b2+c2]

    print (st)

def mul1():
    m = [(i, j, k) for i in range(7) for j in range(7) for k in range(7) if i + j + k == 7]
    s = [(a, b, c) for a in m for b in m for c in m if len(set(sum(m) for m in (a, b, c))) == 1]
    st = [mul for mul in s if all(sum(vasos) == 7 for vasos in zip(*mul)) and
          (len(set([m + 2 * c for v, m, c in mul])) == 1)]

    print(st)
from random import sample
#mul1()
def vas():
    def draw(is_wrong = True):
        while is_wrong:
            mus = sample(vasos,7)
            is_wrong = sum(mus) != 7
        [vasos.remove(v) for v in mus]
        return mus

    vasos = [0]*7 + [1]*7 + [2]*7
    mus1 = draw()
    mus2 = draw()
    print(vasos, mus1, mus2)
#vas()
fox = " ●●●● ● / ● ●● ●● ●● ● / ●●● ●●  ● ● / ●●●  ●●"
ovr = "● ●●  ●● ●●● /  ●●● ● ●●"
dog = " ●●●● ● / ●●● ● ●● ● / ●●  ●"



def converta_em_morse(texto):
    """Converta em código Morse.
        :param texto: O texto a ser codificado
        :return: O texto em código morse
    """
    alpha_morse= "".join(" / ".join([fox,ovr,dog]))
    #print((alpha_morse))
    alpha_morser = []
    [alpha_morser.extend([aml]) for am in alpha_morse.split(" / ") for aml in am.split()]
    #print(list(alpha_morser))
    morse_alpha= "the quick brown fox jumps over the lazy dog"
    morse_alpha = [lt for lt in morse_alpha if not lt.isspace()]
    alpha_morse = {k:v for k, v in zip(morse_alpha, alpha_morser)}
    alpha_morse[" "] = "/"
    #print((alpha_morse))
    texto_em_morse = " ".join([alpha_morse[i] for i in texto])
    #print((texto_em_morse))
    return texto_em_morse


fox = " ●●●● ● / ● ●● ●● ●● ● / ●●● ●●  ● ● / ●●●  ●●"
assert converta_em_morse("the quick brown fox") == fox
ovr = "● ●●  ●● ●●● /  ●●● ● ●●"
assert converta_em_morse("jumps over") == ovr
dog = " ●●●● ● / ●●● ● ●● ● / ●●  ●"
assert converta_em_morse("the lazy dog") == dog
print("Acertou o conversor de morse!")


