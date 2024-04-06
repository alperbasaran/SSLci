# SSLci
SSL Sertifikası geçerlilik süresi kontrolü yapar. 

![SSLci](https://github.com/alperbasaran/SSLci/assets/8544424/fa708be2-8941-440e-9bf8-eda361a090c4)

Sertifikayı veren kuruluş, geçerlilik süresi ve geçerlilik süresinin bitmesine kalan gün sayısını "ssl_bilgileri.txt" dosyasına yazar. 

## Nasıl kullanılır?

1. sslci.exe'nin bulunduğu klasöre "adresler.txt" adında bir .txt dosyası oluşturup alanadlarını altalta (her satıra bir tane olacak şekilde) yazın.
2. sslci.exe'ye çift tıklayıp çalıştırın
3. Programın çalışması bitince oluşan "sertifika_bilgileri.txt" dosyasını kontrol edin
NOT: Çalışması bitince bir encoding hatası veriyor ancak çalışıyor, dert etmeyiniz. Vaktini bulunca düzelteceğim. 

## Neye dikkat etmek lazım?
Süresi geçmiş veya süresinin bitmesine çok az süre kalan alanadlarınız için yeni sertifika alınması gerekiyor.

# Sertifika süresi dolarsa ne olur?
İlk akla gelebilecek sorunlar şunlardır. 

## Ziyaretçi deneyimi olumsuz etkilenir
Sayfayı ziyaret eden kullanıcıların karşısına çıkacak "bu sayfa güvenilmez" türü uyarılar hem deneyim, hem güven açısından olumsuz olabilir. 

## Düşen web trafiği
Arama motorları sertifika süresi dolmuş siteleri sonuçlar içerisinde daha geride gösterebilir. 

## Man-in-the-Middle saldırısı olasılığı
Süre dolan sertifika işini yapmayacağı için uygulamanız ve uygulamanızın kullanıcıları için Man-in-the-Middle saldırı riski artar. 

## Uyum sorunları
Pek çok standart ve denetim yönetmeliği web uygulamalarının TLS kullanmasını talep ediyor. 

