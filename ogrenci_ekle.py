import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()


def student_add():

    def first_name (name):
        if name.isalpha(input("Öğrencinin ismini girin: ")):
            print(" ")
        else:
            print("Lütfen sadece harf giriniz.")
        first_name()
    
    
    
    

    def last_name (lastname):
        if lastname.isalpha():
            print(" ")
        else:
            print("Lütfen sadece harf giriniz.")
            
    input_str = input("Öğrencinin soyad'ını girin: ")
    last_name(input_str)


    def age (yas):
        if yas.isalpha():
            print(" ")
        else:
            print("Lütfen sadece sayı giriniz.")
            
    input_int = input("Öğrencinin yaş'ını girin: ")
    first_name(input_int)


    def gender (cinsiyet):
        if cinsiyet.isalpha():
            print(" ")
        else:
            print("Lütfen sadece harf giriniz.")
            
    input_str = input("Öğrenci'nin cinsiyet'ini girin: ")
    first_name(input_str)




    cursor.execute(
        "INSERT INTO students (first_name, last_name, age, gender) VALUES (?, ?, ?, ?)",
        (first_name, last_name, age, gender)
    )

    conn.commit()  # Değişiklikleri veritabanına kaydet

    print("Öğrenci eklenmiştir")




conn.close()
