import random
import time

kullanicilar = []

def guvenlı_int_input(mesaj):
    while True:
        deger = input(mesaj).strip()
        try:
            return int(deger)
        except ValueError:
            print("Lütfen sadece sayı giriniz.")


def kullanıcı_ekle():
    print("-"*30)
    print("Kullanıcı Ekleme Ekranına Hoşgeldiniz")

    ekle = input("Eklenecek kullanıcı(lar)ı yaz (virgülle ayırabilirsin): ").strip()

    if not ekle:
        print("Boş kullanıcı eklenemez.")
        return
    
    yeni_isimler = [i.strip() for i in ekle.split(",") if i.strip()]
    eklendi = 0

    for isim in yeni_isimler:
        if isim.lower() in [k.lower() for k in kullanicilar]:
            print(f"'{isim}' zaten listede var")
        else:
            kullanicilar.append(isim)
            eklendi += 1
            print(f"'{isim}' listeye eklendi.")

    if eklendi == 0:
        print("Yeni kullanıcı eklenmedi")


def kullanıcı_gor():
    print("-"*30)
    if not kullanicilar:
        print("Liste boş.")
        print("-"*30)
        return
    
    for idx, isim in enumerate(kullanicilar, start=1):
        print(f"{idx}- Kulanıcı Adı: {isim}")
    
    print("-"*30)
    
    
def karistir():
    print("-"*30)
    
    if not kullanicilar:
        print("Liste boş, karıştıracak kullanıcı yok.")
        print("-" * 30)
        return

    random.shuffle(kullanicilar)
    print("Kullanıcılar karıştırıldı ✅")
    kullanıcı_gor()

    print("-"*30)

def rastgele_sec():
    print("-"*30)

    if not kullanicilar:
        print("Liste boş, seçim yapılamaz.")
        print("-" * 30)
        return

    kisi_sec = guvenlı_int_input("Kaç kişi seçilsin ?: ")

    if kisi_sec <= 0:
        print("Seçim sayısı 1 veya daha büyük olmalı.")
        print("-" * 30)
        return
    
    if kisi_sec > len(kullanicilar):
        print(f"Maksimum {len(kullanicilar)} kişi seçilebilir.")
        print("-" * 30)
        return

    print("Kişi seçme alanı hesaplanıyor...")
    time.sleep(1)

    secilenler = random.sample(kullanicilar, kisi_sec)
    print("Seçilenler:")
    for idx, isim in enumerate(secilenler, start=1):
        print(f"{idx}-{isim}")
    print("-"*30)


while True:
    print("\n**** Çekiliş Uygulamasına Hoş Geldiniz ****")
    print("0- Çıkış")
    print("1- Kullanıcı Ekle")
    print("2- Kullanıcı Gör")
    print("3- Kullanıcıları Karıştır")
    print("4- Rastgele Seç")

    secim = guvenlı_int_input("Seçimin: ")

    if secim == 0:
        print("Çekiliş Sona Ermiştir")
        break

    elif secim == 1:
        kullanıcı_ekle()

    elif secim == 2:
        kullanıcı_gor()
    
    elif secim == 3:
        karistir()

    elif secim == 4:
        rastgele_sec()

    else:
        print("Lütfen menüden uygun bir tercih yapınız")


# **** Çekiliş Uygulamasına Hoş Geldiniz ****
# 0- Çıkış
# 1- Kullanıcı Ekle
# 2- Kullanıcı Gör
# 3- Kullanıcıları Karıştır
# 4- Rastgele Seç
# Seçimin: 1
# ------------------------------
# Kullanıcı Ekleme Ekranına Hoşgeldiniz
# Eklenecek kullanıcı(lar)ı yaz (virgülle ayırabilirsin): Eric Moren,Furkan,Ercan,Kaan,Bro
# 'Eric Moren' listeye eklendi.
# 'Furkan' listeye eklendi.
# 'Ercan' listeye eklendi.
# 'Kaan' listeye eklendi.
# 'Bro' listeye eklendi.

# **** Çekiliş Uygulamasına Hoş Geldiniz ****
# 0- Çıkış
# 1- Kullanıcı Ekle
# 2- Kullanıcı Gör
# 3- Kullanıcıları Karıştır
# 4- Rastgele Seç
# Seçimin: 2
# ------------------------------
# 1- Kulanıcı Adı: Eric Moren
# 2- Kulanıcı Adı: Furkan
# 3- Kulanıcı Adı: Ercan
# 4- Kulanıcı Adı: Kaan
# 5- Kulanıcı Adı: Bro
# ------------------------------

# **** Çekiliş Uygulamasına Hoş Geldiniz ****
# 0- Çıkış
# 1- Kullanıcı Ekle
# 2- Kullanıcı Gör
# 3- Kullanıcıları Karıştır
# 4- Rastgele Seç
# Seçimin: 3
# ------------------------------
# Kullanıcılar karıştırıldı ✅
# ------------------------------
# 1- Kulanıcı Adı: Bro
# 2- Kulanıcı Adı: Ercan
# 3- Kulanıcı Adı: Furkan
# 4- Kulanıcı Adı: Eric Moren
# 5- Kulanıcı Adı: Kaan
# ------------------------------
# ------------------------------

# **** Çekiliş Uygulamasına Hoş Geldiniz ****
# 0- Çıkış
# 1- Kullanıcı Ekle
# 2- Kullanıcı Gör
# 3- Kullanıcıları Karıştır
# 4- Rastgele Seç
# Seçimin: 4
# ------------------------------
# Kaç kişi seçilsin ?: 2
# Kişi seçme alanı hesaplanıyor...
# Seçilenler:
# 1-Furkan
# 2-Kaan
# ------------------------------

# **** Çekiliş Uygulamasına Hoş Geldiniz ****
# 0- Çıkış
# 1- Kullanıcı Ekle
# 2- Kullanıcı Gör
# 3- Kullanıcıları Karıştır
# 4- Rastgele Seç
# Seçimin: 0
# Çekiliş Sona Ermiştir

# HATA GÖSTERME:
# **** Çekiliş Uygulamasına Hoş Geldiniz ****
# 0- Çıkış
# 1- Kullanıcı Ekle
# 2- Kullanıcı Gör
# 3- Kullanıcıları Karıştır
# 4- Rastgele Seç
# Seçimin: a
# Lütfen sadece sayı giriniz.
# Seçimin: "
# Lütfen sadece sayı giriniz.
# Seçimin: 7
# Lütfen menüden uygun bir tercih yapınız