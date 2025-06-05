# ROADMAP (Password Security Project)

Bu dosya, projenin (password-security-project) geliştirme adımlarını ve hedeflerini özetler.

## 1. Proje Yapısı ve Temel Araçlar

- [x] Proje dizin yapısı (örneğin, src, docs, tools, tests vb.) oluşturuldu.
- [x] (Örneğin, ROADMAP, password_strength.md, README.md vb.) belgeler (markdown dosyaları) oluşturuldu.
- [x] (Örneğin, sözlük dosyası (common_passwords.txt) vb.) yardımcı dosyalar (tools) oluşturuldu.

## 2. Parola Gücü Ölçümü (Password Strength)

- [x] Kullanıcının girdiği parolanın karmaşıklığını (örneğin, uzunluk, büyük/küçük harf, rakam, özel karakter vb.) ve tahmin edilebilirliğini (örneğin, yaygın sözlük parolalarına karşı) analiz eden bir modül (src/password_cracking/password_strength.py) geliştirildi.
- [x] (Örneğin, password_strength.md) belge (markdown dosyası) oluşturuldu.

## 3. CLI (Command Line Interface)

- [x] Komut satırından (örneğin, parola gücü ölçümü, parola kırma vb.) işlevleri çalıştırmak için bir CLI aracı (örneğin, src/cli.py) geliştirildi.

## 4. Web Arayüzü (Flask)

- [x] Flask kullanılarak, kullanıcıların (örneğin, parola gücü ölçümü, parola kırma vb.) işlevlerini tarayıcıdan çalıştırmasına olanak tanıyan bir web arayüzü (örneğin, src/web/app.py) geliştirildi.

## 5. Birim Testleri (Unit Tests)

- [ ] (Örneğin, parola gücü ölçümü, CLI, web arayüzü vb.) için birim testleri (örneğin, tests/test_password_strength.py, tests/test_cli.py, tests/test_web.py vb.) yazılacak.

## 6. Parola Kırma (Password Cracking) Araçları

- [ ] (Örneğin, brute force, sözlük saldırıları vb.) parola kırma tekniklerini (örneğin, src/password_cracking/cracker.py vb.) araştırmak ve araçlar geliştirmek.

## 7. Hash Algoritmalarının Zayıflıkları (Weaknesses of Hashing Algorithms)

- [ ] (Örneğin, MD5, SHA-1 vb.) hash algoritmalarının (örneğin, çarpışma (collision), ön görüntü (preimage) vb.) zayıflıklarını araştırmak ve (örneğin, src/password_cracking/hash_weakness.py vb.) araçlar geliştirmek.

## 8. (İleride) Ek Araçlar ve Araştırmalar

- [ ] (Örneğin, parola politikaları, çok faktörlü kimlik doğrulama (MFA) vb.) ek araçlar ve araştırmalar (örneğin, src/extra/... vb.) geliştirmek. 