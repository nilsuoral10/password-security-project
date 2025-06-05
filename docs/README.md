# Password Security Project

Bu proje, parola güvenliği (örneğin, parola gücü ölçümü, parola kırma teknikleri, hash algoritmalarının zayıflıkları vb.) üzerine araştırma ve araçlar geliştirmeyi amaçlamaktadır.

## Proje Yapısı

- **src**: Kaynak kodlar (örneğin, parola gücü ölçümü, CLI, web arayüzü vb.) bu dizinde bulunur.
- **docs**: Proje (örneğin, ROADMAP, password_strength.md vb.) ve modüllerin kullanımına ilişkin belgeler (markdown dosyaları) bu dizinde yer alır.
- **tools**: Yardımcı araçlar (örneğin, sözlük dosyaları, test betikleri vb.) bu dizinde bulunabilir.
- **tests**: Birim testleri (örneğin, parola gücü ölçümü, CLI, web arayüzü vb.) bu dizinde yer alır.

## Modüller

### Parola Gücü Ölçümü (Password Strength)

Kullanıcının girdiği parolanın karmaşıklığını (örneğin, uzunluk, büyük/küçük harf, rakam, özel karakter vb.) ve tahmin edilebilirliğini (örneğin, yaygın sözlük parolalarına karşı) analiz eden bir modül. Detaylı kullanım için [password_strength.md](password_strength.md) dosyasına bakabilirsiniz.

### CLI (Command Line Interface)

Komut satırından (örneğin, parola gücü ölçümü, parola kırma vb.) işlevleri çalıştırmak için bir CLI aracı.

### Web Arayüzü (Flask)

Flask kullanılarak geliştirilmiş, kullanıcıların (örneğin, parola gücü ölçümü, parola kırma vb.) işlevlerini tarayıcıdan çalıştırmasına olanak tanıyan bir web arayüzü.

## Kurulum

Projeyi çalıştırmak için (örneğin, CLI veya web arayüzü) gerekli bağımlılıklar (örneğin, Flask vb.) kurulmalıdır. (Not: Proje, sanal ortam (virtual environment) kullanmadan, sistem Python ortamına kurulmuştur.)

## Kullanım

- **Parola Gücü Ölçümü (CLI):** Proje kök dizininde (örneğin, `python src/password_cracking/password_strength.py` veya `python src/password_cracking/password_strength.py "örnek parola"`) çalıştırılabilir.
- **Web Arayüzü:** Proje kök dizininde (örneğin, `python src/web/app.py`) çalıştırılarak (örneğin, `http://localhost:5000`) tarayıcıdan erişilebilir.

## Not

- Proje, (örneğin, sözlük dosyası (common_passwords.txt) vb.) yardımcı dosyaların proje kök dizininde bulunmasını bekler. 