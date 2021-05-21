# Sifre-Saklama-Sistemi
Python'ın Pyside6 modülünden yararlanarak hazırladığım basit bir şifre saklama/yönetim sistemi.
Python Programlama 
(Şifre Saklama ve Yönetimi)



Yaptığımız bu program girdiğimiz siteler için verdiğimiz şifrelerimizi kaydedip saklamayı amaçlar.
Program başladığında tek kullanımlık şifre oluşturulur ve bu şifre yalnızca bir kere gözükür ve başlangıçta bu şifre kullanıcıdan istenir.Girilen şifre yanlış ise program sonlandırılır,doğru ise kullanıcı forma yönlendirilir.



<img alt="program goruntusu" src="https://github.com/osmnbkrerk/Sifre-Saklama-Sistemi/blob/main/resimler/program.png">
















                                      (Örnek-1)


    
   
  
Programımızda(Örnek-1) Site Adı,Site Adresi ve Şifresi yazan kısıma kaydetmek istediğimiz bilgilerimizi giriyoruz.Girilen bilgiler sqlite3 kullanarak oluşturduğumuz veritabanına kaydedilir.Programda kaydedilen şifrelerin güvenliği için Encrpyt ve Decrpyt özellikleri vardır.Encrypt It butonu kullanıldığında şifre gizlenir,Decrypt It butonu kullanıldığında ise asıl şifre gözükür.Kullanıcı isterse kaydedilen şifreleri Şifre Güncelle butonu ile değiştirebilir.
 
Programda Kullanılan Dosyalar/Kütüphaneler


•	sifre.json Dosyası :  Sadece tek bir değişken ile şifreyi tek seferlik tutmayı sağlar.


•	my_db.db Dosyası : Siteye ait bilgileri (Site adı, Site Adresi, Şifre) tutan sqlite3 kullanarak oluşturulan veritabanı.

•	program.py Dosyası : Oluşturulan tek kullanımlık şifreyi  1000-9999 arasında rastgele bir sayı üretip sifre.json dosyasına yazdırır ve kontrol edip forma aktarır.

•	app_ui.py Dosyası :  Pyside6 designer kullanılarak oluşturulmuştur. Arayüz dosyasıdır.




              



  



              



<img alt="program goruntusu" src="https://github.com/osmnbkrerk/Sifre-Saklama-Sistemi/blob/main/resimler/qtdesigner.jpg">
 

                                                                                           (Örnek-2)

    Programın arayüzü tasarlanırken Pyside6(Örnek-2) kullanılmıştır. PyQt5 benzeri fonksiyonlar sağlayan Pyside6 aynı zamanda designer imkanı da sunuyor.

    Encryption ve Decryption olaylarında onetimepad paketi kullanılmıştır;
 
-( tut=onetimepad.encrypt(sifre,kilit)

   Örnekte gördüğümüz onetimepad kullanımı tut adlı değişkende şifrenin içindeki veriyi kilit kelimesine göre encrypt edilmiş halini saklar.

    

