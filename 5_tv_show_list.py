import re
import os
#Store a list of tv shows, that we can add to, remove from, and store locally
#be able to show your shows


#re for the fun of it

def read_shows():
    shows_list = []
    try:
        with open('shows_list.txt', 'r') as file:
            for line in file:
                data = re.search(r'([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)', line)
                shows_list.append({'Title': data.group(1), 'W2W': data.group(2), 'Genre': data.group(3).strip()})
    except FileNotFoundError:
        print('No Local files')
        return []
    else:
        print('Importing Local Data...')
        return shows_list



#[{'Title': title, 'W2W': platform, 'Genre': genre}]

def write_shows(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['W2W']}-:-{show['Genre']}\n")


def add_show(shows):
    os.system('cls')
    title = input('Title: ')
    platform = input('Where can you stream this? ')
    genre = input('Genre: ')
    shows.append({'Title': title, 'W2W': platform, 'Genre': genre})
    write_shows(shows)
    print(f'Added {title} to your list')

def view(shows):
    os.system('cls')
    print('Shows List')
    print('------------')
    for idx, show in enumerate(shows):
        print(f"{idx+1}.) {show['Title']} is a {show['Genre']} show on {show['W2W']}")

def remove_show(shows):
    view(shows)
    option = int(input("Select the number of the show you want to remove: "))
    show = shows.pop(option-1)
    print(f"Removed {show['Title']}!")
    write_shows(shows)




def runner():
    shows_list = read_shows() #add local data search
    while True:
        action = input('''
Options
--------------                       
1.) Add Show
2.) Remove Show
3.) View List
4.) Quit
> ''')
        if action == '1':
            add_show(shows_list)
        elif action == '2':
            remove_show(shows_list)
        elif action == '3':
            view(shows_list)
        elif action == '4':
            break
        else:
            print('Invalid Selection Dingus, Try Again!')

runner()
