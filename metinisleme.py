okunanDosya = open("metinisleme.txt", 'rt')
okunanMetin = okunanDosya.read()
okunanMetin = okunanMetin.lower()
okunanDosya.close()
print(okunanMetin)

anahtarKelimeler = [
                    "bilgi",
                    "belge",
                    "açık",
                    "erişim",
                    "bilim",
                    "büyük",
                    "veri",
                    "semantik",
                    "teknoloji",
                    "makine",
                    "öğrenmesi",
                    "yapay",
                    "zeka"
]
print(anahtarKelimeler)

for anahtarKelime in anahtarKelimeler:
  sonuc = okunanMetin.count(anahtarKelime)
  print(anahtarKelime+": " + str(sonuc))
  hesaplama=sonuc*1/100
  print("Bu metnin yüzde",sonuc*1/100,"'ü",anahtarKelime+" ","ile ilgili")
  if sonuc >= 4:
    print("Bu metnin konusu",anahtarKelime+" ile ilgilidir.")
  else:
    print("Konuyu tespit edebilmek için daha fazla yazı gerekli")