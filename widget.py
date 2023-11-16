# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from pprint import pprint
from collections import Counter
import re
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

    def counter(self, filepath, alphabet):

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read().lower()
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

        counter_letters = Counter(dict.fromkeys(alphabet,0))
        find_letters = re.findall(r'[а-я]',text)
        counter_letters.update(Counter(find_letters))
        return counter_letters

    def ChooseFileButton_pressed(self):
        print("Choose button pressed")
        self.open_dialog_box()

    def ResetFileButton_pressed(self):
        print("Reset button pressed")
        self.ui.LinesLineEdit.clear()
        self.ui.WordsLineEdit.clear()
        self.ui.SymbolsLineEdit.clear()
        self.ui.textEdit.clear()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        filepath = filename[0]
        cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]
        print(filepath)
        text = open(filepath, encoding="utf-8").read()
        self.ui.textEdit.setPlainText(text)
        start_time = time.time()
        letters = self.counter(filepath, cyrillic)
        pprint(letters)
        print("Analyze took ""--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
