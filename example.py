from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QDoubleSpinBox, QRadioButton, QButtonGroup, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import widgetFunc as wf

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        self.setWindowTitle('Hello World')
        self.setWindowIcon(QIcon('icon.png'))

        parentLayout = QGridLayout()

        """self.loginText = wf.createLabel(window, 'Login', 50, True)
        self.usernameInputText = wf.createLabel(window, 'Username:', 20, False)
        self.passwordInputText = wf.createLabel(window, 'Password:', 20, False)
        self.usernameInput = wf.createInputField(window, 'Enter your username', 20, False)
        self.passwordInput = wf.createInputField(window, 'Enter your password', 20, False)
        self.submitButton = wf.createButton(window, 'Submit', 20, False)

        parentLayout.addWidget(self.loginText, 0, 0, 1, 5, alignment=Qt.AlignmentFlag.AlignCenter)

        parentLayout.addWidget(self.usernameInputText, 1, 0, 2, 1)
        parentLayout.addWidget(self.usernameInput, 1, 1, 2, 4)
        parentLayout.addWidget(self.passwordInputText, 3, 0, 1, 1)
        parentLayout.addWidget(self.passwordInput, 3, 1, 1, 4)

        parentLayout.addWidget(self.submitButton, 5, 0, 1, 5)"""

        self.label = QLabel("Label")
        self.button = QPushButton("Button")
        self.comboBox = QComboBox()
        self.spinBox = QSpinBox()
        self.buttonGroup = QButtonGroup()

        self.comboBox.addItem("Item 1")
        self.comboBox.addItem("Item 2")
        self.comboBox.addItem("Item 3")

        self.spinBox.setMinimum(0)
        self.spinBox.setValue(50)
        self.spinBox.setSingleStep(10)
        self.spinBox.setMaximum(100)

        self.radioButton1 = QRadioButton("Radio Button 1")
        self.radioButton2 = QRadioButton("Radio Button 2")
        self.radioButton3 = QRadioButton("Radio Button 3")

        self.buttonGroup.addButton(self.radioButton1)
        self.buttonGroup.addButton(self.radioButton2)
        self.buttonGroup.addButton(self.radioButton3)

        self.button.clicked.connect(self.buttonClicked)

        parentLayout.addWidget(self.label, 0, 0, 1, 1)
        parentLayout.addWidget(self.button, 1, 0, 1, 1)
        parentLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        parentLayout.addWidget(self.spinBox, 3, 0, 1, 1)
        parentLayout.addWidget(self.radioButton1, 4, 0, 1, 1)
        parentLayout.addWidget(self.radioButton2, 4, 1, 1, 1)
        parentLayout.addWidget(self.radioButton3, 4, 2, 1, 1)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

    def buttonClicked(self):
        self.label.setText("Button Clicked")


app = QApplication([])
window = Window()

window.show()
app.exec()