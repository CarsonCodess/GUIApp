from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import widgetFunc as wf

app = QApplication([])

window = QMainWindow()

parentLayout = QGridLayout()


loginText = wf.createLabel(window, 'Login', 50, True)
usernameInputText = wf.createLabel(window, 'Username:', 20, False)
passwordInputText = wf.createLabel(window, 'Password:', 20, False)
usernameInput = wf.createInputField(window, 'Enter your username', 20, False)
passwordInput = wf.createInputField(window, 'Enter your password', 20, False)
submitButton = wf.createButton(window, 'Submit', 20, False)

parentLayout.addWidget(loginText, 0, 0, 1, 5, alignment=Qt.AlignmentFlag.AlignCenter)

parentLayout.addWidget(usernameInputText, 1, 0, 2, 1)
parentLayout.addWidget(usernameInput, 1, 1, 2, 4)
parentLayout.addWidget(passwordInputText, 3, 0, 1, 1)
parentLayout.addWidget(passwordInput, 3, 1, 1, 4)

parentLayout.addWidget(submitButton, 5, 0, 1, 5)

centerWidget = QWidget()
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

#Setting up window
window.showMaximized()
window.setWindowTitle('Hello World')
window.setWindowIcon(QIcon('icon.png'))


window.show()
app.exec()