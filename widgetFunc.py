from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
#NEED THESE WIDGETS:
#Button
#Label
#Pixmap
#
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