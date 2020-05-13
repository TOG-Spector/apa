import sys
import main
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


def window():
    global widget
    global book
    global web
    global article
    
    app = QApplication(sys.argv)
    widget = QWidget()
    
    book = QCheckBox('Books',widget)
    book.move(60,10)

    article = QCheckBox('Articles',widget)
    article.move(60,35)

    web = QCheckBox('Webpages',widget)
    web.move(60,60)

    button = QPushButton("Format",widget)
    button.clicked.connect(click)
    button.resize(70,30)
    button.move(150,100)

    widget.setGeometry(700,400,350,200)
    widget.setWindowTitle("APA PRO")
    widget.show()
    sys.exit(app.exec_())

def click():
    if book.isChecked():
        book_format()
        book.toggle()
        
    if article.isChecked():
        article_format()
        article.toggle()
        
    if web.isChecked():
        web_format()
        web.toggle()

def book_format():
    main.books()
    
def article_format():
    main.articles()
    
def web_format():
    main.webpages()
    
window()
