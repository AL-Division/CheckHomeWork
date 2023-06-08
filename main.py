from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QTextEdit, QListWidget, QLineEdit


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Программа контроля обучения учеников')
main_win.resize(1280,720)

#Создание виджетов
lbl_schedule = QLabel("Расписание")
lbl_schedule_today = QLabel("Соц.сети ученика")
btn_del_student = QPushButton('Удалить ученика')
btn_add_student = QPushButton('Добавить ученика')
btn_send_homework = QPushButton('Отправить')
btn_change_schedule = QPushButton('Изменить расписание')
text_homework= QTextEdit()
text_homework.setPlaceholderText("Введите текст ДЗ")
list_schedule = QListWidget()
list_students = QListWidget()
list_mail = QListWidget()
line_mail = QLineEdit()

#Создание слоев


#Обработка событий
def del_student():
    pass
def add_student():
    pass
def send_homework():
    pass
def change_schedule():
    pass

#Подключение событий
btn_del_student.clicked.connect(del_student)
btn_add_student.clicked.connect(add_student)
btn_send_homework.clicked.connect(send_homework)
btn_change_schedule.clicked.connect(change_schedule)

# main_win.setLayout(v_line)
main_win.show()
app.exec_()