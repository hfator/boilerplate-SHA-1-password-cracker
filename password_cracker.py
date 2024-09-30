import hashlib


def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt", "r") as pass_file:
        passwords = [line.strip() for line in pass_file]

    if use_salts:
        with open("known-salts.txt", "r") as salt_file:
            salts = [line.strip() for line in salt_file]

        for password in passwords:
            for salt in salts:
                if hashlib.sha1((password + salt).encode()).hexdigest() == hash:
                    return password
                elif hashlib.sha1((salt + password).encode()).hexdigest() == hash:
                    return password

    else:
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password
    return "PASSWORD NOT IN DATABASE"
