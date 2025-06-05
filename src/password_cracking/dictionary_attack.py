import hashlib

def dictionary_attack(target_hash, hash_func, wordlist):
    """
    Basit sözlük saldırısı ile parola kırıcı.
    :param target_hash: Kırılması istenen hash (string)
    :param hash_func: Hash fonksiyonu (örn: lambda s: hashlib.md5(s.encode()).hexdigest())
    :param wordlist: Parola adaylarının listesi
    :return: Parola bulunduysa string, bulunamadıysa None
    """
    for word in wordlist:
        word = word.strip()
        if hash_func(word) == target_hash:
            return word
    return None

if __name__ == "__main__":
    # Örnek: 'password123' parolasının md5 hash'i
    password = 'password123'
    target_hash = hashlib.md5(password.encode()).hexdigest()
    # Basit bir sözlük
    wordlist = ['123456', 'password', 'admin', 'password123', 'letmein']
    print(f"Hedef hash: {target_hash}")
    result = dictionary_attack(target_hash, lambda s: hashlib.md5(s.encode()).hexdigest(), wordlist)
    if result:
        print(f"Parola bulundu: {result}")
    else:
        print("Parola bulunamadı.") 