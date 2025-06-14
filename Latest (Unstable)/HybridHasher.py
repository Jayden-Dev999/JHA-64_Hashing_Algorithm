
import hashlib
from argon2 import PasswordHasher
import bcrypt

def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_argon2(password):
    ph = PasswordHasher()
    return ph.hash(password)

def hash_bcrypt(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def full_hybrid_hash(password):
    sha256_result = hash_sha256(password)
    argon2_result = hash_argon2(sha256_result)
    bcrypt_result = hash_bcrypt(argon2_result)
    return {
        "SHA-256": sha256_result,
        "Argon2 of SHA-256": argon2_result,
        "bcrypt of Argon2": bcrypt_result
    }

def main():
    print("🔐 Hybrid Hash Generator")
    print("1 - SHA-256")
    print("2 - Argon2")
    print("3 - bcrypt")
    print("4 - Full Hybrid")
    choice = input("Choose an option (1-4): ")
    password = input("Enter password to hash: ")

    if choice == "1":
        print("\n[SHA-256]\n", hash_sha256(password))
    elif choice == "2":
        print("\n[Argon2]\n", hash_argon2(password))
    elif choice == "3":
        print("\n[bcrypt]\n", hash_bcrypt(password))
    elif choice == "4":
        results = full_hybrid_hash(password)
        for name, value in results.items():
            print(f"\n[{name}]\n{value}")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
