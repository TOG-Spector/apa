import sys
import time
import apa
import os

def begin():
    print('Welcome to my automatic APA formatting program.\nWe all know after that citation master quiz you did not remeber jack.\nFear no more Jeffrey has got your back.')
    options = {'(1)':'Article','(2)':'Webpage','(3)':'Book','(4)':'Quit'}

    for x in options:
        print(f"{x}:{options[x]}")
    choice = input('What is your choice?: ')

    if choice == '4':
        print('\nExiting...')
        time.sleep(2)
        try:
            os.system('clear')
        except:
            os.system('cls')
        sys.exit()
    elif choice == '1':
        print(f"\nReference: {choice1()}")
    elif choice == '2':
        print(f"\nReference: {choice2()}")
    elif choice == '3':
        choice3()
        #print(f"\nReference: {choice3()}")
    else:
        print("Invalid Input, press any key to reselect")
        input()
        begin()

#function for processing author names
def author_info(number,author_list):
    names = []
    for x in range(int(number)):
        names.append(author_list[x+1])
    for y in range(int(number)):
        author_list.pop(author_list.index(author_list[1]))
    author_list.pop(0)

    return names
    '''
def author_info():
    authors = input('How many authors?: ')
    names = []
    for x in range(int(authors)):
        names.append(input(f"author number {x}: "))
    return names
    '''

#article option
def choice1():
    author = author_info()
    title_of_article = input("Title of the article: ")
    title_of_periodical = input("Name of periodical: ")
    date = input("Date of publication(dd-mm-yyyy): ")
    volume_number = input("Volume number: ")
    issue_number = input("Issue number: ")
    url = input("Url: ")
    kojo = apa.Apa()
    return kojo.article(author,date,title_of_article,title_of_periodical,volume_number,issue_number,url)
    '''
    title
    author
    publication_date
    periodical title'
    volume number
    issue number
    url
    '''
#book option
def choice3():
    source = open("book.txt","r")
    destination = open("bookref.txt","w")
    for line in source:
        stuff = line.split(',')
        author = author_info(stuff[0],stuff)
        title = stuff[0]
        year = stuff[1]
        location = stuff[2]
        publisher = stuff[3]
        kojo = apa.Apa()
        destination.write(kojo.book(author,title,year,location,publisher))

    source.close()
    destination.close()

    '''
    author = author_info()
    title = input("Title of the book: ")
    year = input("Year of publication: ")
    location = input("Location of publication: ")
    publisher = input("Publisher: ")
    kojo = apa.Apa()
    return kojo.book(author,title,year,location,publisher)
    '''
    '''
    title
    author
    year
    location
    publisher
    '''
#webpage
def choice2():
    print('choice 2 working')
    '''
    author
    date
    site_name
    url
    title
    '''

begin()
