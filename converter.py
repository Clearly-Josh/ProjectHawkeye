# String to Binary command originated from https://www.geeksforgeeks.org/python-convert-string-to-binary/
# Vice versa funcions & commands originated from https://www.geeksforgeeks.org/convert-binary-to-string-using-python/

def BinaryToDecimal(binary):      
  binary1 = binary  
  decimal, i, n = 0, 0, 0
  while(binary != 0):  
    dec = binary % 10
    decimal = decimal + dec * pow(2, i)  
    binary = binary //10
    i += 1
  return (decimal)

conv2 = ''

knowledge = 'The_meaning_is_forty_two'

def converter(knowledge, conv2):
  conv_knowledge = ''.join(format(ord(i), 'b') for i in knowledge)
  
  response = input('''Would you like to retrieve the entire database of human knowledge or not?
''')

  if response == "Yes" or response == "yes" or response == "Y" or response == "y":
    for i in range(0, len(conv_knowledge), 7):
      temp = int(conv_knowledge[i:i + 7])
      decimal = BinaryToDecimal(temp)
      conv2 = conv2 + chr(decimal)
    return conv2
  
  elif response == "No" or response == "no" or response == "N" or response == "n":
    print("Knowledge repertoire is saved but not returned.")
    return ''
  
  else:
    print("I'll take that unknown response as a no and, thus, shan't print out the knowledge")
    return ''
#print(converter(knowledge, conv2))