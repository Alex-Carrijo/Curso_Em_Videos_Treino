import math
x = float(input('digite o angulo:'))
x = math.radians(x)
cos = math.cos(x)
sen = math.sin(x)
tag = math.tan(x)
print("o seno vale:{:.2f}  o coseno:{:.2f}, e a tangente:{:.2f}".format(sen, cos, tag))
