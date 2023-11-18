def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Currying
curryin = perkalian(10)(2)
print(curryin)
    
# HoF
Hof = perkalian(10)
print(Hof(2))
