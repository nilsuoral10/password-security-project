# Web Arayüzü (Flask) Uygulaması

Bu uygulama, Flask kullanılarak geliştirilmiş, kullanıcıların (örneğin, parola gücü ölçümü, parola kırma vb.) işlevlerini tarayıcıdan çalıştırmasına olanak tanıyan bir web arayüzüdür.

## Kullanım

Web arayüzü (örneğin, `src/web/app.py`) aşağıdaki endpoint'leri (örneğin, /, /strength vb.) sunar:

- **/ (Ana Sayfa)**: Kullanıcıya (örneğin, parola gücü ölçümü, parola kırma vb.) işlevlerini seçmesi için bir sayfa (örneğin, index.html) gösterir.

- **/strength (Parola Gücü Ölçümü)**: Kullanıcıdan bir parola alır (örneğin, POST ile) ve (örneğin, password_strength.py modülüne bağlanarak) parolanın karmaşıklığını (örneğin, uzunluk, büyük/küçük harf, rakam, özel karakter vb.) ve tahmin edilebilirliğini (örneğin, yaygın sözlük parolalarına karşı) analiz eder. Sonuç (örneğin, puan (0–100) ve açıklama) (örneğin, /strength sonuç sayfası (örneğin, strength.html) vb.) kullanıcıya gösterilir.

- (İleride) **/crack (Parola Kırma)**: (Örneğin, brute force, sözlük saldırıları vb.) parola kırma işlevlerini (örneğin, /crack sonuç sayfası (örneğin, crack.html) vb.) çalıştırmak için kullanılabilir.

## Çalıştırma

Proje kök dizininde (örneğin, `python src/web/app.py`) çalıştırılarak (örneğin, `http://localhost:5000`) tarayıcıdan erişilebilir.

## Örnek

- Tarayıcıda (örneğin, `http://localhost:5000`) ana sayfaya gidilir.
- (Örneğin, "Parola Gücü Ölçümü" vb.) işlev seçilir (örneğin, /strength endpoint'ine yönlendirilir).
- Kullanıcı (örneğin, "ÖrnekParola123!" vb.) bir parola girer (örneğin, POST ile) ve (örneğin, /strength sonuç sayfası (örneğin, strength.html) vb.) sonuç (örneğin, puan (0–100) ve açıklama) görüntülenir.

## Not

- Web arayüzü, (örneğin, sözlük dosyası (common_passwords.txt) vb.) yardımcı dosyaların proje kök dizininde bulunmasını bekler. 