from PIL import Image
import PIL.ImageOps
import os

import PIL
def encrypt_image(input_img_path, data_to_encrypt, output_img_path):
    if not output_img_path.lower().endswith('.png'):
        raise ValueError("Output file must be a .png file to preserve hidden data.")
    
    image = Image.open(input_img_path).convert("RGB")
    new_image = image.copy()
    
    
    data_bytes = data_to_encrypt.encode('utf-8')
    
    
    data_bin_list = [format(b, '08b') for b in data_bytes]
    data_len = len(data_bin_list)
    
    
    image_data = iter(new_image.getdata())
    
    width = new_image.size[0]
    (x, y) = (0, 0)
    for i in range(data_len):
        
        pixels = [value for value in image_data.__next__()[:3] +
                                     image_data.__next__()[:3] +
                                     image_data.__next__()[:3]]
        
        
        for j in range(8):
            if (data_bin_list[i][j] == '0') and (pixels[j] % 2 != 0):
                pixels[j] -= 1
            elif (data_bin_list[i][j] == '1') and (pixels[j] % 2 == 0):
                if pixels[j] != 0:
                    pixels[j] -= 1
                else:
                    pixels[j] += 1 
        
        
        
        if (i == data_len - 1):
            if (pixels[-1] % 2 == 0):
                if pixels[-1] != 0:
                    pixels[-1] -= 1
                else:
                    pixels[-1] += 1
        else:
            if (pixels[-1] % 2 != 0):
                pixels[-1] -= 1
        
        pixel_sets = [tuple(pixels[0:3]), tuple(pixels[3:6]), tuple(pixels[6:9])]
        
        for pixel in pixel_sets:
            new_image.putpixel((x, y), pixel)
            if (x == width - 1):
                x = 0
                y += 1
            else:
                x += 1
    new_image = PIL.ImageOps.invert(new_image)
    new_image.save(output_img_path)
    print(f"Data encrypted successfully into {output_img_path}")

def decrypt_image(input_img_path):
    image = Image.open(input_img_path).convert("RGB")
    image = PIL.ImageOps.invert(image)
    image_data = iter(image.getdata())
    
    extracted_bytes = bytearray()
    while True:
        
        try:
            pixels = [value for value in image_data.__next__()[:3] +
                                         image_data.__next__()[:3] +
                                         image_data.__next__()[:3]]
        except StopIteration:
            break
        binary_str = ''
        
        
        for i in pixels[:8]:
            if i % 2 == 0:
                binary_str += '0'
            else:
                binary_str += '1'
        
        extracted_bytes.append(int(binary_str, 2))
        
        
        
        if pixels[-1] % 2 != 0:
            break
            
    
    try:
        return extracted_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return f"Error decoding text: {extracted_bytes}"