#### TRY - EXCEPT - ELSE - FINALLY

while True:
    try:
        myInt = int(input("Numaranizi giriniz :"))
    except: #--> Hata olursa calisir.
        print("Lutfen gercekten numara giriniz")
        continue
    else: # -->try dogru bir sekilde calistigi  zaman aktif olur
        print("Thanks")
        break
    finally: #--> Her zaman cagirilir.
        print("Finally Cagirildi.")