COUNT = 256


def encrypt(symbol, key):
    c = (symbol + key) % COUNT
    return c


def decrypt(symbol, key):
    c = (symbol - key) % COUNT
    return c


def encrypt_data(data, key):
    cypher_data = []
    for symbol in data:
        encrypted_symbol = encrypt(symbol, key)
        cypher_data.append(encrypted_symbol)
    return cypher_data


def decrypt_data(data_c, key):
    data = []
    for symbol in data_c:
        m = decrypt(symbol, key)
        data.append(m)
    return data
