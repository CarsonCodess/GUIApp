from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QDoubleSpinBox, QRadioButton, QButtonGroup, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import widgetFunc as wf

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        parentLayout = QGridLayout()

        self.loginText = wf.createLabel(self, 'Login', 50, True)
        self.usernameInputText = wf.createLabel(self, 'Username:', 20, False)
        self.passwordInputText = wf.createLabel(self, 'Password:', 20, False)
        self.usernameInput = wf.createInputField(self, 'Enter your username', 20, False)
        self.passwordInput = wf.createInputField(self, 'Enter your password', 20, False)
        self.submitButton = wf.createButton(self, 'Submit', 20, False)
        self.ageBox = wf.createSpinBox(self, 0, 100, 1, 10, 15, False)
        self.ethnicityBox = wf.createComboBox(self, ['White', 'Black', 'Asian', 'Hispanic', 'Other'], 20, False)

        parentLayout.addWidget(self.loginText, 0, 0, 1, 5, alignment=Qt.AlignmentFlag.AlignCenter)

        parentLayout.addWidget(self.usernameInputText, 1, 0, 1, 1)
        parentLayout.addWidget(self.usernameInput, 1, 1, 1, 4)
        parentLayout.addWidget(self.passwordInputText, 2, 0, 1, 1)
        parentLayout.addWidget(self.passwordInput, 2, 1, 1, 4)

        parentLayout.addWidget(self.ageBox, 3, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        parentLayout.addWidget(self.ethnicityBox, 3, 3, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        parentLayout.addWidget(self.submitButton, 5, 0, 1, 5)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

        self.showMaximized()
        self.setWindowTitle('Hello World')
        self.setWindowIcon(QIcon('icon.png'))

    def buttonClicked(self):
        self.label.setText("Button Clicked")


app = QApplication([])
window = Window()

window.show()
app.exec()