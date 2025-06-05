# Password Security Analysis Project

Bu proje, parola güvenliği ve tersine mühendislik konularını kapsayan bir araştırma ve uygulama projesidir.

## Proje Hedefleri

1. **Parola Kırma Teknikleri Analizi**
   - Brute Force saldırıları
   - Dictionary saldırıları
   - Rainbow Table saldırıları
   - Sosyal mühendislik tabanlı saldırılar

2. **Hash Algoritmaları ve Zayıflıkları**
   - MD5, SHA-1, SHA-256 analizi
   - Salt ve Pepper kullanımı
   - Hash çakışmaları
   - Zayıf hash implementasyonları

3. **Tersine Mühendislik ile Parola Analizi**
   - Bellek dökümü analizi
   - Statik ve dinamik analiz
   - Binary dosya analizi
   - Güvenlik açığı tespiti

## Proje Yapısı

- `src/`: Kaynak kodlar
  - `password_cracking/`: Parola kırma teknikleri implementasyonları
  - `hash_analysis/`: Hash analizi ve zayıflık tespiti araçları
  - `reverse_engineering/`: Tersine mühendislik araçları
- `research/`: Araştırma dokümanları ve bulgular
- `tools/`: Yardımcı araçlar ve scriptler
- `tests/`: Test senaryoları ve test dosyaları
- `docs/`: Detaylı dokümantasyon

## Geliştirme Ortamı

- Python 3.8+
- Gerekli kütüphaneler: requirements.txt dosyasında belirtilecek
- Geliştirme araçları: IDA Pro, Ghidra, Wireshark (opsiyonel)

## Güvenlik Uyarısı

Bu proje sadece eğitim ve araştırma amaçlıdır. Projede geliştirilen araçlar ve teknikler yalnızca:
- Kendi sistemlerinizde
- İzin verilen test ortamlarında
- Etik hacking eğitimlerinde
kullanılmalıdır.

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız. 