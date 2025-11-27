import sys

# We pick a starting offset in the Unicode Emoji block.
# 0x1F300 corresponds to "Cyclone" (🌀).
# This block (Miscellaneous Symbols and Pictographs) is fairly contiguous.
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
    
    # 1. Encode to UTF-8 bytes
    # Examples: 'A' -> b'\x41', '€' -> b'\xe2\x82\xac'
    byte_data = text.encode('utf-8')
    
    # 2. Convert bytes to emojis
    emoji_chars = []
    for byte in byte_data:
        # We simply add the byte value to our base emoji offset
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
        
        # Reverse the math: Codepoint - Offset = Byte
        original_byte = codepoint - EMOJI_OFFSET
        
        # Validation: Ensure the result is a valid byte (0-255)
        if 0 <= original_byte <= 255:
            byte_array.append(original_byte)
        else:
            # If we encounter a character that isn't part of our cipher scheme,
            # we can either ignore it or raise an error. Here we define a placeholder
            # or simply skip. For strictness, let's raise a helpful error.
            raise ValueError(f"Character '{char}' is not a valid encrypted emoji in this scheme.")
    
    # 3. Decode back to string
    try:
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        return "[Error: Decrypted bytes are not valid UTF-8. Was the input text corrupted?]"

def main():
    """
    Simple demonstration of the cipher.
    """
    print("--- Emoji Cipher Demo ---")
    
    # Test 1: Simple ASCII
    original_text = "Hello World!"
    encrypted = encrypt_to_emojis(original_text)
    decrypted = decrypt_from_emojis(encrypted)
    
    print(f"\nOriginal:  {original_text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Test 2: Complex UTF-8 (symbols and other languages)
    # '€' is 3 bytes, so it will become 3 emojis.
    complex_text = "Python is cool 🐍 €100" 
    encrypted_complex = encrypt_to_emojis(complex_text)
    decrypted_complex = decrypt_from_emojis(encrypted_complex)
    
    print(f"\nOriginal:  {complex_text}")
    print(f"Encrypted: {encrypted_complex}")
    print(f"Decrypted: {decrypted_complex}")

if __name__ == "__main__":
    main()