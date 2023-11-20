# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QTextCursor
import time

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.ChooseFileButton.clicked.connect(self.ChooseFileButton_pressed)
        self.ui.ResetFileButton.clicked.connect(self.ResetFileButton_pressed)

    def counter(self, filepath):
        lines = 0
        words = 0
        symbols = 0
        file = open(filepath, "r", encoding="utf-8")
        for line in file:
            lines += 1
            words += len(line.split())
            symbols += len(line)
        self.ui.LinesLineEdit.setText(str(lines))
        self.ui.WordsLineEdit.setText(str(words))
        self.ui.SymbolsLineEdit.setText(str(symbols))
        file.close()



    def ChooseFileButton_pressed(self):
        print("Choose button pressed")
        filename = QFileDialog.getOpenFileName()
        filepath = filename[0]
        print(filepath)

        read_time = time.time()
        text = open(filepath, encoding="utf-8").read()
        self.ui.ReadingTimeLineEdit.setText(" ""--- %s seconds ---" % (time.time() - read_time))

        text_time = time.time()



        #previous_cursor_pos = self.ui.textEdit.textCursor()
        # self.ui.textEdit.moveCursor(QTextCursor.End)
        # self.ui.textEdit.insertPlainText(text)
        #self.ui.textEdit.setTextCursor(previous_cursor_pos)


        max_length_text = self.ui.Symbols_amountLineEdit.text()
        max_length = int(max_length_text)
        if len(text) > max_length:
            print("limit hitted, slicing text")
            text = text[:max_length]
        self.ui.textEdit.setPlainText(text)

       # self.ui.textEdit.setPlainText(text)
        self.ui.Setting_textTimeLineEdit.setText(" ""--- %s seconds ---" % (time.time() - text_time))
        text = ""

        analyze_time = time.time()
        self.counter(filepath)
        self.ui.AnalyzeTimeLineEdit.setText(" ""--- %s seconds ---" % (time.time() - analyze_time))

    def ResetFileButton_pressed(self):
        print("Reset button pressed")
        self.ui.LinesLineEdit.clear()
        self.ui.WordsLineEdit.clear()
        self.ui.SymbolsLineEdit.clear()
        self.ui.textEdit.clear()
        self.ui.ReadingTimeLineEdit.clear()
        self.ui.Setting_textTimeLineEdit.clear()
        self.ui.AnalyzeTimeLineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
