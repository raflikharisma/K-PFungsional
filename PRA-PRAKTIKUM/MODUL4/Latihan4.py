import math

def translation(tx, ty):
    def inner(p1):
        a,b = p1
        print((tx + a, ty + b))
    return inner

def dilatasi(sx, sy):
    return lambda a,b: (sx * a, sy * b)

def rotasi(derajat):
    radian = math.radians(derajat)
    return lambda x, y: (x * math.cos(radian) - y * math.sin(radian), x * math.sin(radian) + y * math.cos(radian))

def titikPusat():
    return (3,5)

result = translation(2,-1)
resultDilatasi = dilatasi(2,-1)(*titikPusat())
resultRotasi = rotasi(30)(*titikPusat())

result(titikPusat())

print(resultDilatasi)
print(resultRotasi)
