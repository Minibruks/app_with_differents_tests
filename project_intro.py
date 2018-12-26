import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QInputDialog, QLabel
from PyQt5 import QtGui


def space_count(s):
    count = 0
    for elem in s[::-1]:
        if elem == ' ':
            count += 1
        else:
            return count
    return count


# Иницилизация вводного окна
class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('fpage.ui', self)


# Иницилизация окна, в котором пользователь выбирает предмет для тестов
class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('second_page.ui', self)


class ResultPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('result_page.ui', self)


class YourResPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('your_res_page.ui', self)


# Иницилизация окна теста по математике
class MathTest(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('math_test.ui', self)
        # Файл с текстом задания
        with open('math_q1.txt', 'r') as f:
            read = list(map(lambda x: x.strip(), f.read().split('???')))

        x0, y0 = 20, 20
        questions = []
        self.answers = ['' for i in range(len(read))]
        self.bool_ans = []
        self.answers_btn = []
        self.got_answers = []
        for i in range(len(read)):
            label = QLabel(self)
            questions.append(label)

        for i in range(len(questions)):
            questions[i].setText(read[i])
            questions[i].setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
            questions[i].adjustSize()
            questions[i].resize(1000, 25)
            questions[i].move(x0, y0)
            y0 += 80

        for i in range(len(questions)):
            btn = QPushButton(self)
            self.answers_btn.append(btn)
            got_ans = QLabel(self)
            self.got_answers.append(got_ans)

        y0 = 50

        for i in range(len(self.answers_btn)):
            self.answers_btn[i].setText('Ввести ответ' + (' ' * i))
            self.answers_btn[i].resize(100, 25)
            self.answers_btn[i].move(x0, y0)

            self.got_answers[i].setText('                                        ')
            self.got_answers[i].resize(200, 25)
            self.got_answers[i].setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
            self.got_answers[i].move(x0 + 150, y0)
            y0 += 80

        for i in range(len(self.answers_btn)):
            self.answers_btn[i].clicked.connect(self.ans)

        self.check_btn = QPushButton(self)
        self.check_btn.setText('Результаты')
        self.check_btn.resize(100, 25)
        self.check_btn.move(x0, y0)

    def ans(self):
        try:
            inf, okBtnPressed = QInputDialog.getText(
                self, "Ответ", "Введите ответ"
            )
            if okBtnPressed:
                k = space_count(self.sender().text())
                self.answers[k] = inf
                self.got_answers[k].setText('Ваш ответ: ' + str(inf))
        except Exception as e:
            print(e)


class YourTestLoad(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test_load.ui', self)


class YourTestExe(QWidget):
    def __init__(self):
        super().__init__()

    def do(self, in_task):
        self.setGeometry(300, 300, 1000, 900)
        self.setWindowTitle('Пользовательский тест')
        self.task_file = in_task

        with open(self.task_file, 'r') as f:
            read = list(map(lambda x: x.strip(), f.read().split('???')))

        x0, y0 = 20, 20
        questions = []
        self.answers = ['' for i in range(len(read))]
        self.bool_ans = []
        self.answers_btn = []
        self.got_answers = []
        for i in range(len(read)):
            label = QLabel(self)
            questions.append(label)

        for i in range(len(questions)):
            questions[i].setText(read[i])
            questions[i].setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
            questions[i].adjustSize()
            questions[i].resize(1000, 25)
            questions[i].move(x0, y0)
            y0 += 80

        for i in range(len(questions)):
            btn = QPushButton(self)
            self.answers_btn.append(btn)
            got_ans = QLabel(self)
            self.got_answers.append(got_ans)

        y0 = 50

        for i in range(len(self.answers_btn)):
            self.answers_btn[i].setText('Ввести ответ' + (' ' * i))
            self.answers_btn[i].resize(100, 25)
            self.answers_btn[i].move(x0, y0)

            self.got_answers[i].setText('                                        ')
            self.got_answers[i].resize(200, 25)
            self.got_answers[i].setFont(QtGui.QFont("Times", 11, QtGui.QFont.Bold))
            self.got_answers[i].move(x0 + 150, y0)
            y0 += 80

        for i in range(len(self.answers_btn)):
            self.answers_btn[i].clicked.connect(self.ans)

        self.check_btn = QPushButton(self)
        self.check_btn.setText('Результаты')
        self.check_btn.resize(100, 25)
        self.check_btn.move(x0, y0)

    def ans(self):
        try:
            inf, okBtnPressed = QInputDialog.getText(
                self, "Ответ", "Введите ответ"
            )
            if okBtnPressed:
                k = space_count(self.sender().text())
                self.answers[k] = inf
                self.got_answers[k].setText('Ваш ответ: ' + str(inf))
        except Exception as e:
            print(e)


# Главное рабочее окно
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.w1 = FirstPage()
        self.w2 = SecondPage()
        self.math = MathTest()
        self.res = ResultPage()
        self.pers_test = YourTestLoad()
        self.pers_res = YourResPage()

        self.your_test_task = ''
        self.your_test_ans = ''

        self.test_exe = YourTestExe()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('благодаря этому окну программа работает!')
        self.show_firt_page()
        self.uname = ''

    # Метод показывает первое окно
    def show_firt_page(self):
        self.w1.show()
        self.w1.input_name.clicked.connect(self.name_in)

    # Вводится имя пользователя и закрывается первое окно
    def name_in(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите имя", "Как тебя зовут?"
        )
        if okBtnPressed:
            self.w1.close()
            self.uname = i
            self.select()

    # Открывается второе окно
    def select(self):
        try:
            self.w2.greet.setText('Здравствуйте, {}'.format(self.uname))
            self.w2.show()
            self.w2.math.clicked.connect(self.math_test)
            self.w2.load_test.clicked.connect(self.load_your_test)
        except Exception as e:
            print(e)

    def math_test(self):
        with open('math_q1_ans.txt') as right_ans_list:
            self.right_ans = right_ans_list.read().split('\n')

        self.math.show()
        self.w2.close()
        self.math.check_btn.clicked.connect(self.check_math)

    def check_math(self):
        try:
            for i in range(len(self.right_ans)):
                if self.right_ans[i] == self.math.answers[i]:
                    self.math.bool_ans.append(True)
                else:
                    self.math.bool_ans.append(False)

            self.res.count_res.setText('{} из {}'.format(str(sum([1 for elem in self.math.bool_ans if elem])),
                                                         str(len(self.math.bool_ans))))
            det_res = []
            for i in range(len(self.right_ans)):
                a = 'Задание {0}\n{1}'.format(str(i + 1),
                                              'Ваш ответ: {}. Правильный ответ: {}'.format(self.math.answers[i],
                                                                                           self.right_ans[i]))
                det_res.append(a)

            det_res = '\n'.join(det_res)
            self.res.detailed_res.setText(det_res)

            self.res.show()
        except Exception as e:
            print(e)

    def load_your_test(self):
        self.pers_test.show()
        self.w2.close()
        self.pers_test.generate_btn.clicked.connect(self.generate_test)

    def generate_test(self):
        try:
            assert self.pers_test.input_task.text()[-4:] == '.txt'
            assert self.pers_test.input_task.text() != ''
            assert self.pers_test.input_task.text()[0] != '.'

            assert self.pers_test.input_ans.text()[-4:] == '.txt'
            assert self.pers_test.input_ans.text() != ''
            assert self.pers_test.input_ans.text()[0] != '.'

            self.your_test_task = self.pers_test.input_task.text()
            self.your_test_ans = self.pers_test.input_ans.text()

            self.pers_test.close()
            self.test_exe.do(self.your_test_task)
            self.test_exe.show()
            self.test_exe.check_btn.clicked.connect(self.your_test)
        except AssertionError:
            self.pers_test.error_lbl.setText('Имя файла введено неверно!')

    def your_test(self):
        with open(self.your_test_ans) as right_ans_list:
            self.your_right_ans = right_ans_list.read().split('\n')

        try:
            for i in range(len(self.your_right_ans)):
                if self.your_right_ans[i] == self.test_exe.answers[i]:
                    self.test_exe.bool_ans.append(True)
                else:
                    self.test_exe.bool_ans.append(False)

            self.pers_res.count_res.setText('{} из {}'.format(str(sum([1 for elem in self.test_exe.bool_ans if elem])),
                                                         str(len(self.test_exe.bool_ans))))
            det_res = []
            for i in range(len(self.your_right_ans)):
                a = 'Задание {0}\n{1}'.format(str(i + 1),
                                              'Ваш ответ: {}. Правильный ответ: {}'.format(self.test_exe.answers[i],
                                                                                           self.your_right_ans[i]))
                det_res.append(a)

            det_res = '\n'.join(det_res)
            self.pers_res.detailed_res.setText(det_res)

            self.pers_res.show()
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
ex = MainWindow()
ex.showMinimized()
sys.exit(app.exec_())
