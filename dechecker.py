def decrypt_checkered(line1, line2):
    evens = line1[1::2]
    odds = line2[1::2]
    
    decrypted = []
    
    for i in range(len(odds)):
        decrypted.append(evens[i])
        decrypted.append(odds[i])
        
    if len(evens) > len(odds):
        decrypted.append(evens[-1])
        
    return "".join(decrypted)

""" original_text = "HELLO WORLD"

encrypted_row_1 = " H L O W R D"
encrypted_row_2 = " E L   O L"

result = decrypt_checkered(encrypted_row_1, encrypted_row_2)

print(f"Row 1: '{encrypted_row_1}'")
print(f"Row 2: '{encrypted_row_2}'")
print(f"Decrypted: '{result}'") """