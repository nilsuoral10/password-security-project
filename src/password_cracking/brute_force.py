import itertools
import string

def brute_force_crack(target_hash, hash_func, max_length=4, charset=string.ascii_lowercase):
    """
    Basit brute force parola kırıcı.
    :param target_hash: Kırılması istenen hash (string)
    :param hash_func: Hash fonksiyonu (örn: lambda s: hashlib.md5(s.encode()).hexdigest())
    :param max_length: Maksimum parola uzunluğu
    :param charset: Kullanılacak karakter seti
    :return: Parola bulunduysa string, bulunamadıysa None
    """
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_str = ''.join(guess)
            if hash_func(guess_str) == target_hash:
                return guess_str
    return None

if __name__ == "__main__":
    import hashlib
    # Örnek: 'abc' parolasının md5 hash'i
    password = 'abc'
    target_hash = hashlib.md5(password.encode()).hexdigest()
    print(f"Hedef hash: {target_hash}")
    result = brute_force_crack(target_hash, lambda s: hashlib.md5(s.encode()).hexdigest(), max_length=4)
    if result:
        print(f"Parola bulundu: {result}")
    else:
        print("Parola bulunamadı.") 