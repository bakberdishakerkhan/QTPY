#подключение модулей и виджетов
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt






class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.title = QLabel('Психологический тест:')
        self.button = QPushButton('Подтвердить')
        self.button2 = QPushButton('Назад')

        self.setWindowTitle('Психологический тест')
        self.move(900, 70)
        self.resize(600, 200)  
        self.show() 



        self.radio_button_1 = QRadioButton('Ухаживать за животными')
        self.radio_button_1.setChecked(True)

        self.radio_button_2 = QRadioButton('Обслуживать машины,приборы (следить,регулировать)')
       

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
      

        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)


        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)
        layout.addWidget(self.button, alignment = Qt.AlignBottom)
        layout.addWidget(self.button2, alignment = Qt.AlignTop)


        self.setLayout(layout)

        self.button.clicked.connect(self.dalee)

        self.button2.clicked.connect(self.nazad)

    def dalee(self):
        pass
#        self.radio_button_1.setParent(None)
#        self.radio_button_2.setParent(None)
        

#        self.radio_button_1 = QRadioButton('Помогать больным людям,лечить их')
#        self.radio_button_1.setChecked(True)

#        self.radio_button_2 = QRadioButton('Составлять таблицы, схемы,программы длявычислительных машин')
    def nazad(self):
        pass
    


    def _on_radio_button_clicked(self, button):
#        print(button)
        self.title.setText('Психологический тест: ' + button.text())


#создание основной (main) функции проекта
def main():
    app = QApplication([])
    w = Widget()
    w.show()
#    mw = MainWindow()
    app.exec_()
#запуск проекта
main()
