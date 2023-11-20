# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ChooseFileButton = QPushButton(Widget)
        self.ChooseFileButton.setObjectName(u"ChooseFileButton")

        self.gridLayout.addWidget(self.ChooseFileButton, 1, 0, 1, 1)

        self.ResetFileButton = QPushButton(Widget)
        self.ResetFileButton.setObjectName(u"ResetFileButton")

        self.gridLayout.addWidget(self.ResetFileButton, 1, 1, 1, 1)

        self.TextGroupBox = QGroupBox(Widget)
        self.TextGroupBox.setObjectName(u"TextGroupBox")
        self.gridLayout_4 = QGridLayout(self.TextGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.FileVerticalLayout = QVBoxLayout()
        self.FileVerticalLayout.setObjectName(u"FileVerticalLayout")
        self.textEdit = QPlainTextEdit(self.TextGroupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setMaximumBlockCount(0)

        self.FileVerticalLayout.addWidget(self.textEdit)


        self.gridLayout_4.addLayout(self.FileVerticalLayout, 2, 0, 1, 1)

        self.label_4 = QLabel(self.TextGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.Symbols_amountLineEdit = QLineEdit(self.TextGroupBox)
        self.Symbols_amountLineEdit.setObjectName(u"Symbols_amountLineEdit")

        self.gridLayout_4.addWidget(self.Symbols_amountLineEdit, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.TextGroupBox, 0, 1, 1, 1)

        self.TextAnalyzeGroupBox = QGroupBox(Widget)
        self.TextAnalyzeGroupBox.setObjectName(u"TextAnalyzeGroupBox")
        self.gridLayout_2 = QGridLayout(self.TextAnalyzeGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Setting_textLabel = QLabel(self.TextAnalyzeGroupBox)
        self.Setting_textLabel.setObjectName(u"Setting_textLabel")

        self.gridLayout_3.addWidget(self.Setting_textLabel, 4, 0, 1, 1)

        self.label_3 = QLabel(self.TextAnalyzeGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label = QLabel(self.TextAnalyzeGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.ReadingLabel = QLabel(self.TextAnalyzeGroupBox)
        self.ReadingLabel.setObjectName(u"ReadingLabel")

        self.gridLayout_3.addWidget(self.ReadingLabel, 3, 0, 1, 1)

        self.SymbolsLineEdit = QLineEdit(self.TextAnalyzeGroupBox)
        self.SymbolsLineEdit.setObjectName(u"SymbolsLineEdit")
        self.SymbolsLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.SymbolsLineEdit, 2, 1, 1, 1)

        self.WordsLineEdit = QLineEdit(self.TextAnalyzeGroupBox)
        self.WordsLineEdit.setObjectName(u"WordsLineEdit")
        self.WordsLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.WordsLineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.TextAnalyzeGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.LinesLineEdit = QLineEdit(self.TextAnalyzeGroupBox)
        self.LinesLineEdit.setObjectName(u"LinesLineEdit")
        self.LinesLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.LinesLineEdit, 0, 1, 1, 1)

        self.AnalyzeLabel = QLabel(self.TextAnalyzeGroupBox)
        self.AnalyzeLabel.setObjectName(u"AnalyzeLabel")

        self.gridLayout_3.addWidget(self.AnalyzeLabel, 5, 0, 1, 1)

        self.ReadingTimeLineEdit = QLineEdit(self.TextAnalyzeGroupBox)
        self.ReadingTimeLineEdit.setObjectName(u"ReadingTimeLineEdit")
        self.ReadingTimeLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.ReadingTimeLineEdit, 3, 1, 1, 1)

        self.Setting_textTimeLineEdit = QLineEdit(self.TextAnalyzeGroupBox)
        self.Setting_textTimeLineEdit.setObjectName(u"Setting_textTimeLineEdit")
        self.Setting_textTimeLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.Setting_textTimeLineEdit, 4, 1, 1, 1)

        self.AnalyzeTimeLineEdit = QLineEdit(self.TextAnalyzeGroupBox)
        self.AnalyzeTimeLineEdit.setObjectName(u"AnalyzeTimeLineEdit")
        self.AnalyzeTimeLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.AnalyzeTimeLineEdit, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.TextAnalyzeGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Text analyzer", None))
        self.ChooseFileButton.setText(QCoreApplication.translate("Widget", u"Choose file", None))
        self.ResetFileButton.setText(QCoreApplication.translate("Widget", u"Reset file", None))
        self.TextGroupBox.setTitle(QCoreApplication.translate("Widget", u"File", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Set amount of symbols to print, 1mil+ is RAM-unefficient", None))
        self.Symbols_amountLineEdit.setInputMask(QCoreApplication.translate("Widget", u"000000000000", None))
        self.Symbols_amountLineEdit.setText(QCoreApplication.translate("Widget", u"1000000", None))
        self.Symbols_amountLineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"1000000 is default", None))
        self.TextAnalyzeGroupBox.setTitle(QCoreApplication.translate("Widget", u"File analyze", None))
        self.Setting_textLabel.setText(QCoreApplication.translate("Widget", u"Setting text time", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Lines:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Symbols:", None))
        self.ReadingLabel.setText(QCoreApplication.translate("Widget", u"Reading time", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Words:", None))
        self.AnalyzeLabel.setText(QCoreApplication.translate("Widget", u"Analyze time", None))
    # retranslateUi

