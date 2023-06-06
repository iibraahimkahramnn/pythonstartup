import sqlite3
import ogrenci_listele
import ogrenci_ekle
import ogrenci_sil
import ogrenci_düzenle

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

def menü():
    while True:
        print("\n-- İşlem Menüsü --")
        print("1. Öğrencileri Listele")
        print("2. Öğrenci Ekle")
        print("3. Öğrenci Sil")
        print("4. Öğrenci Düzenle")
        print("5. Çıkış Yap")

        secenek = input("Seçiminizi yapın: ")

        if (secenek == "1"):
            ogrenci_listele.student_list()
        elif (secenek == "2"):
            ogrenci_ekle.student_add()
        elif (secenek == "3"):
            ogrenci_sil.student_delete()
        elif (secenek == "4"):
            ogrenci_düzenle.student_edit()
        elif (secenek == "5"):
            break
        else:
            print("Yanlış tuşa bastınız, tekrar deneyiniz.")
        menü()
        conn.commit()
    conn.close()
menü()
