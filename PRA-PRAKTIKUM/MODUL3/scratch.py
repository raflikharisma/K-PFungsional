from functools import reduce
def check (input):
    if input < 1:
        return print ("inputan tidak valid")
    elif input % 2 == 0:
        return  print("inputan genap")
    elif input % 2 == 1:
        return print("inputan ganjil")
    
def pangkat(data):
    return [x ** 2  for x in data]

def pangkatMap(data):
    return list(map(lambda x: x ** 2, data))

def pangkatReduce(data):
    return reduce(lambda x,y: x * y, data) 



kali = lambda x,y:  x * y

def sortt(data):
    return data[::-1]

def paksaTurun(data):
    return data.lower()


def bilanganpostif(data):
    return data >= 0

def main():
    inputan = int(input("Masukkan Inputan Anda : "))
    check(inputan)
    
    my_list = [1,2,3,4,5]
    print(sum(my_list))
    print(pangkat(my_list))
    print(pangkatMap(my_list))
    print(pangkatReduce(my_list))
    print(kali(2,3))
    print(sortt(my_list))
    
    aw = [x for x in range(1,11) if x % 2 == 1]
    print(aw)
    
    listme = [-1,-34,45.6,-76.8,-31.3]
    aww = reduce(lambda x,y: x + y, listme)
    print(aww)
    
    awww = map(paksaTurun, "RaFli KHaRismA")
    awwww = list(filter(bilanganpostif, listme))
    print(awwww)
    
if __name__ == "__main__":
    main()

    