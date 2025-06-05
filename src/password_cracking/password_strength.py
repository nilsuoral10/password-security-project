import re
import string
import sys
from pathlib import Path

# Proje kök dizinini sys.path'e ekle (örneğin, sözlük dosyası için)
sys.path.append(str(Path(__file__).parent.parent))

# Örnek bir sözlük dosyası (örneğin, yaygın parolalar listesi) kullanılabilir.
# Bu örnekte, sözlük dosyası (örneğin, "common_passwords.txt") proje kök dizininde olmalıdır.
# Eğer dosya yoksa, sözlük saldırı kontrolü yapılmaz.
DICTIONARY_FILE = Path(__file__).parent.parent / "common_passwords.txt"


def compute_password_strength(password):
    """
    Kullanıcının girdiği parolanın gücünü (karmaşıklık ve tahmin edilebilirlik) analiz eder.
    :param password: (str) Kullanıcının girdiği parola.
    :return: (dict) Parola gücü puanı (0–100) ve açıklama (str).
    """
    if not password:
        return {"score": 0, "explanation": "Parola boş."}

    # Karmaşıklık puanı (0–100) hesaplanıyor.
    score = 0
    explanation = []

    # Uzunluk kontrolü (örneğin, 8'den uzun ise + 20 puan)
    if len(password) >= 8:
        score += 20
        explanation.append("Uzunluk (≥ 8) + 20 puan.")
    else:
        explanation.append("Uzunluk ( < 8 ) yetersiz.")

    # Büyük harf kontrolü (en az bir büyük harf varsa + 20 puan)
    if re.search(r'[A-Z]', password):
        score += 20
        explanation.append("Büyük harf (en az bir tane) + 20 puan.")
    else:
        explanation.append("Büyük harf yok.")

    # Küçük harf kontrolü (en az bir küçük harf varsa + 20 puan)
    if re.search(r'[a-z]', password):
        score += 20
        explanation.append("Küçük harf (en az bir tane) + 20 puan.")
    else:
        explanation.append("Küçük harf yok.")

    # Rakam kontrolü (en az bir rakam varsa + 20 puan)
    if re.search(r'[0-9]', password):
        score += 20
        explanation.append("Rakam (en az bir tane) + 20 puan.")
    else:
        explanation.append("Rakam yok.")

    # Özel karakter kontrolü (en az bir özel karakter varsa + 20 puan)
    if re.search(r'[^A-Za-z0-9]', password):
        score += 20
        explanation.append("Özel karakter (en az bir tane) + 20 puan.")
    else:
        explanation.append("Özel karakter yok.")

    # Tahmin edilebilirlik kontrolü (örneğin, sözlük dosyasında parola varsa, puanı düşür)
    if DICTIONARY_FILE.exists():
        with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
            common_passwords = [line.strip() for line in f.readlines()]
        if password.lower() in [p.lower() for p in common_passwords]:
             score -= 20
             explanation.append("Parola yaygın bir sözlük parolası (– 20 puan).")
        else:
             explanation.append("Parola sözlükte bulunmadı (tahmin edilebilirlik düşük).")
    else:
         explanation.append("Sözlük dosyası (common_passwords.txt) bulunamadı, tahmin edilebilirlik kontrolü yapılmadı.")

    # Açıklamayı birleştir.
    explanation_str = " ".join(explanation)

    return {"score": score, "explanation": explanation_str}


if __name__ == "__main__":
    # Örnek kullanım: Komut satırından parola alıp gücünü hesapla.
    if len(sys.argv) > 1:
         parola = sys.argv[1]
    else:
         parola = input("Parola girin (güç analizi için): ")
    sonuç = compute_password_strength(parola)
    print("Parola Gücü Puanı:", sonuç["score"])
    print("Açıklama:", sonuç["explanation"]) 