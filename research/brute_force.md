# Brute Force Parola Kırma Yöntemi

## Tanım
Brute force (kaba kuvvet) saldırısı, bir parolanın olası tüm kombinasyonlarının sistematik olarak denenmesiyle parolanın bulunmasını amaçlayan bir saldırı türüdür. En basit ve en garantili parola kırma yöntemlerinden biridir, ancak genellikle en yavaş olanıdır.

## Nasıl Çalışır?
- Saldırgan, belirli bir karakter seti ve maksimum uzunluk belirler.
- Tüm olası kombinasyonlar sırayla denenir.
- Her deneme, hedef hash veya parola ile karşılaştırılır.
- Doğru kombinasyon bulunduğunda saldırı sona erer.

## Avantajları
- Teorik olarak her zaman başarılıdır (yeterli zaman ve kaynak varsa).
- Karmaşık algoritmalara veya özel bilgiye ihtiyaç duymaz.

## Dezavantajları
- Çok yavaştır; parola uzunluğu ve karakter seti büyüdükçe deneme sayısı üstel olarak artar.
- Güçlü, uzun ve karmaşık parolalar için pratik değildir.
- Hesaplama gücü ve zaman gereksinimi yüksektir.

## Örnek Python Kodu
Aşağıda, bu projede kullanılan basit bir brute force parola kırıcı örneği verilmiştir:

```python
import itertools
import string
import hashlib

def brute_force_crack(target_hash, hash_func, max_length=4, charset=string.ascii_lowercase):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_str = ''.join(guess)
            if hash_func(guess_str) == target_hash:
                return guess_str
    return None

# Kullanım örneği
password = 'abc'
target_hash = hashlib.md5(password.encode()).hexdigest()
result = brute_force_crack(target_hash, lambda s: hashlib.md5(s.encode()).hexdigest(), max_length=4)
print(result)
```

## Korunma Yöntemleri
- Uzun ve karmaşık parolalar kullanmak
- Hesaplama açısından pahalı hash algoritmaları (örn. bcrypt, scrypt, Argon2) kullanmak
- Hesap denemelerini sınırlamak (rate limiting)
- Captcha ve iki faktörlü kimlik doğrulama uygulamak

## Kaynaklar
- [Wikipedia: Brute-force attack](https://en.wikipedia.org/wiki/Brute-force_attack)
- [OWASP: Password Attacks](https://owasp.org/www-community/attacks/Password_Attacks) 