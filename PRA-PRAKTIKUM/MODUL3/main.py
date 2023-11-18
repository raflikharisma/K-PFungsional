
def contains_digit(word):
    return any(char.isdigit() for char in word)

def data_split(value):
     return list(filter(contains_digit, value.split()))
 
def convert(minggu):
    def d(day):
        def h(hours):   
            def m(minute):
                return (minggu * 10080) + (day * 1440) + (hours * 60) + minute
            return m
        return h
    return d

def is_string(value):
    if isinstance(value, str):
     return value
        
def is_integer(value):
    if isinstance(value, int):
     return value
 
def is_float(value):
    if isinstance(value, float):
     return value
 
def resultFilterStr(value):
     return list(filter(is_string, value))
 
def resultFilterFloat(value):
     return tuple(filter(is_float, value))
 
def resultFilterInteger(value):
     return list(filter(is_integer, value))

def parseResult(value):
    temp = [x for x in value]
    keys = ['ratusan', 'puluhan', 'satuan']
    return dict(map(lambda keys, value: (keys, value), keys, temp))


def main():
    data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]
    
    result = []
    kegiatan2 = []
    
    for element in data:
        data_points = data_split(element)
        kegiatan2.append(data_points)
        if len(data_points) == 4:
            minggu, hari, jam, menit = map(int, data_points)
            result.append(convert(minggu)(hari)(jam)(menit))

    # Kegiatan 1 dan 2
    print(result)
    print(kegiatan2)
    
    # Kegiatan 3
    random_list = [105, 3.1, 737, "python", 2.7, "world", 412, 5.5, "Al"]
    tempInteger = resultFilterInteger(random_list)
    print(parseResult(str(tempInteger[0])))
    print(parseResult(str(tempInteger[1])))
    print(parseResult(str(tempInteger[2])))
    print(resultFilterStr(random_list))
    print(resultFilterFloat(random_list))



    
  

if __name__ == "__main__":
    main()

