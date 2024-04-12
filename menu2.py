import time
from datetime import datetime
import json
import os

def login(user_name):
    user_file_path = r"E:\metakod\menu\user_name.txt" 
    
    
    if not os.path.exists(user_file_path):
        print(f"{user_file_path} dosyası bulunamadı.")
        return

    with open(user_file_path, "r") as kullanicilar:
        kullanici_adlari = [line.strip() for line in kullanicilar]

    if user_name in kullanici_adlari:
        json_file_path = os.path.join(r"E:\metakod\menu", user_name + '.json')
        
        
        if not os.path.exists(json_file_path):
            print(f"{json_file_path} dosyası bulunamadı.")
            return

        with open(json_file_path, 'r') as kullanici_dosyasi:
            kullanici_1 = json.load(kullanici_dosyasi)
        while True:
            user_password = input("Şifre: ")
            if user_password == kullanici_1["user_password"]:
                print("Giriş başarılı!")
                break
            else:
                print("Hatalı şifre....")
    else:
        print("Geçersiz kullanıcı adı....")

def register():
    while True:
        try:
            name, surname = input("İsim ve soyisim sırası ile: ").split()
            break
        except:
            print("Lütfen arada boşluk bırakarak yazınız.")
    while True:
        tc_kimlik_no = input("Lütfen TC Kimlik Numaranızı girin: ")

        if len(tc_kimlik_no) != 11:
            print("Hata: TC Kimlik Numarası 11 haneden oluşmalıdır. Lütfen tekrar deneyin.")
            continue

        if not tc_kimlik_no.isdigit():
            print("Hata: TC Kimlik Numarası sadece rakamlardan oluşmalıdır. Lütfen tekrar deneyin.")
            continue

        if tc_kimlik_no[0] == '0':
            print("Hata: TC Kimlik Numarası ilk hanesi sıfır olamaz. Lütfen tekrar deneyin.")
            continue
        else:
            break
    while True:
        try:
            anne, baba = input("Anne ve baba adı giriniz sırası ile: ").split()
            break
        except:
            print("lütfen arada boşluk bırakarak giriniz..")
    while True:
        try:
            birthday_str = input("Doğum tarihiniz(GG/AA/YYYY): ")
            birthday_dt = datetime.strptime(birthday_str, "%d/%m/%Y")
            break
        except:
            print("Lütfen doğum tarihinizi gün/ay/yıl olarak giriniz...")
         #   print("Hatalı formatta girniz lütfen gün/ay/yıl olarak giriniz..")
    #day, month, year = list(map(int, birthday.split("/")))
    #birthdate = datetime.date(year, month, day)


    while True:
        try:
            user_name = input("Kullanıcı adı oluşturunuz: ")

            if os.path.exists(os.path.join(r"E:\metakod\menu", user_name + '.json')):
                print("Bu kullanıcı adı zaten var.")
            else:
                user_password = input("Şifre oluşturunuz:")
                veri = {
                    "name": name,
                    "surname": surname,
                    "tc_kimlik": tc_kimlik_no,
                    "birthdate": birthday_dt.strftime("%d/%m/%Y"),
                    "user_name": user_name,
                    "user_password": user_password
                }

                # Kullanıcıya özel JSON dosyasını oluştur ve verileri kaydet
                json_file_path = os.path.join(r"E:\metakod\menu", user_name + '.json')
                with open(json_file_path, 'w', encoding='utf-8') as dosya:
                    json.dump(veri, dosya, ensure_ascii=False, indent=4)

                user_file_path = r"E:\metakod\menu\user_name.txt"
                with open(user_file_path, 'a') as kullanici:
                    kullanici.write(user_name +'\n')
                print("kullanıcı başarı ile oluşturuldu.")
                break
        except:
            pass

def login_menu():
    c = 0
    while c ==0:
        print("""
                Kullanıcı arayüzüne hoşgeldiniz
                
                
                
            """)
   
admin_password = "12345678"
x = input("Programın şifresini giriniz: ")
if x != admin_password:
    print("Yanlış şifre...")
else:
    b = 2
    while b == 2:
        print(""" 
                  Programa hoşgeldiniz

                  Giriş için '1'
                  Yeni kayıt için '2'
                  Çıkış yapmak için '3'
                  """)
        a = input("....=")
        if a == "1":
            try:
                user_name = input("Kullanıcı adı: ")
                login(user_name)
            except:
                print("Fatal Error")
        elif a == "2":
            register()
        elif a == "3":
            b = 5
        else:
            print("Geçersiz komut.")
