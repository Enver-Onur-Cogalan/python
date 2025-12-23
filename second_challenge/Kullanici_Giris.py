db_ka = "admin"
db_ps = 1234

while True:

    kullanıcı_adi = (input("Lütfen kullanıcı adını giriniz: "))
    kullanıcı_ps = (int(input("Lütfen Şifrenizi girininiz: ")))

    if db_ka == kullanıcı_adi and db_ps == kullanıcı_ps:
        print("Hoşgeldiniz: ", kullanıcı_adi)
        break
# Lütfen kullanıcı adını giriniz: admin
# Lütfen Şifrenizi girininiz: 1234
# Hoşgeldiniz:  admin

    elif db_ka != kullanıcı_adi and db_ps == kullanıcı_ps:
        print("Kullanıcı adınız hatalı")

# Lütfen kullanıcı adını giriniz: dhsjafh
# Lütfen Şifrenizi girininiz: 1234
# Kullanıcı adınız hatalı

    elif db_ka == kullanıcı_adi and db_ps != kullanıcı_ps:
        print ("Şifreniz hatalı")
        print("Şifre değiştirilsin mi ? E/H")
        cevap = input()
        if cevap == "E":
            print("Şifreniz değiştiriliyor...")
            yeni_sifre = int(input("Lütfen yeni şifrenizi yazınız: "))
            db_ps = yeni_sifre

# Lütfen kullanıcı adını giriniz: admin
# Lütfen Şifrenizi girininiz: 4545
# Şifreniz hatalı
# Şifre değiştirilsin mi ? E/H
# E
# Şifreniz değiştiriliyor...
# Lütfen yeni şifrenizi yazınız: 4545
# Lütfen kullanıcı adını giriniz: admin
# Lütfen Şifrenizi girininiz: 4545
# Hoşgeldiniz:  admin

    else:
        print("Kullanıcı adı ve şifresi hatalı.")

# Lütfen kullanıcı adını giriniz: 11111
# Lütfen Şifrenizi girininiz: 11111
# Kullanıcı adı ve şifresi hatalı.