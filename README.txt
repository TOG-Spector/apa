APA FORMATTING TOOL
By: Kojo Nyarku Baidoo; 69092023; Cohort B
======================================================================================================
REQUIREMENTS
PyQt5==5.14.2
PyQt5-sip==12.7.2

======================================================================================================
SETUP:
pip3 install -r requirements.txt
======================================================================================================
CLEAN UP:
pip3 uninstall -y -r requirements.txt
======================================================================================================
DESCRIPTION:
A tool for generating APA style references for webpages, online articles and books.
Enter information about the source, with the appropriate preprocessing guidlines stated below, in the appropriate file.
======================================================================================================
PREPROCESSING:
1. One source per line
2. All information is separated using commas

<ONLINE ARTICLES>
File:	unformatted_articles.txt
Format: {number of authors}, {comma separated author names}, {date: dd-mm-yyyy}, {article title}, {title of periodical}, {article volume number}, {issue number}, {url}
Eg: 	1,Dieter Bohn,12-02-2020,Samsung's Galaxy Z Flip beats the Motorola Razr in nearly every way,The Verge,12,14,https://www.theverge.com/2020/2/12/21134261/samsung-galaxy-z-flip-vs-motorola-razr-folding-flip-phone-camera-battery-processor

<BOOKS>
File:	unformatted_books.txt
Format: {number of authors}, {comma separated author names}, {book title}, {Year of publication: yyyy}, {Location of publication}, {Publisher name}
Eg: 	1,George Orwell,Animal farm,1989,Blairgowrie,Guidlines

<WEBPAGES>
File:	unformatted_webpages.txt
Format: {number of authors}, {comma separated author names}, {site name}, {page title}, {upload/recent edit date: dd-mm-yyyy}, {url}
Eg: 	1,Devon Price,Medium,Laziness Does not Exist,23-03-2018,https://humanparts.medium.com/laziness-does-not-exist-3af27e312d01
======================================================================================================
