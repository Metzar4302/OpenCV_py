import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui, QtCore
import design  # Это наш конвертированный файл дизайна
from qlabel import Ui_MainWindow  
import os

# class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.setupUi(self)  # Это нужно для инициализации нашего дизайна
#         self.btnBrowse.clicked.connect(self.browse_folder)

#     def browse_folder(self):
#         self.listWidget.clear()  # На случай, если в списке уже есть элементы
#         directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
#         # открыть диалог выбора директории и установить значение переменной
#         # равной пути к выбранной директории

#         if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
#             for file_name in os.listdir(directory):  # для каждого файла в директории
#                 self.listWidget.addItem(file_name)   # добавить файл в listWidget


# def main():
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()  # и запускаем приложение

# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.test_lable.setFont(QtGui.QFont('SansSerif', 30))
        self.ui.test_lable.setGeometry(
            QtCore.QRect(10, 10, 200, 200)
        )

        self.ui.test_horizontalSlider.maximum = 100
        self.ui.test_horizontalSlider.setValue(50)
        self.ui.test_horizontalSlider.valueChanged.connect(self.setValForTextEdit)
        
        self.ui.test_textEdit.setText("123")

        self.ui.test_pushButton.clicked.connect(self.addOneButton)
        

    def addOneButton(self):
        self.ui.test_textEdit.setText("LCD screen was set to 500")
        self.setValForLCD()

    def setValForTextEdit(self):
        self.ui.test_textEdit.setText(str(self.ui.test_horizontalSlider.value()))

    def setValForLCD(self):
        self.ui.test_lcdNumber.intValue = 500
        
    

def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()