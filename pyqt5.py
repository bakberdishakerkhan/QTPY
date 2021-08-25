#подключение модулей и виджетов
from PyQt5.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Current')

        self.radio_button_1 = QRadioButton('1')
        self.radio_button_1.setChecked(True)

        self.radio_button_2 = QRadioButton('2')
        self.radio_button_3 = QRadioButton('3')

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
        self.button_group.addButton(self.radio_button_3)

        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)
        layout.addWidget(self.radio_button_3)

        self.setLayout(layout)

    def _on_radio_button_clicked(self, button):
        print(button)
        self.label.setText('Current: ' + button.text())

#создание основной (main) функции проекта
def main():
    app = QApplication([])
    w = Widget()
    w.show()
#    mw = MainWindow()
    app.exec_()
#запуск проекта
main()
