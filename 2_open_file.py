

#Write to a file

file = open('new_file.txt', 'w')
file.write('writing to a file from python!') #use .write() method to write to a file

file.close() #This ensures the data gets commited, and keeps your computer from harm



#Overwriting Files
file = open('new_file.txt', 'w')
file.write('Overwriting previous data\n') # \n format new entry with a new line 
file.close()


#adding to a file (without overwriting)

file = open('new_file.txt', 'a')
file.write('Adding to my file with "a" mode\n') # .write() when in 'a' mode appends without overwriting
file.close()


#reading files

file = open('new_file.txt', 'r')
content = file.read() #returns a large string of the entire text
#lines = file.readlines() #returns a list of items defined by new lines
file.close()
print(content)


#-- with : allows us to open files to a codeblock and automatically close files
#when the codeblock is exited

with open('new_file.txt', 'r') as file:
    for line in file:
        print(line.strip()) #removes the \n from the end of each line


#-- Store Data from a list

flowers = ['Wysteria', 'Sun Flowers', 'Orchids', 'Marigold']
with open('garden.txt', 'w') as file:
    for flower in flowers:
        file.write(flower + '\n')



#-- Storing Dictionary Data

clubs = {'Driver': 'Cobra', 'Irons': 'Sirixon', 'Hyrbid': 'Callaway', 'Putter': 'Ping'}

with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f'{club}: {brand}\n')


#-- Storing Book
#{ title: {author: name, genre: name, desc: summary}, }


books = {
    'Green Lights': {'Author': 'Mathew McConaughey', 'Genre': 'Biography', 'Desc': 'I really, love this Book and stuff'},
    'More than A Carpenter': {'Author': 'Josh McDowell', 'Genre': 'Christian Literature', 'Desc': 'I really, love this Book and stuff'},
    'Diary of A Wimpy Kid' : {'Author': 'Jeff Kiney', 'Genre': 'YAF', 'Desc': 'A tale of a wimpy kid'},
    'Black Flags': {'Author': 'Joby Ray', 'Genre': 'Nonfiction', 'Desc': 'Potentially, this is a story about pirates?'}
}

def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")

add_books(books)

