# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GENAP
def point(x,y):
    return x,y

def line_equation_of(p1, gradien):
    x1,y1 = p1
    def rumusConstanta():
        return y1 - gradien * x1
    constanta =  rumusConstanta()
    
    return f"y = {gradien:.2f}x + {constanta:.2f}"



def line_equation_with_closure(p1, gradien):
    x1,y1 = p1
    def rumusPersamaan():
        constanta = y1 - gradien * x1
        print(f"y = {gradien:.2f}x + {constanta:.2f}")
    return rumusPersamaan
        


# tanpa closure

print("Persamaan garis yang melalui titik (4,0) dan bergradien 2:")
# print(line_equation_of(point(4,0),2))
print(line_equation_of(point(4,0),2))
print("Dengan Closure : ")
closure = line_equation_with_closure(point(4,0),2)
closure()
del line_equation_with_closure
# print( line_equation_with_closure(point(4,0),2))
closure()







