import hashlib

def generate_rainbow_table(wordlist, hash_func):
    """
    Belirtilen sözlük (wordlist) ve hash fonksiyonu (hash_func) kullanarak bir rainbow table (gökkuşağı tablosu) oluşturur.
    :param wordlist: Parola adaylarının listesi (örneğin, ['password', 'admin', '123456', 'password123', 'letmein'])
    :param hash_func: Hash fonksiyonu (örneğin, lambda s: hashlib.md5(s.encode()).hexdigest())
    :return: Rainbow table (hash değeri -> parola) (dict)
    """
    rainbow_table = {}
    for word in wordlist:
        word = word.strip()
        hash_value = hash_func(word)
        rainbow_table[hash_value] = word
    return rainbow_table


def crack_using_rainbow_table(target_hash, rainbow_table):
    """
    Rainbow table (rainbow_table) kullanarak hedef hash (target_hash) değerine karşılık gelen parolayı bulur.
    :param target_hash: Kırılması istenen hash (string)
    :param rainbow_table: Rainbow table (hash değeri -> parola) (dict)
    :return: Parola bulunduysa string, bulunamadıysa None
    """
    return rainbow_table.get(target_hash, None)


if __name__ == "__main__":
    # Örnek: 'password123' parolasının md5 hash'i
    password = 'password123'
    target_hash = hashlib.md5(password.encode()).hexdigest()
    # Basit bir sözlük
    wordlist = ['123456', 'password', 'admin', 'password123', 'letmein']
    rainbow_table = generate_rainbow_table(wordlist, lambda s: hashlib.md5(s.encode()).hexdigest())
    print(f"Hedef hash: {target_hash}")
    result = crack_using_rainbow_table(target_hash, rainbow_table)
    if result:
        print(f"Parola bulundu: {result}")
    else:
        print("Parola bulunamadı.") 