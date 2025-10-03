x = int(input('Input satu angka bulat: '))
 
prima = True
if((x == 0) or (x == 1)):
  prima = False
else:
  for i in range(2,(x//2)):
    if ((x % i) == 0):
       prima = False
       break
 
if(prima):
  print(x,'adalah angka prima')
else:
  print(x,'bukan angka prima')