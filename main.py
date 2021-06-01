from calculator import calculator
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QLabel, QLineEdit, QTextEdit)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.s = ''
        self.initUI()

    def on_clicked_cell(self, button):
        #print(button.text())
        if button.text()=='=':

            try:
                #print(self.label.text())
                res = calculator(self.label.text())
                self.label.setText(str(res))
            except:
                self.label.setText('Неверный ввод')
        elif button.text()=='<-':
            if self.label.text()!='':
                self.label.setText(self.label.text()[:-1])
            else:self.label.setText('')
        elif button.text()=='del':
            self.label.setText('')
        else:
            self.label.setText(self.label.text() + button.text())

    def initUI(self):

        grid = QGridLayout()
        self.label = QLineEdit()
        grid.addWidget(self.label, 1, 1, 1, 4)
        self.setLayout(grid)

        names = [
                 '1', '2', '3', '/',
                 '4', '5', '6', '*',
                 '7', '8', '9', '-',
                 '0', '(', ')', '+',
                 '~', 'del', '<-','=']

        k=0
        for i in range(5,10):
            for j in range(1,5):

                if names[k] == '':
                    continue
                button = QPushButton(names[k])
                button.clicked.connect(
                    lambda checked, button=button : self.on_clicked_cell(button)
                )
                grid.addWidget(button, i,j)
                if k != len(names)-1:

                    k += 1
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()







if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
