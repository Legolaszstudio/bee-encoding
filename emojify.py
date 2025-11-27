import sys




EMOJI_OFFSET = 0x1F300

def encrypt_to_emojis(text: str) -> str:
    """
    Encrypts a string into a string of emojis.
    
    Strategy:
    1. Convert the input string to UTF-8 bytes.
    2. Map each byte (0-255) to a Unicode emoji codepoint by adding an offset.
    """
    if not text:
        return ""
    
    
    
    byte_data = text.encode('utf-8')
    
    
    emoji_chars = []
    for byte in byte_data:
        
        emoji_codepoint = EMOJI_OFFSET + byte
        emoji_chars.append(chr(emoji_codepoint))
        
    return "".join(emoji_chars)

def decrypt_from_emojis(emoji_text: str) -> str:
    """
    Decrypts a string of emojis back to the original text.
    
    Strategy:
    1. Convert each emoji character back to its integer codepoint.
    2. Subtract the offset to recover the original byte value.
    3. Decode the resulting bytes as UTF-8.
    """
    if not emoji_text:
        return ""
        
    byte_array = bytearray()
    
    for char in emoji_text:
        codepoint = ord(char)
        
        
        original_byte = codepoint - EMOJI_OFFSET
        
        
        if 0 <= original_byte <= 255:
            byte_array.append(original_byte)
        else:
            
            
            
            raise ValueError(f"Character '{char}' is not a valid encrypted emoji in this scheme.")
    
    
    try:
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        return "[Error: Decrypted bytes are not valid UTF-8. Was the input text corrupted?]"

def main():
    """
    Simple demonstration of the cipher.
    """
    print("--- Emoji Cipher Demo ---")
    
    
    original_text = "Hello World!"
    encrypted = encrypt_to_emojis(original_text)
    decrypted = decrypt_from_emojis(encrypted)
    
    print(f"\nOriginal:  {original_text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    
    
    complex_text = "Python is cool 🐍 €100" 
    encrypted_complex = encrypt_to_emojis(complex_text)
    decrypted_complex = decrypt_from_emojis(encrypted_complex)
    
    print(f"\nOriginal:  {complex_text}")
    print(f"Encrypted: {encrypted_complex}")
    print(f"Decrypted: {decrypted_complex}")

if __name__ == "__main__":
    main()