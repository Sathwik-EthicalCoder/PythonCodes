import json

#writing the data into the file

fil=open("data.json","w")
json.dump({11212:132323,343434343:89709787098},fil)
fil.close()

#reading the data

file=open("data.json","r")
data=json.load(file)
file.close()
print(data)
