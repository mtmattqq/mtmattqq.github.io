import os

print('Enter File Name')
file_name = input()

file = open(os.path.join(os.getcwd(), 'source', '_posts', file_name), 'r', encoding = "utf-8")
text = file.read()
file.close()

output_text = ''
is_talking = False
quote_mark = ['「', '」']
for ch in text :
    if ch.encode() == "\'".encode() :
        output_text += quote_mark[is_talking]
        is_talking = not is_talking
    else :
        output_text += ch
    # print(ch.encode() == "\'".encode())

file = open(os.path.join(os.getcwd(), 'source', '_posts', file_name), 'w', encoding = "utf-8")
file.write(output_text)
file.close()