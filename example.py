from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

app = QApplication([])

window = QMainWindow()

#parentLayout = QVBoxLayout()
parentLayout = QGridLayout()

buttonLayout = QHBoxLayout()

button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')

#buttonLayout.addWidget(button1)
#buttonLayout.addSpacing(50)
#buttonLayout.addWidget(button2)

label1 = QLabel('Label 1')
parentLayout.addWidget(label1,1,0)

parentLayout.addWidget(button1,0,1)
parentLayout.addWidget(button2,1,1)

#parentLayout.addLayout(buttonLayout)

label = QLabel('Hello World', alignment=Qt.AlignmentFlag.AlignCenter)
parentLayout.addWidget(label,0,0, 2,1)

centerWidget = QWidget()
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

#Setting up window
"""window.setMinimumSize(800, 600)
#window.setMinimumHeight(800)
#window.setMinimumWidth(600)
#window.setFixedSize(800, 600)
window.setWindowTitle('Hello World')
window.setWindowIcon(QIcon('icon.png'))"""

#Adding Widgets
"""label = QLabel('Hello World', alignment=Qt.AlignmentFlag.AlignCenter)
font = window.font()
font.setPointSize(18)
font.setBold(True)
label.setFont(font)
window.setCentralWidget(label)

label2 = QLabel()
label2.setPixmap(QPixmap('icon.png').scaled(200, 200))
window.setCentralWidget(label2)

button = QPushButton('Click Me')
font = window.font()
font.setPointSize(18)
button.setFont(font)
window.setCentralWidget(button)"""


window.show()
app.exec()