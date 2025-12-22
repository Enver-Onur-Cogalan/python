vize_puanı = int(input("Lütfen Vize Notunuzu Giriniz: "))
final_puanı = int(input("Lütfen Final Notunuzu Giriniz: "))

ortalama_hesapla = (vize_puanı * 0.4) + (final_puanı * 0.6)

if ortalama_hesapla >= 60:
    durum = "Geçtiniz"
else:
    durum = "Kaldınız"

print('-'*30)
print(f"Vize Puanınız: {vize_puanı}\nFinal Puanınız: {final_puanı}\nOrtalamanız: {ortalama_hesapla}\nDurum: {durum}")
print('-'*30)


# DURUM 1:
# Lütfen Vize Notunuzu Giriniz: 45
# Lütfen Final Notunuzu Giriniz: 75
# ------------------------------
# Vize Puanınız: 45
# Final Puanınız: 75
# Ortalamanız: 63.0
# Durum: Geçtiniz
# ------------------------------

# DURUM 2:
# Lütfen Vize Notunuzu Giriniz: 75
# Lütfen Final Notunuzu Giriniz: 45
# ------------------------------
# Vize Puanınız: 75
# Final Puanınız: 45
# Ortalamanız: 57.0
# Durum: Kaldınız
# ------------------------------

