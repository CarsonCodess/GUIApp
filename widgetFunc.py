from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QDoubleSpinBox, QRadioButton, QButtonGroup, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import widgetFunc as wf

#NEED THESE WIDGETS:
#

def createLabel(window, text, alignment, pointSize, bold):
    label = QLabel(text, alignment=alignment)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    label.setFont(font)
    return label
def createButton(window, text, pointSize, bold):
    button = QPushButton(text)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    button.setFont(font)
    return button
def createPixmap(path, scaleX, scaleY):
    label = QLabel()
    label.setPixmap(QPixmap(path).scaled(scaleX, scaleY))
    return label
def createInputField(window, text, alignment, pointSize, bold):
    label = QLineEdit(alignment=alignment)
    label.setPlaceholderText(text)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    label.setFont(font)
    return label
def createLabel(window, text, pointSize, bold):
    label = QLabel(text)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    label.setFont(font)
    return label
def createButton(window, text, pointSize, bold):
    button = QPushButton(text)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    button.setFont(font)
    return button
def createPixmap(path, scaleX, scaleY):
    label = QLabel()
    label.setPixmap(QPixmap(path).scaled(scaleX, scaleY))
    return label
def createInputField(window, text, pointSize, bold):
    label = QLineEdit()
    label.setPlaceholderText(text)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    label.setFont(font)
    return label
def createComboBox(window, items, pointSize, bold):
    comboBox = QComboBox()
    for item in items:
        comboBox.addItem(item)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    comboBox.setFont(font)
    return comboBox
def createSpinBox(window, minimum, maximum, singleStep, value, pointSize, bold):
    spinBox = QSpinBox()
    spinBox.setMinimum(minimum)
    spinBox.setMaximum(maximum)
    spinBox.setSingleStep(singleStep)
    spinBox.setValue(value)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    spinBox.setFont(font)
    return spinBox
def createDoubleSpinBox(window, minimum, maximum, singleStep, value, pointSize, bold):
    spinBox = QDoubleSpinBox()
    spinBox.setMinimum(minimum)
    spinBox.setMaximum(maximum)
    spinBox.setSingleStep(singleStep)
    spinBox.setValue(value)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    spinBox.setFont(font)
    return spinBox
def createRadioButton(window, text, pointSize, bold):
    radioButton = QRadioButton(text)
    font = window.font()
    font.setPointSize(pointSize)
    font.setBold(bold)
    radioButton.setFont(font)
    return radioButton