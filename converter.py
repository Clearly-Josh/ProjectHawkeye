def function(whattoadd):
  rev = ''''''
  def converter(rev, arg):
    new4arg = ''.join(format(ord(i), 'b') for i in arg) 
    rev = rev + new4arg
    return rev
  print(converter(rev, whattoadd))
