
dataList = []
dataTuple = ()
dataDict = {}


random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "world", 412, 5.5, "AI"]
i = 0
for data in random_list:
    if isinstance(data, float):
        dataTuple += (data,)
    elif isinstance(data, str):
        dataList.append(data)
    elif isinstance(data,int):
        dataDict["key {}".format(i)] = data
        i += 1
        
print("ini adalah data dict", dataDict)
print("ini adalah data list", dataList)
print("ini adalah data tuple", dataTuple)
        
        