def conversao (x):
  boi = x * 0.39
  file  = open("arquivo.txt","w+")
  file.write("o valor em centímetros {} corresponde a valor em polegadas {:.2f}.".format(x,boi))
  file.seek(0,0)
  print(file.read())
  file.seek(0,0)
  file.close()