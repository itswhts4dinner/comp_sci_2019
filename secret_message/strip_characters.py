line = "My sentence! Is awesome?"
for char in line:
    if char in " ?.!/;:":
        line = line.replace(char,'')
print(line)
