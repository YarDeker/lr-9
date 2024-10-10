def Open(file_name, mode):
    try: file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        return file

def process_files(input_file, output_file, temp_file):
    digits = []
    other_chars = []

    file_input_r = Open(input_file, 'r')
    if file_input_r == None: return 

    for line in file_input_r:
        for char in line:
            if char.isdigit():
                digits.append(char)
            elif char.isalpha() or not char.isspace():
                other_chars.append(char)

    file_temp_w = Open(temp_file, 'w')
    if file_temp_w != None:
        file_temp_w.write(''.join(digits) + ''.join(other_chars))
        file_temp_w.close()

    file_temp_r = Open(temp_file, 'r')
    file_out_w = Open(output_file, 'w')

    content = file_temp_r.read()
    for i in range(0, len(content), 10):
        file_out_w.write(content[i:i+10] + '\n')

    file_input_r.close()
    file_temp_r.close()
    file_out_w.close()

def start():
    file1_name = "TF17_1.txt"
    file2_name = "TF17_2.txt"
    file3_name = "TF17_3.txt"

    lines = [
        "Hello 123",
        "Wor ld456",
        "Python__789",
        "D ata!001"
    ]

    file1_w = Open(file1_name, 'w')
    if file1_w != None:
        for line in lines:
            file1_w.write(f"{line}\n")
        file1_w.close()

    process_files(file1_name, file2_name, file3_name)

    print("Вміст файлу TF17_2:")
    file_r = Open(file2_name, 'r')
    if file_r != None:
        for line in file_r:
            print(line.strip())
        file_r.close()

start()
