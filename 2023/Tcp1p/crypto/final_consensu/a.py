import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, AES.block_size)

def receive_data(sock):
    data = b""
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            break
        data += chunk
    return data

def main():
    server_address = ('ctf.tcp1p.com', 35257)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_address)

    data = receive_data(s)
    print(data.decode())

    for _ in range(2):
        s.send(b"A" * 15 + b"\n")
        data = receive_data(s)
        print(data.decode())

    double_encrypted_flag = data.decode().strip().split()[-1]
    flag = bytes.fromhex(double_encrypted_flag)

    key_a = b""  # Define the key-a here
    key_b = b""  # Define the key-b here

    decrypted_flag = decrypt(flag, key_b)
    decrypted_flag = decrypt(decrypted_flag, key_a)

    print("Decrypted Flag:", decrypted_flag.decode())

    s.close()

if __name__ == '__main__':
    main()
