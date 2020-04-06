import os

A = []
B = []
J= []
K= []



menu = ['1.Penjumlahan','2. Pengurangan','3. Exit']


print ("=======Selamat Datang di Operasi Matriks 2x2====")

print ("MASUKKAN MATRIKS A")
print(" ")

for baris in range (0,2,1) :
  for kolom in range (0,1,1) :
    
    print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+1)
    test = int (input("Masukkan :"))

    print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+2)
    test1 = int (input("Masukkan :"))

    A.append([test,test1])

os.system("clear")
print ("MASUKKAN MATRIKS B")

for baris in range (0,2,1) :
  for kolom in range (0,1,1) :
    print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+1)
    test = int (input("Masukkan :"))

    print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+2)
    test1 = int (input("Masukkan :"))
    B.append([test,test1])

def printmatriks() :
#printmatriks#
  print ("Matriks A :")
  for baris in range (0,2,1) :
    print (A[baris][0], '\t', A[baris][1])
        
  print ("Matriks B :")
  for baris in range (0,2,1) :
    print (B[baris][0], '\t', B[baris][1])

os.system("clear")
printmatriks()




while True :
  print ("")
  print ('=======MENU=======')
  print ('\t'.join(menu))

  pilihmenu = int (input("pilih :"))
  os.system("clear")


  if pilihmenu == 1 :
    print ('====Penjumlahan====')
    print("")
    printmatriks()

#jumlah
    for x in range (0,2,1):
     for y in range (0,1,1) :
      for z in range (1,0,-1) :
        #print (x,y,x,z)
        hasil1 = A[x][y] + B[x][y]
        hasil2= A[x][z] + B[x][z]
        J.append([hasil1,hasil2])

    print("")
    print("Hasil Penjumlahan :")
    for baris in range (0,2,1) :
      print (J[baris][0], '\t', J[baris][1])



  elif pilihmenu == 2:
    print ("===PENGURANGAN===")
    print('')
    printmatriks()

    for x in range (0,2,1):
     for y in range (0,1,1) :
      for z in range (1,0,-1) :
        #print (x,y,x,z)
        hasil1 = A[x][y] - B[x][y]
        hasil2= A[x][z] - B[x][z]
        K.append([hasil1,hasil2])


    print("")
    print("Hasil Pengurangan")
    for baris in range (0,2,1) :
      print (K[baris][0], '\t', K[baris][1])  
    

  elif pilihmenu== 3 :
    break


  