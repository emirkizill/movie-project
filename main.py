import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
class MyWindow(QMainWindow):
  def __init__(self):
      super().__init__()
      self.setWindowTitle("Film")
      self.setFixedSize(700,700)
      central_widget = QWidget(self)
      self.setCentralWidget(central_widget)
      layout = QVBoxLayout()
      central_widget.setLayout(layout)
      ##label
      self.label = QLabel("Hosgeldiniz",self)
      self.label.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.label)
      ##buton
      self.button1 = QPushButton("Button 1",self)
      self.button1.clicked.connect(self.on_button_click)
      layout.addWidget(self.button1)
  def on_button_click(self):
      self.label.setText("butona tiklandi")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
