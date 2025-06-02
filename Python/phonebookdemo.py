import os

filename=input('enter filename=')
if os.path.exists(filename):
    print("file already exists so can't create again")
else:
    with open(filename,'w')as fp:
        count=int(input('enter count for adding name and number='))
        phonebook=[]
        for i in range(count):
            name=input('enter name=')
            mobile=int(input('enter mobile='))
            data={'name':name,'mobile':mobile}
            phonebook.append(data)
        fp.write(str(phonebook))
        fp=open(filename,'r')
        print("My phonebook")
        print(fp.read())