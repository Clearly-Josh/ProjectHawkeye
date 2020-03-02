#Lot of code from https://kite.com/python/answers/how-to-convert-binary-string-to-and-from-ascii-text-in-python
#Credit to Obabbamama
#Thanks dad!

k = open("Knowledge.txt","w+")

what_toadd = "The meaning is 42."

byte_array = "abc".encode()


converter(what_toadd, k)
getelfile = open("Knowledge.txt","r+")
l = getelfile.read()

print(l)

def BinaryToDecimal(binary): 
  string = int(binary, 2)
  return string

str_data =' '

for i in range(0, len(l)):
  Possibly_data = l[i:i + 7]
  Notpercentage = BinaryToDecimal(Possibly_data)
  str_data = str_data + chr(Notpercentage)

print ("Secret Message:",str_data)