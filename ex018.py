from math import radians, sin, cos, tan
a = int(input('Digite um ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O ângulo de {} tem o SEN de {:.2f}'.format(a, sen))
print('O ângulo de {} tem o COS de {:.2f}'.format(a, cos))
print('O ângulo de {} tem a TAN de {:.2f}'.format(a, tan))






