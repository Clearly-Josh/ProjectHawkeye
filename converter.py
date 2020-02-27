k = open("Knowledge.txt","w+")

def converter(what_toadd, knowledge_doc):
  new4arg = ''.join(format(ord(i), 'b') for i in what_toadd)
  knowledge_doc.write(new4arg)

what_toadd = "The meaning is 42."

converter(what_toadd, k)
getelfile = open("Knowledge.txt","r+")
l = getelfile.read()

open("Knowledge.txt").seek(0,0)

print(l)
#A lot of code coming up taken from https://www.geeksforgeeks.org/convert-binary-to-string-using-python/
#Purpose is getting from binary back to string

def BinaryToDecimal(binary): 
  string = int(binary, 2)
  return string

str_data =' '

for i in range(0, len(l)):
  Possibly_data = l[i:i + 7]
  Notpercentage = BinaryToDecimal(Possibly_data)
  str_data = str_data + chr(Notpercentage)

print ("Secret Message:",str_data)