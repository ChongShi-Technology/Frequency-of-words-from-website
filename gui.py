#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "ChongShi Technology"

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Frequency_words(QtGui.QWidget):

    def __init__(self):
        super(Frequency_words, self).__init__()

        self.initUI()

    def initUI(self):
        # the website
        website = QtGui.QLabel('the website you want to analyse')
        websiteEdit = QtGui.QLineEdit()
        website_button = QtGui.QPushButton('analyse', self)
        website_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connect(website_button, QtCore.SIGNAL('clicked()'),
            self.showDialog)
        self.setFocus()

        # the top number
        number = QtGui.QLabel('top number words you want to get')
        numberEdit = QtGui.QLineEdit()
        number_button = QtGui.QPushButton('submit', self)
        number_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connect(number_button, QtCore.SIGNAL('clicked()'),
            self.showDialog)
        self.setFocus()

        # the frequency of word
        word = QtGui.QLabel('get the frequency of the word')
        wordEdit = QtGui.QLineEdit()
        word_button = QtGui.QPushButton('submit', self)
        word_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connect(word_button, QtCore.SIGNAL('clicked()'),
            self.showDialog)
        self.setFocus()


        grid = QtGui.QGridLayout()
        grid.setSpacing(6)

        grid.addWidget(website, 1, 0)
        grid.addWidget(websiteEdit, 2, 0)
        grid.addWidget(website_button, 2, 1)

        grid.addWidget(number, 3, 0)
        grid.addWidget(numberEdit, 4, 0)
        grid.addWidget(number_button, 4, 1)

        grid.addWidget(word, 5, 0)
        grid.addWidget(wordEdit, 6, 0)
        grid.addWidget(word_button, 6, 1)

        self.setLayout(grid)


        self.setWindowTitle('Frequency analyse')
        self.setGeometry(300, 300, 500, 200)


    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')

        if ok:
            self.label.setText(str(text))



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Frequency_words()
    ex.show()
    app.exec_()