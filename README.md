# Parola Güvenliği Analiz Projesi
*Password Security Analysis Project*

Parola güvenliği ve tersine mühendislik konularını kapsayan kapsamlı bir araştırma ve uygulama projesi. Bu proje, güvenlik uzmanları, araştırmacılar ve eğitimciler için değerli bir kaynak olmayı hedeflemektedir.
*A comprehensive research and implementation project covering password security and reverse engineering topics. This project aims to be a valuable resource for security professionals, researchers, and educators.*

---

## Özellikler
*Features*

- **Parola Kırma Analizi:** Brute force, sözlük saldırıları ve rainbow table saldırıları dahil çeşitli parola kırma tekniklerinin detaylı implementasyonu ve analizi. Sosyal mühendislik tabanlı saldırıların da incelenmesi.
  *Password Cracking Analysis: Detailed implementation and analysis of various password cracking techniques including brute force, dictionary attacks, and rainbow table attacks.*

- **Hash Algoritma Analizi:** MD5, SHA-1, SHA-256 gibi yaygın hash algoritmalarının derinlemesine analizi. Salt ve pepper kullanımı, hash çakışmaları ve zayıf implementasyonların tespiti ve güvenlik açıklarının belirlenmesi.
  *Hash Algorithm Analysis: In-depth analysis of common hash algorithms like MD5, SHA-1, SHA-256, including salt and pepper usage, hash collisions, and weak implementations.*

- **Tersine Mühendislik Araçları:** Bellek dökümü analizi, statik ve dinamik analiz, binary dosya analizi ve güvenlik açığı tespiti için gelişmiş araçlar. Güvenlik testleri ve penetrasyon testleri için kullanılabilecek metodolojiler.
  *Reverse Engineering Tools: Advanced tools for memory dump analysis, static and dynamic analysis, binary file analysis, and security vulnerability detection.*

---

## Proje Yapısı
*Project Structure*

```
├── src/
│   ├── password_cracking/    # Parola kırma implementasyonları
│   ├── hash_analysis/        # Hash analiz araçları
│   └── reverse_engineering/  # Tersine mühendislik araçları
├── research/                 # Araştırma dokümanları
├── tools/                    # Yardımcı araçlar ve scriptler
├── tests/                    # Test senaryoları
└── docs/                     # Detaylı dokümantasyon
```

---

## Geliştirme Ortamı
*Development Environment*

- Python 3.8 ve üzeri
- Gerekli kütüphaneler: requirements.txt dosyasında belirtilmiştir
- Geliştirme araçları: IDA Pro, Ghidra, Wireshark (isteğe bağlı)

---

## Kurulum
*Installation*

1. **Depoyu Klonlayın / *Clone the Repository***:  
   ```bash
   git clone https://github.com/MD/password-security-project.git
   cd password-security-project
   ```

2. **Sanal Ortam Kurulumu / *Set Up Virtual Environment*** (Önerilen):  
   ```bash
   python -m venv venv
   # Windows için:
   venv\Scripts\activate
   # Linux/Mac için:
   source venv/bin/activate
   ```

3. **Bağımlılıkları Yükleyin / *Install Dependencies***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Kullanım
*Usage*

Bu proje sadece eğitim ve araştırma amaçlıdır. Geliştirilen araçlar ve teknikler yalnızca aşağıdaki durumlarda kullanılmalıdır:
*This project is intended for educational and research purposes only. The tools and techniques developed should only be used in the following cases:*

- Kendi sistemlerinizde
- İzin verilen test ortamlarında
- Etik hacking eğitimlerinde
- Güvenlik araştırmalarında

---

## Katkıda Bulunma
*Contributing*

1. Bu depoyu fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b ozellik/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Dalınızı push edin (`git push origin ozellik/yeni-ozellik`)
5. Pull Request oluşturun

---

## Lisans
*License*

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.
*This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.*

---

## Güvenlik Uyarısı
*Security Warning*

⚠️ Bu proje sadece eğitim ve araştırma amaçlıdır. Tüm araçlar ve teknikler sorumlu ve etik bir şekilde kullanılmalıdır. İzinsiz sistemlere erişim veya kötü niyetli kullanım yasalara aykırıdır.
*⚠️ This project is for educational and research purposes only. All tools and techniques should be used responsibly and ethically. Unauthorized access to systems or malicious use is illegal.*

---

## İletişim
*Contact*

Bir hata bulduysanız veya öneriniz varsa, lütfen bir sorun açın. Ayrıca projeye katkıda bulunmak isterseniz, yukarıdaki katkıda bulunma adımlarını takip edebilirsiniz.
*Found a bug or have a suggestion? Please open an issue. If you want to contribute to the project, you can follow the contributing steps above.*

---

## Ekip
*Team*

- **2320191047** - Nilsu Oral: Proje Geliştirici ve Araştırmacı
  *Project Developer and Researcher*
- **2320191051** - Zehra Kaba: Proje araştırmacısı
  *[Name Surname]: [Role or Contribution]*

*Not: Ekip üyeleri projeye katkıda bulundukça güncellenecektir.*
*Note: Team members will be updated as they contribute to the project.* 