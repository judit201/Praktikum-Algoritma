hitung = 0
jawab = "iya"


while(jawab == "iya" or jawab == "lanjut"):
    inputbulan = int(input("Masukkan bulan (1-12): "))
    inputtahun = int(input("Masukkan tahun : "))
    jawab = str(input("Ingin lanjut atau tidak: "))
    

     
    def hitung_bulan():
    
      if(inputbulan >= 13 or inputbulan <= 0):
          print("Bulan tidak terdaftar di dalam kalender")
          
      elif(inputbulan == 1 or inputbulan == 3 or inputbulan == 5 or inputbulan == 7 or inputbulan == 8 or inputbulan == 10 or inputbulan == 12):
    	     print("31 hari dalam sebulan")
          
      
           
      elif (inputbulan == 2):
      
        if(inputtahun % 4 == 0 and inputbulan == 2):
          print("29 hari dalam sebulan")
          return
        
        else :
            print("28 hari dalam sebulan ")
            
      else:
          print("30 hari dalam sebulan")
        
          
    hitung_bulan()
