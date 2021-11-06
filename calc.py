from PyQt6 import QtCore, QtGui, QtWidgets, uic
from numpy import *
from math import *
import sys
import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('calculator.ui', self)
        self.setFixedSize(452, 588)
    

    def press_one(self):
         # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}1')   
    
    def press_two(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}2')
    
    def press_tree(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}3')
    
    def press_four(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}4')
    
    def press_five(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}5')
    
    def press_six(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}6')
    
    def press_seven(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}7')
    
    def press_eight(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}8')

    def press_nine(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}9')
    
    def press_zero(self):
            # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}0')
    
    def press_C(self):
        self.outputLabel.setText('0')

    def press_DEL(self):
        # In MEMO we grab what's on the screen already
        MEMO = self.outputLabel.text()
        # Remove last item in list/string
        MEMO = MEMO[:-1]
        self.outputLabel.setText(MEMO)
    
    
    def press_PM(self):
        # Grab what's on the screen already
        MEMO = self.outputLabel.text()
        if "-" in MEMO:
            self.outputLabel.setText(MEMO.replace("-", ""))
        else:
            self.outputLabel.setText(f'-{MEMO}')
        
    def press_DOT(self):
        # In MEMO we grab what's on the screen already
        MEMO = self.outputLabel.text()
        if "." in MEMO:
            pass
        else:
            self.outputLabel.setText(f'{MEMO}.')
   
    '''
    def press_percent(self):
        MEMO = self.outputLabel.text()
        calc = eval(MEMO[-1])/100
        #MEMO[-1] = str(calc) 
        self.outputLabel.setText(MEMO)
    '''
    def press_leftpar(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}(')
    
    def press_rightpar(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()})')
    
    def press_pig(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}pi')
    
    def press_nepero(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}e')
    
    def press_squareroot(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}sqrt(')
    def press_power(self):
        # Check to see if starts with 0 and delete 0
        if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
        # Concatenate the pressed button with what was there already
        self.outputLabel.setText(f'{self.outputLabel.text()}**')

    
    def press_DIV(self):
        MEMO = self.outputLabel.text()
        self.outputLabel.setText(f'{MEMO}/')
    
    def press_PER(self):
        MEMO = self.outputLabel.text()
        self.outputLabel.setText(f'{MEMO}*')
    
    def press_MEN(self):
        MEMO = self.outputLabel.text()
        self.outputLabel.setText(f'{MEMO}-')
    
    def press_PIU(self):
        MEMO = self.outputLabel.text()
        self.outputLabel.setText(f'{MEMO}+')

    # Let's Do Some Math!

    def press_UGU(self):
        
        # Grab what's on the screen already
        MEMO = self.outputLabel.text()
        try:
            # Do the math
            answer = eval(MEMO)
            self.outputLabel.setText("")
            # Output answer to the screen
            self.outputLabel.setText(str(answer))
        except:
            # Output error to the screen
            self.outputLabel.setText("ERROR")
    


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())