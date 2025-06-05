# Rainbow Table (Gökkuşağı Tablosu) Saldırısı

## Tanım
Rainbow Table (gökkuşağı tablosu) saldırısı, önceden hesaplanmış hash değerlerini bir tabloda (genellikle bir sözlük (dictionary) olarak) saklayarak parola kırma sürecini hızlandıran bir saldırı türüdür. Bu yöntem, her seferinde hash hesaplamak yerine, hedef hash değerini tabloda arayarak parolayı bulmaya çalışır.

## Nasıl Çalışır?
- Saldırgan, belirli bir sözlük (wordlist) ve hash fonksiyonu (örneğin, MD5) kullanarak bir rainbow table oluşturur. Bu tablo, her parola adayının hash değerini (örneğin, MD5) içerir.
- Hedef hash değeri (örneğin, kırılması istenen parolanın MD5 hash'i) rainbow table'da aranır.
- Eğer hedef hash tabloda bulunursa, karşılık gelen parola (yani, o hash değerine sahip parola) bulunmuş olur.

## Avantajları
- Hash hesaplama maliyeti (örneğin, MD5) yüksek olduğundan, önceden hesaplanmış bir tablo kullanmak parola kırma sürecini çok hızlandırır.
- Özellikle kısa ve yaygın parolalar için oldukça etkilidir.
- Brute force veya dictionary attack gibi yöntemlere göre daha hızlıdır.

## Dezavantajları
- Rainbow table oluşturmak için önceden hesaplama (precomputation) gerektirir; bu da büyük depolama alanı ve zaman gerektirebilir.
- Salt (tuz) kullanıldığında (örneğin, her parolaya benzersiz bir salt eklenerek hash hesaplanırsa) rainbow table etkisiz hale gelir çünkü her parola için farklı bir hash değeri oluşur.
- Sözlükte olmayan (veya tabloda bulunmayan) güçlü ve rastgele parolalar için başarısız olur.

## Örnek Python Kodu
Aşağıda, bu projede kullanılan basit bir Rainbow Table (gökkuşağı tablosu) örneği verilmiştir:

```python
import hashlib

def generate_rainbow_table(wordlist, hash_func):
    rainbow_table = {}
    for word in wordlist:
        word = word.strip()
        hash_value = hash_func(word)
        rainbow_table[hash_value] = word
    return rainbow_table

def crack_using_rainbow_table(target_hash, rainbow_table):
    return rainbow_table.get(target_hash, None)

# Kullanım örneği
password = 'password123'
target_hash = hashlib.md5(password.encode()).hexdigest()
wordlist = ['123456', 'password', 'admin', 'password123', 'letmein']
rainbow_table = generate_rainbow_table(wordlist, lambda s: hashlib.md5(s.encode()).hexdigest())
result = crack_using_rainbow_table(target_hash, rainbow_table)
print(result)
```

## Korunma Yöntemleri
- Salt (tuz) kullanmak: Her parolaya benzersiz bir salt ekleyerek hash değerini hesaplamak, rainbow table saldırılarını etkisiz hale getirir.
- Güçlü ve karmaşık parolalar kullanmak.
- Hesaplama açısından pahalı (örneğin, bcrypt, scrypt, Argon2) hash algoritmaları kullanmak.
- Hesap denemelerini sınırlamak (rate limiting) ve çok faktörlü kimlik doğrulama uygulamak.

## Kaynaklar
- [Wikipedia: Rainbow table](https://en.wikipedia.org/wiki/Rainbow_table)
- [OWASP: Password Attacks](https://owasp.org/www-community/attacks/Password_Attacks) 