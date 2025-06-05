# CLI (Command Line Interface) Aracı

Bu CLI aracı, komut satırından (örneğin, parola gücü ölçümü, parola kırma vb.) işlevleri çalıştırmak için kullanılır.

## Kullanım

CLI aracı (örneğin, `src/cli.py`) aşağıdaki komut satırı argümanlarını destekler:

- **--strength (veya -s)**: Parola gücü ölçümü (örneğin, `python src/cli.py --strength "örnek parola"` veya `python src/cli.py -s "örnek parola"`). Bu komut, (örneğin, `password_strength.py` modülüne bağlanarak) parolanın karmaşıklığını (örneğin, uzunluk, büyük/küçük harf, rakam, özel karakter vb.) ve tahmin edilebilirliğini (örneğin, yaygın sözlük parolalarına karşı) analiz eder ve bir puan (0–100) ile açıklama döndürür.

- **--crack (veya -c)**: (İleride) Parola kırma (örneğin, brute force, sözlük saldırıları vb.) işlevlerini çalıştırmak için (örneğin, `python src/cli.py --crack "hash"` veya `python src/cli.py -c "hash"`).

- **--help (veya -h)**: Yardım (örneğin, `python src/cli.py --help` veya `python src/cli.py -h`) ile kullanılabilir komutlar ve açıklamaları görüntülenir.

## Örnek

Aşağıdaki komut, "ÖrnekParola123!" parolasının gücünü ölçer:

```bash
python src/cli.py --strength "ÖrnekParola123!"
```


Çıktı (örneğin):

```
Parola Gücü Puanı: 100
Açıklama: Uzunluk (≥ 8) + 20 puan. Büyük harf (en az bir tane) + 20 puan. Küçük harf (en az bir tane) + 20 puan. Rakam (en az bir tane) + 20 puan. Özel karakter (en az bir tane) + 20 puan. Parola sözlükte bulunmadı (tahmin edilebilirlik düşük).
```


## Not

- CLI aracı, (örneğin, sözlük dosyası (common_passwords.txt) vb.) yardımcı dosyaların proje kök dizininde bulunmasını bekler. 