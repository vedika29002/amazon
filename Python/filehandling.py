books=open('library.text',"w")
print("file created")
print("file name:",books.name)
print("mode of file:",books.mode)
print("can i write in file:",books.writable())
print("can i read file:",books.readable())
books=open('library.text',"r")
print("can i write in file:",books.writable())
print("can i read file:",books.readable())
print("can i close the file:",books.closed)
books.close()
print("can i close the file:",books.closed)
print("can i write in file:",books.writable())



books=open('library.txt', "w")
books.write("Hello-1\n")
books.write("Hello-2\n")
books.write("Hello-3\n")
books.write("Hello-4\n")
print("added content")

books.writelines("Welcome")
print(books)

books=open('library.txt', "r")
print(books.read())

import os

if os.path.exists('library.txt'):
    print("file esixts")
else:
    print("file not exists")