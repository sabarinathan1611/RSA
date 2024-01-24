import rsa

def generate_key_pair():

    public_key, private_key = rsa.newkeys(512)
    return public_key, private_key

def encrypt_message(message, public_key):

    encrypted_message = rsa.encrypt(message.encode('utf-8'), public_key)
    return encrypted_message

def decrypt_message(encrypted_message, private_key):

    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode('utf-8')
    return decrypted_message

if __name__ == "__main__":

    public_key, private_key = generate_key_pair()

  
    original_message = " RSA encryption and decryption!"

  
    encrypted_message = encrypt_message(original_message, public_key)
    print(f"Original Message: {original_message}")
    print(f"Encrypted Message: {encrypted_message}")

 
    decrypted_message = decrypt_message(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")
