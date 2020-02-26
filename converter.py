k = open("Knowledge.txt","w+")

def converter(what_toadd, knowledge_doc):
  new4arg = ''.join(format(ord(i), 'b') for i in what_toadd)
  knowledge_doc.write(new4arg)
  knowledge_doc.write('''
''')

what_toadd = "The meaning is 42."

converter(what_toadd, k)

getelfile = open("Knowledge.txt","r")
l = getelfile.read()
print(l)

#A lot of code coming up taken from https://www.geeksforgeeks.org/convert-binary-to-string-using-python/
#Purpose is getting from binary back to string

def BinaryToDecimal(binary): 
  string = int(binary, 2)
  return string