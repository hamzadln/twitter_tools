import time
import requests , os
import pyfiglet

api = "PUT YOUR API HERE"
dm_status = "ON" 
mydata = { "api" : api,
          "dm_status" : dm_status, 
         "consumer_key" : "FILL YOUR CONSUMER KEY HERE ",
         "consumer_secret" : "FILL YOUR CONSUMER SECRET HERE ",
         "access_token" : "FILL YOUR ACCESS TOKEN HERE ",
         "access_token_secret" : "FILL YOUR ACCESS TOKEN SECRET "}


status1 = True
def banner():
        os.system('clear')
        ascii_banner = pyfiglet.figlet_format("Tweeter Media")
        print(ascii_banner)
        

while status1 == True:
    banner()
    print("==============================================")
    print ("COMMAND ||              MENU  :              |")
    print("==============================================")
    print (" 'UNF'  ||   1. Unfollow Not Follback        |")
    print (" 'UAF'  ||   2. Unfollow ALL FOLLOWING [HOT] |")
    print (" 'FFT'  ||   3. Follow Followers Target      |")
    print (" 'TGT'  ||   4. ADD TARGET                   |")
    print (" 'DM'   ||   5. ADD CAPTION DM               |")
    print (" 'exit'                                      |")
    print("==============================================|")
    pil = input("Pilihan Kamu (UNF / UAF / FFT / exit) : ")
    n = 0
    i = 1
    if pil == "UNF":
        r = requests.post("https://tweetermedia.zapto.org/private/notfollback.php", data = mydata)
        if r.status_code == 500:
            print ("ERROR 500")
        print (r.status_code)
        input("Press Anything..")
    elif pil == "UAF":
         print ("May cause your twitter token expired, broken, and your twitter might be temporary or permanently suspended.")
         pil2 = 0
         status=True
         while status:
             pil2 = input("1. Continue 2. Exit    CHOOSE : ")
             if pil2 == "1":
                 status = False
                 r = requests.post("https://tweetermedia.zapto.org/private/unfollowall.php", data = mydata)
                 print(r.text)
    elif pil== "FFT": 
        while n != 1:
            r = requests.post("https://tweetermedia.zapto.org/private/fftmantap.php", data = mydata)
            print ("Percobaan ke-", i)
            print(r.text)
            if "TARGET" in r.text:
                print("isi target dulu")
            if "Berhasil" in r.text:
                print("Berhasil")
                if i==1:
                    time.sleep(45)
                elif i>1:
                    time.sleep(40)
            elif "Gagal" in r.text:
                time.sleep(0)
                print("Gagal TOKEN ERROR")
                n = 2
            elif "Duplikat" in r.text:
                print("Duplikat")
            i += 1
    elif pil=="TGT":
        isi = True
        while isi:
              isi1 = input("Mau isi username Target? Ya / Tidak : ")
              if isi1 == "Ya":
                 username = input("Input username target : ")
                 target = {"username" : username , "api": api}
                 r = requests.post("https://tweetermedia.zapto.org/private/add_target.php", data = target)
                 print(r.text)
              elif isi1 == "Tidak":
                    isi = False
              else:
                 print("ISI YANG BENERLAH GOBLOG")
    elif pil=="DM":
        isi = True
        while isi:
              isi1 = input("Mau isi caption DM mu? Ya / Tidak : ")
              if isi1 == "Ya":
                 username = input("Input Captionmu (ex: follback ya babiikk) : ")
                 target = {"username" : username , "api": api}
                 r = requests.post("https://tweetermedia.zapto.org/private/add_caption.php", data = target)
                 print(r.text)
              elif isi1 == "Tidak":
                    isi = False
              else:
                 print("ISI YANG BENERLAH GOBLOG")
    elif pil=="exit":
         status1 = False
print ("END. Thank You.")
