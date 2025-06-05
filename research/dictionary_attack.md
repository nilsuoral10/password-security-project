# Dictionary Attack (Sözlük Saldırısı)

## Tanım
Dictionary attack (sözlük saldırısı), yaygın olarak kullanılan parolaların veya kelimelerin bir listesinin (sözlük) kullanılarak parolanın tahmin edilmeye çalışıldığı bir saldırı türüdür. Brute force saldırısına göre çok daha hızlıdır çünkü olası tüm kombinasyonlar yerine, en çok kullanılan veya tahmin edilmesi muhtemel parolalar denenir.

## Nasıl Çalışır?
- Saldırgan, yaygın parolalardan oluşan bir sözlük (wordlist) hazırlar.
- Sözlükteki her kelime, hedef hash veya parola ile karşılaştırılır.
- Doğru parola bulunduğunda saldırı sona erer.

## Avantajları
- Brute force saldırısına göre çok daha hızlıdır.
- Gerçek hayatta sık kullanılan zayıf parolalar için oldukça etkilidir.
- Hesaplama maliyeti düşüktür.

## Dezavantajları
- Sözlükte olmayan güçlü ve rastgele parolalar için başarısız olur.
- Sözlük güncel değilse başarı oranı düşer.
- Sözlük boyutu büyüdükçe depolama ihtiyacı artar.

## Örnek Python Kodu
Aşağıda, bu projede kullanılan basit bir sözlük saldırısı örneği verilmiştir:

```python
import hashlib

def dictionary_attack(target_hash, hash_func, wordlist):
    for word in wordlist:
        word = word.strip()
        if hash_func(word) == target_hash:
            return word
    return None

# Kullanım örneği
password = 'password123'
target_hash = hashlib.md5(password.encode()).hexdigest()
wordlist = ['123456', 'password', 'admin', 'password123', 'letmein']
result = dictionary_attack(target_hash, lambda s: hashlib.md5(s.encode()).hexdigest(), wordlist)
print(result)
```

## Korunma Yöntemleri
- Tahmin edilmesi zor, uzun ve karmaşık parolalar kullanmak
- Parola politikalarını sıkılaştırmak
- Sık kullanılan parolaların yasaklanması (blacklist)
- Hesap denemelerini sınırlamak (rate limiting)
- Çok faktörlü kimlik doğrulama uygulamak

## Kaynaklar
- [Wikipedia: Dictionary attack](https://en.wikipedia.org/wiki/Dictionary_attack)
- [OWASP: Password Attacks](https://owasp.org/www-community/attacks/Password_Attacks) 