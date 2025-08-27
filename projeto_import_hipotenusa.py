

import math
cat1 = float(input('Digite a metragem do cateto adjacente: '))
cat2 = float(input('Digite a metragem do cateto oposto: '))
hip = math.hypot(cat1, cat2)
print('Dado os catetos {} e {} a sua hipotenusa é {}'.format(cat1, cat2, hip))