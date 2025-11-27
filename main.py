import emojify
import json

f = open("input.json", "r", encoding="utf-8")
data = f.read()
json_data = json.loads(data)
f.close()

print(json_data)
output_lines = []
for key, value in json_data.items():
    if isinstance(value, str):
        value = value.replace("\"", "According to all known laws of aviation,there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.⛄")
        value = value.replace("int", "According to all known laws of aviation,there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.☃︎")
        key = key.replace("\"", "According to all known laws of aviation,there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.⛄")
        key = key.replace("int", "According to all known laws of aviation,there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.☃︎")
    output = ""
    if isinstance(value, str):
        output = f'The key "{key}" is a string with the value of "{value}" which is {len(value)} chars'
    elif isinstance(value, int):
        divisibility = "divisible by 2" if value % 2 == 0 else "NOT divisible by 2"
        output = f'The key "{key}" is an int with the value of {value} which is {divisibility}'
    else:
        output = f'The key "{key}" has a value of type {type(value).__name__}'
        
    # Create a checkered pattern in the output (One line is in two, one char at first line, the next in second)
    checkered_output = [
        "",
        "",
    ]
    for i, char in enumerate(output):
        if i % 2 == 0:
            checkered_output[0] += " " + char
        else:
            checkered_output[1] += " " + char
    checkered_output[0] = emojify.encrypt_to_emojis(checkered_output[0])
    checkered_output[1] = emojify.encrypt_to_emojis(checkered_output[1])
    output_lines.extend(checkered_output)

f = open("out.bee", "w", encoding="utf-8")
f.write("\n".join(output_lines))
f.close()
    
import steg
steg.encrypt_image("bee_image.jpg", "\n".join(output_lines), "out.png")

