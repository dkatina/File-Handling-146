

#-- Extracting List data

# flowers = []
# with open('garden.txt', 'r') as file:
#     for line in file:
#         flowers.append(line.strip()) #default removes whitespace \t \n

# print(flowers)


#-- Extracting Dictionary Data
golf_clubs = {}

with open('golf_bag.txt', 'r') as file:
    for line in file:
        club, brand = line.strip().split(': ')
        golf_clubs[club] = brand

print(golf_clubs)

#-- Extracting Denser Data

def read_books():
    books = {}
    with open('books.txt', 'r') as file:
        for line in file:
            title, author, genre, desc = line.strip().split('-:-')
            books[title] = {'Author': author, 'Genre': genre, 'Desc': desc}
    return books


def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")


#Utilizing our read and write functions to extract data, change the data, overwrite the previous data
def edit_book():
    books = read_books() #grab books from local file
    title = input('What book do you want to change? ')
    if title in books:
        desc = input('Give a new description: ')
        books[title]['Desc'] = desc
        add_books(books)

edit_book()






