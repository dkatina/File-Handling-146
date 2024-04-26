#Files have a pointer that tell us where we are in the file

with open('new_file.txt', 'a+') as file:
    file.write('Adding something totally new\n')
    print(file.tell()) # returns the index of the pointer
    file.seek(0)
    content = file.read()
    print(content)
