try:
    word = 'currupt'
    if word != 'corrupt':
         raise ValueError
except ValueError:
     print("Currupt is spelled wrong!")