def point(x,y):
    return x,y

def line_equation_of(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    
    def rumusGradien():
        return (y2-y1)/(x2-x1)
    
    def totalAkhir():
         gradien = rumusGradien()
         constanta = y1 - gradien * x1 
         print(f"y = {gradien:.2f}x + {constanta:.2f}")
    
    return totalAkhir

hasil = line_equation_of(point(1,4),point(0,2))
hasil()

def line_equation_of_without(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    M = (y2-y1)/(x2-x1)
    C =  y1 - M * x1 
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of_without(point(1,4),point(0,2)))

