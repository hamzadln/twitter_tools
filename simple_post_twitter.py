import time
import requests
mydata = { "api" : "API KEY FROM ME",
         "consumer_key" : "CONSUMER KEY FROM TWITTER",
         "consumer_secret" : "CONSUMER SECRET KEY FROM TWITTER",
         "access_token" : "ACCESS TOKEN FROM TWITTER",
         "access_token_secret" : "ACCESS TOKEN SECRET FROM TWITTER"}
status1 = True
while status1 == True:
    print("================================")
    print ("         MENU  :               ")
    print("================================")
    print ("1. Unfollow Not Follback       ")
    print ("2. Unfollow ALL FOLLOWING [HOT]")
    print ("3. Follow Followers Target     ")
    print ("0. EXIT                        ")
    print("================================")
    pil = input("Pilihan Kamu: ")
    n = 0
    i = 1
    if pil == "1":
        r = requests.post("https://tweetermedia.zapto.org/private/notfollback.php", data = mydata)
        if r.status_code == 500:
            print ("ERROR")
        print (r.text)
    elif pil == "2":
         print ("May cause your twitter token expired, broken, and your twitter might be temporary or permanently suspended.")
         pil2 = 0
         status=True
         while status:
             pil2 = input("1. Continue 2. Exit    CHOOSE : ")
             if pil2 == "1":
                 status = False
                 r = requests.post("https://tweetermedia.zapto.org/private/unfollowall.php", data = mydata)
                 print(r.text)
    elif pil== "3": 
        while n != 1:
            r = requests.post("https://tweetermedia.zapto.org/private/fftmantap.php", data = mydata)
            print ("Percobaan ke-", i)
            print(r.text)
            if "TARGET" in r.text:
                isi = True
                while isi:
                    isi1 = input("Mau isi username Target? : 1. Ya 2. Tidak")
                    if isi1 == "1":
                       username = input("Input username target : ")
                       target = {"username" : username , "api": "hamzadln99"}
                       r = requests.post("https://tweetermedia.zapto.org/private/add_target.php", data = target)
                       print(r.text)
                    elif isi1 == "2":
                        isi = False
                    else:
                        print("ISI YANG BENERLAH GOBLOG")
            if "Berhasil" in r.text:
                print("Berhasil")
                time.sleep(30)
            elif "Gagal" in r.text:
                n = 1
                print("Gagal")
            elif "Duplikat" in r.text:
                print("Duplikat")
            i += 1
    elif pil=="exit":
         status1 = False
print ("END. Thank You.")
