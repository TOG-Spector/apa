import apa

#function for processing author names
def author_info(number,author_list):
    names = []
    for x in range(int(number)):
        names.append(author_list[x+1])
    for y in range(int(number)):
        author_list.pop(author_list.index(author_list[1]))
    author_list.pop(0)

    return names

#article option
def articles():
    try:
        source = open("unformatted_articles.txt","r")
        destination = open("formatted_articles.txt","w")
    except:
        exit(1)
    for line in source:
        source_info = line.split(',')
        author = author_info(source_info[0],source_info)
        date = source_info[0]
        title = source_info[1]
        periodical = source_info[2]
        volume_number = source_info[3]
        issue_number = source_info[4]
        url = source_info[-1]
        kojo = apa.Apa()
        destination.write(kojo.article(author,date,title,periodical,volume_number,issue_number,url))
    
    source.close()
    destination.close()


#book option
def books():
    try:
        source = open("unformatted_books.txt","r")
        destination = open("formatted_books.txt","w")
    except:
        exit(1)
    for line in source:
        source_info = line.split(',')
        author = author_info(source_info[0],source_info)
        title = source_info[0]
        year = source_info[1]
        location = source_info[2]
        publisher = source_info[-1]
        kojo = apa.Apa()
        destination.write(kojo.book(author,title,year,location,publisher))

    source.close()
    destination.close()


#webpage
def webpages():
    try:
        source = open("unformatted_webpages.txt","r")
        destination = open("formatted_webpages.txt","w")
    except:
        exit(1)
    for line in source:
        source_info = line.split(',')
        author = author_info(source_info[0],source_info)
        title = source_info[1]
        name  = source_info[0]
        date = source_info[2]
        url = source_info[-1]
        kojo = apa.Apa()
        destination.write(kojo.webpage(author,date,title,name,url))

    source.close()
    destination.close()
