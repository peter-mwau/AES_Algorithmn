import gradio as gr
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)  # Generate a random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv.hex() + ciphertext.hex()


def decrypt(ciphertext, key):
    try:
        iv = bytes.fromhex(ciphertext[:32])  # Extract the IV from the ciphertext
        ciphertext = bytes.fromhex(ciphertext[32:])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        unpadded = unpad(decrypted, AES.block_size)
        return unpadded.decode()
    except (ValueError, IndexError):
        return "Decryption failed. Please check the ciphertext and key."


def aes_cipher(text, key, mode):
    key = key.encode()  # Encode key as byte string
    result = ""

    if mode == "Encrypt":
        result = encrypt(text, key)
    elif mode == "Decrypt":
        result = decrypt(text, key)
    else:
        print('Invalid mode:', mode)

    return result


iface = gr.Interface(
    fn=aes_cipher,
    inputs=[
        "text",
        "text",
        gr.inputs.Radio(["Encrypt", "Decrypt"], label="Mode")
    ],
    outputs="text",
    title="AES Encryption/Decryption",
    description="Enter the text and key to perform AES encryption or decryption.",
    examples=[
        ["Hello World!", get_random_bytes(16).hex(), "Encrypt"],
        ["2f89f30e4ea8f8f77f7bce0e6a1d4b1b", get_random_bytes(16).hex(), "Decrypt"],
    ]
)

iface.launch()
