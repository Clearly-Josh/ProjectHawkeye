print("Eight is running..")

rev = ''''''
def converter(rev, arg):
  new4arg = ''.join(format(ord(i), 'b') for i in arg) 
  rev = rev + new4arg
  return rev
whattoadd = input('''What knowledge do you want to add to the repertoire?
''')
print(converter(rev, whattoadd))