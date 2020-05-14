APA FORMATTING TOOL
By: Kojo Nyarku Baidoo; 69092023; Cohort B
======================================================================================================
REQUIREMENTS
PyQt5==5.14.2
PyQt5-sip==12.7.2

======================================================================================================
SETUP:
pip3 install -y -r requirements.txt
======================================================================================================
CLEAN UP:
pip3 uninstall -y -r requirements.txt
======================================================================================================
DESCRIPTION:
A tool for generating APA style references for webpages, online articles and books.
======================================================================================================
USAGE:
1.Enter information about the source, with the appropriate preprocessing guidlines stated below, in the appropriate file.
2.Run format.py.
3.Check the box next to the references you want to generate.
4.Click the "Format" button.
5.Locate your APA formatted references in the newly generated formatted_{source}.txt file.
======================================================================================================

PREPROCESSING:
1. One source per line
2. All information is separated using commas

<ONLINE ARTICLES>
FILE:	unformatted_articles.txt
FORMAT: {number of authors}, {author names}, {date: dd-mm-yyyy}, {article title}, {title of periodical}, {article volume number}, {issue number}, {url}
EXAMPLE:1,Dieter Bohn,12-02-2020,Samsung's Galaxy Z Flip beats the Motorola Razr in nearly every way,The Verge,12,14,https://www.theverge.com/2020/2/12/21134261/samsung-galaxy-z-flip-vs-motorola-razr-folding-flip-phone-camera-battery-processor

<BOOKS>
FILE:	unformatted_books.txt
FORMAT: {number of authors}, {author names}, {book title}, {Year of publication: yyyy}, {Location of publication}, {Publisher name}
EXAMPLE:1,George Orwell,Animal farm,1989,Blairgowrie,Guidlines

<WEBPAGES>
FILE:	unformatted_webpages.txt
FORMAT: {number of authors}, {author names}, {site name}, {page title}, {upload/recent edit date: dd-mm-yyyy}, {url}
EXAMPLE:1,Devon Price,Medium,Laziness Does not Exist,23-03-2018,https://humanparts.medium.com/laziness-does-not-exist-3af27e312d01
======================================================================================================
