# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     pyside2-uic form.ui -o ui_form.py
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QErrorMessage

import time

from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.ChooseFileButton.clicked.connect(self.ChooseFileButton_pressed)
        self.ui.ResetFileButton.clicked.connect(self.ResetFileButton_pressed)
        error_dialog = QErrorMessage()
        error_dialog.showMessage('Error was occured during process! Possibly no file or wrong format was chosen')

    def counter(self, filepath):
        lines = 0
        words = 0
        symbols = 0
        filetext = open(filepath, "r", encoding="utf-8")
        for line in filetext:
            lines += 1
            words += len(line.split())
            symbols += len(line)
        self.ui.LinesLineEdit.setText(str(lines))
        self.ui.WordsLineEdit.setText(str(words))
        self.ui.SymbolsLineEdit.setText(str(symbols))
        self.ui.Avg_wordsymbolsLineEdit.setText(str(symbols / words))

        filetext.close()



    def ChooseFileButton_pressed(self):
        print("Choose button pressed")
        filename = QFileDialog.getOpenFileName(self, "Open text file")
        filepath = filename[0]
        print(filepath)


        read_time = time.time()
        text = open(filepath, encoding="utf-8").read()
        self.ui.ReadingTimeLineEdit.setText(" ""--- %s seconds ---" % (time.time() - read_time))

        self.ui.textEdit.clear()
        text_time = time.time()

        max_length_text = self.ui.Symbols_amountLineEdit.text()
        max_length = int(max_length_text)
        if len(text) > max_length:
            self.ui.textEdit.appendPlainText("Limit hitted, text is sliced!")
            text = text[:max_length]
        self.ui.textEdit.appendPlainText(text)

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
        self.ui.Avg_wordsymbolsLineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
