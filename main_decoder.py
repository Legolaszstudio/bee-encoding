
import dechecker
import steg

# -----------------------------------
checkered_input = steg.decrypt_image("out.png")
print(checkered_input)

lines = checkered_input.split("\n")
# -----------------------------------

decheckered_lines = []
for i in range(0, len(lines), 2):
    decrypted_line = dechecker.decrypt_checkered(lines[i], lines[i+1])
    decheckered_lines.append(decrypted_line)

out = {}
for line in decheckered_lines:
    line.strip()
    line = line.replace("\n", "")
    key = line.split("\"")[1]
    if line.__contains__("int"):
      value = int(line.split(" ")[10])
    else:
      value = line.split("\"")[3]
    out[key] = value
print(out)

  