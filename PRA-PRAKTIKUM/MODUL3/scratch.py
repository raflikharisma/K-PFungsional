# filtered_data = [
    # ' '.join(list(filter(contains_digit, element.split())))
    # for element in data
    # ]   
    
    # data1 = data_split(filtered_data[0])
    # minggu1 = int(data1[0])
    # hari1 = int(data1[1])
    # jam1 = int(data1[2])
    # menit1 = int(data1[3])
    
    # data2 = data_split(filtered_data[1])
    # minggu2 = int(data2[0])
    # hari2 = int(data2[1])
    # jam2 = int(data2[2])
    # menit2 = int(data2[3])
    
    # data3 = data_split(filtered_data[2])
    # minggu3 = int(data3[0])
    # hari3 = int(data3[1])
    # jam3 = int(data3[2])
    # menit3 = int(data3[3])
    
    
    
    
    # data1 = convert(minggu1)(hari1)(jam1)(menit1)
    # data2 = convert(minggu2)(hari2)(jam2)(menit2)
    # data3 = convert(minggu3)(hari3)(jam3)(menit3)
    
    # tempList = [data1, data2, data3]
    
    # print(tempList)
    
    # def sumByGenre(data):
    # drama = len(list(filter(lambda x: x["genre"] == "Drama", data)))
    # action = len(list(filter(lambda x: x["genre"] == "Action", data)))
    # comedy = len(list(filter(lambda x: x["genre"] == "Comedy", data)))
    # horor = len(list(filter(lambda x: x["genre"] == "Horror", data)))
    # scifi = len(list(filter(lambda x: x["genre"] == "Sci-Fi", data)))
    # return {"Action": action,"Drama": drama ,"Horor": horor, "Comedy": comedy, "Sci-Fi": scifi}
    
    # def counting(filtered):
    #     tempList = {}
    #     for year in filtered:
    #         yearMovies = list(filter(lambda x: x["year"] == year, data))
    #         sumMovies = sum(movie["rating"] for movie in data if movie["year"] == year)
    #         tempList[year] = sumMovies/len(yearMovies)
    #     return tempList
        
    # return counting(temp)
        