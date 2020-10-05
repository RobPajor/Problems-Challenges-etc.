import random
import string
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



# get random string password with letters, digits, and symbols
def get_random_password_string(length):
    password_characters = ""
    if checkbox1.isChecked() == True:
        password_characters += string.ascii_lowercase
    if checkbox2.isChecked() == True:
        password_characters += string.ascii_uppercase
    if checkbox3.isChecked() == True:
        password_characters += string.digits
    if checkbox4.isChecked() == True:
        password_characters += string.punctuation
    print(line.text())

        
    # password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    print("Random string password is: ", password)
    return password


def update():    
    label.setText("Your random password is: " + get_random_password_string(int(line.text())))
    label.adjustSize()

def retrieve():
    print(label.text())

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(200,100,500,300)
win.setWindowTitle("Random Password Generator v1.0.0")

# Title
label1 = QtWidgets.QLabel(win)
label1.setText("Random Password Generator made in PyQt5")
label1.adjustSize()
label1.move(20,10)
label1.setTextInteractionFlags(Qt.TextSelectableByMouse)


# Generated Password
label = QtWidgets.QLabel(win)
label.setText(" ")
label.adjustSize()
label.move(20,180)
label.setTextInteractionFlags(Qt.TextSelectableByMouse)

# Generate Button
button = QtWidgets.QPushButton(win)
button.clicked.connect(update)
button.setText("Generate")
button.adjustSize()
button.move(20,150)

# Checkboxes
checkbox1 = QtWidgets.QCheckBox(win)
checkbox1.setText("Lowercase")
checkbox1.move(20,30)

checkbox2 = QtWidgets.QCheckBox(win)
checkbox2.setText("Uppercase")
checkbox2.move(20,50)

checkbox3 = QtWidgets.QCheckBox(win)
checkbox3.setText("Numbers")
checkbox3.move(20,70)

checkbox4 = QtWidgets.QCheckBox(win)
checkbox4.setText("Punctuation")
checkbox4.move(20,90)

label2 = QtWidgets.QLabel(win)
label2.setText("Password Length")
label2.adjustSize()
label2.move(55,120)


line = QtWidgets.QLineEdit(win)
line.move(20,120)
line.adjustSize()
line.setFixedWidth(30)
line.setFixedHeight(15)

win.show()
sys.exit(app.exec_())
