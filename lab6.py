import sys# UI құруға компоненттік тәсіл-Модульдік функционалдық компоненттерді пайдалана отырып, пайдаланушы интерфейсін әзірлеу python


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('UI құруға компоненттік тәсілді модульдік функционалдық компоненттерді пайдалану')

        # Модульдік функционалдық компоненттерді құру
        self.name_label = QLabel('Атыңызды енгізіңіз:')
        self.name_edit = QLineEdit()
        self.greet_button = QPushButton('Қош келдіңіз!')

        # Орналастыру
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.greet_button)

        # Орналастыру элементтерінің байланыстары
        self.setLayout(layout)

        # Оқиғаларды қосу
        self.greet_button.clicked.connect(self.greet)

    def greet(self):
        name = self.name_edit.text()
        greeting_message = f'Ассалаумагаликум, {name}!'
        print(greeting_message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
