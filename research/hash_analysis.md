# Hash Analizi (MD5, SHA-1, SHA-256) ve Salt Kullanımı

## Tanım
Hash analizi, bir parolanın (veya herhangi bir veri) belirli bir hash fonksiyonu (örneğin, MD5, SHA-1, SHA-256) kullanılarak sabit uzunlukta bir hash değerine dönüştürülmesi ve bu hash değerinin güvenlik açısından incelenmesi sürecidir. Hash fonksiyonları, veri bütünlüğünü sağlamak, parolaları saklamak ve dijital imzalar oluşturmak gibi amaçlarla kullanılır. Ancak, bazı hash fonksiyonları (örneğin, MD5, SHA-1) artık güvenli kabul edilmemektedir çünkü çakışma (collision) saldırılarına açıktır. Ayrıca, salt (tuz) kullanımı, her parolaya benzersiz bir salt ekleyerek hash değerini hesaplamak, rainbow table veya dictionary attack gibi saldırıları etkisiz hale getirir.

## Nasıl Çalışır?
- **Hash Fonksiyonu:** Bir parola (veya veri) belirli bir hash fonksiyonu (örneğin, MD5, SHA-1, SHA-256) ile işlenir ve sabit uzunlukta bir hash değeri (genellikle onaltılık (hex) formatında) üretilir. Örneğin, "password123" parolası MD5 ile işlendiğinde "ef73781effc5774100f87fe2f437a435" gibi bir hash değeri elde edilir.
- **Salt Kullanımı:** Salt, parolaya eklenen rastgele (veya benzersiz) bir değerdir. Böylece, aynı parola için bile farklı hash değerleri üretilir. Örneğin, "password123" parolasına "mysalt" salt eklenerek MD5 ile işlendiğinde, "password123mysalt" için farklı bir hash değeri (örneğin, "a1b2c3d4e5f6g7h8i9j0") elde edilir. Bu, önceden hesaplanmış hash tabloları (rainbow table) veya sözlük saldırılarını (dictionary attack) etkisiz hale getirir.

## Avantajları
- **Veri Bütünlüğü:** Hash fonksiyonları, veri bütünlüğünü sağlamak için kullanılabilir. Örneğin, bir dosyanın hash değeri hesaplanır ve dosya değiştirilirse, hash değeri değişir.
- **Parola Saklama:** Parolalar açık metin (plaintext) olarak saklanmak yerine, hash değeri olarak saklanabilir. Böylece, veritabanı sızıntısı durumunda bile parolalar açığa çıkmaz.
- **Salt Kullanımı:** Salt eklenerek, aynı parola için bile farklı hash değerleri üretilir. Bu, önceden hesaplanmış hash tabloları (rainbow table) veya sözlük saldırılarını (dictionary attack) etkisiz hale getirir.

## Dezavantajları
- **Çakışma (Collision) Saldırıları:** Bazı hash fonksiyonları (örneğin, MD5, SHA-1) artık güvenli kabul edilmemektedir çünkü çakışma (collision) saldırılarına açıktır. Yani, farklı iki veri aynı hash değerini üretebilir.
- **Hız:** Hash fonksiyonları (örneğin, MD5, SHA-1, SHA-256) hızlıdır. Bu, brute force veya dictionary attack gibi saldırılar için avantaj sağlar. Bu nedenle, parola saklama için hesaplama açısından pahalı (örneğin, bcrypt, scrypt, Argon2) hash algoritmaları önerilir.
- **Salt Kullanımı:** Salt kullanımı, her parola için ayrı bir salt değeri saklamayı gerektirir. Bu, veritabanı yönetimini biraz karmaşıklaştırabilir.

## Örnek Python Kodu
Aşağıda, bu projede kullanılan basit bir hash analizi (örneğin, MD5, SHA-1, SHA-256) ve salt kullanımı örneği verilmiştir:

```python
import hashlib

def compute_hash(password, hash_algo='md5'):
    if hash_algo == 'md5':
        h = hashlib.md5(password.encode()).hexdigest()
    elif hash_algo == 'sha1':
        h = hashlib.sha1(password.encode()).hexdigest()
    elif hash_algo == 'sha256':
        h = hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Desteklenmeyen hash algoritması: " + hash_algo)
    return h

def compute_hash_with_salt(password, salt, hash_algo='md5'):
    salted_password = password + salt
    return compute_hash(salted_password, hash_algo)

# Kullanım örneği
password = 'password123'
print("Parola: " + password)
print("MD5 hash (salt olmadan): " + compute_hash(password, 'md5'))
print("SHA-1 hash (salt olmadan): " + compute_hash(password, 'sha1'))
print("SHA-256 hash (salt olmadan): " + compute_hash(password, 'sha256'))

salt = 'mysalt'
print("Salt: " + salt)
print("MD5 hash (salt ile): " + compute_hash_with_salt(password, salt, 'md5'))
```

## Korunma Yöntemleri
- **Güçlü Hash Algoritmaları Kullanmak:** Parola saklama için hesaplama açısından pahalı (örneğin, bcrypt, scrypt, Argon2) hash algoritmaları kullanmak.
- **Salt Kullanmak:** Her parolaya benzersiz bir salt ekleyerek hash değerini hesaplamak, rainbow table veya dictionary attack gibi saldırıları etkisiz hale getirir.
- **Parola Politikalarını Sıkılaştırmak:** Uzun, karmaşık ve tahmin edilmesi zor parolalar kullanmak.
- **Çok Faktörlü Kimlik Doğrulama Uygulamak:** Hesap güvenliğini artırmak için çok faktörlü kimlik doğrulama (örneğin, SMS, e-posta, uygulama) kullanmak.

## Kaynaklar
- [Wikipedia: Cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [OWASP: Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) 