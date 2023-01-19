 
with open('books.txt','rt') as f:
    data = f.read()

    name=input('Enter the old word: ')
    name1=input('Enter new word: ')
    
    data = data.replace(name, name1)
with open('books.txt','wt') as f:    
    f.write(data)
 