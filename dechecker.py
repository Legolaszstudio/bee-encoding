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