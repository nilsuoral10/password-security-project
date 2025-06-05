# Parola Gücü Ölçümü (Password Strength) Modülü

Bu modül, kullanıcının girdiği parolanın karmaşıklığını (örneğin, uzunluk, büyük/küçük harf, rakam, özel karakter vb.) ve tahmin edilebilirliğini (örneğin, yaygın sözlük parolalarına karşı) analiz ederek bir puan (0–100) ve açıklama döndürür.

## Kullanım

Modül, `compute_password_strength(password)` fonksiyonunu içerir. Bu fonksiyon, bir parola (str) alır ve aşağıdaki anahtarları içeren bir sözlük (dict) döndürür:

- **score**: (int) Parola gücü puanı (0–100). (Örneğin, uzunluk ≥ 8 ise + 20, büyük harf varsa + 20, küçük harf varsa + 20, rakam varsa + 20, özel karakter varsa + 20, ve eğer parola yaygın bir sözlük parolası ise – 20 puan.)
- **explanation**: (str) Parola gücü puanının nasıl hesaplandığını açıklayan bir metin.

Ayrıca, modül komut satırından çalıştırıldığında (örneğin, `python src/password_cracking/password_strength.py` veya `python src/password_cracking/password_strength.py "örnek parola"`), kullanıcıdan bir parola alır (veya komut satırından verilen parolayı kullanır) ve sonucu ekrana yazdırır.

## Örnek

```python
from password_cracking.password_strength import compute_password_strength

parola = "ÖrnekParola123!"
sonuç = compute_password_strength(parola)
print("Parola Gücü Puanı:", sonuç["score"])
print("Açıklama:", sonuç["explanation"])
```

Çıktı (örneğin):

```
Parola Gücü Puanı: 100
Açıklama: Uzunluk (≥ 8) + 20 puan. Büyük harf (en az bir tane) + 20 puan. Küçük harf (en az bir tane) + 20 puan. Rakam (en az bir tane) + 20 puan. Özel karakter (en az bir tane) + 20 puan. Parola sözlükte bulunmadı (tahmin edilebilirlik düşük).
```

## Not

- Sözlük kontrolü için, proje kök dizininde (örneğin, `common_passwords.txt`) bir dosya bulunmalıdır. Eğer dosya yoksa, tahmin edilebilirlik kontrolü yapılmaz.
- Modül, proje kök dizinini (örneğin, sözlük dosyası için) `sys.path`'e ekler. 