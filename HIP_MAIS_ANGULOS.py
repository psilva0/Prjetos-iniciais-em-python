import time
import math
print('Para fazer toda a análise de um triângulo, siga as informações a seguir.')
cata = float(input('Digite a metragem do cateto adjacente: '))
cato = float(input('Digite a metragem do cateto oposto: '))
ang = float(input('Digite um ângulo alfa para saber seu cosseno, seno e tangente.'))
hip = math.hypot(cata, cato)
cos = math.cos(math.radians(ang))
sin = math.sin(math.radians(ang))
tg = math.tan(math.radians(ang))

print('Dado os catetos {} e {}, sua hipotenusa é {}'.format(cata,cato,hip))
print('Dado o ângulo de {} graus, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(ang,sin,cos, math.ceil(tg)))

