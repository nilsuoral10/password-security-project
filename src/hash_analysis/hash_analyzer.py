import hashlib

def compute_hash(password, hash_algo='md5'):
    """
    Belirtilen parola (password) için, seçilen hash algoritması (hash_algo) kullanarak hash değerini hesaplar.
    :param password: Parola (string)
    :param hash_algo: Hash algoritması (string, örneğin 'md5', 'sha1', 'sha256')
    :return: Hash değeri (string)
    """
    if hash_algo == 'md5':
        h = hashlib.md5(password.encode()).hexdigest()
    elif hash_algo == 'sha1':
        h = hashlib.sha1(password.encode()).hexdigest()
    elif hash_algo == 'sha256':
        h = hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Desteklenmeyen hash algoritması: " + hash_algo)
    return h


def compute_hash_with_salt(password, salt, hash_algo='md5'):
    """
    Belirtilen parola (password) ve salt (salt) kullanarak, seçilen hash algoritması (hash_algo) ile hash değerini hesaplar.
    :param password: Parola (string)
    :param salt: Salt (string)
    :param hash_algo: Hash algoritması (string, örneğin 'md5', 'sha1', 'sha256')
    :return: Hash değeri (string)
    """
    salted_password = password + salt
    return compute_hash(salted_password, hash_algo)


if __name__ == "__main__":
    # Örnek: 'password123' parolası için MD5, SHA-1 ve SHA-256 hash değerlerini hesapla
    password = 'password123'
    print("Parola: " + password)
    print("MD5 hash (salt olmadan): " + compute_hash(password, 'md5'))
    print("SHA-1 hash (salt olmadan): " + compute_hash(password, 'sha1'))
    print("SHA-256 hash (salt olmadan): " + compute_hash(password, 'sha256'))

    # Örnek: 'password123' parolasına 'mysalt' salt ekleyerek MD5 hash değerini hesapla
    salt = 'mysalt'
    print("Salt: " + salt)
    print("MD5 hash (salt ile): " + compute_hash_with_salt(password, salt, 'md5')) 