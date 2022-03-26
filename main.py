from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class cc:
  def __init__(self, url):
    fixerData = requests.get(url).json()
    self.rates = fixerData["rates"]

  def convert(self, cFrom, cTo, amount):
    if cFrom != 'EUR':
      EURamount = amount / self.rates[cFrom]

    convertedAmount = (EURamount * self.rates[cTo])

    return round(convertedAmount, 2)

  def driver(self, cFrom, cTo, amount):
    sAmount = str(amount)
    endAmount = self.convert(cFrom, cTo, amount)
    return f"{sAmount}{cFrom} is {endAmount} in {cTo} "

CurrencyConverter = cc("http://data.fixer.io/api/latest?access_key=38120ef0f3713d26985e19289e0c1f3b")

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(918, 479)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 881, 431))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.background = QtWidgets.QLabel(self.widget)
        self.background.setGeometry(QtCore.QRect(10, 10, 861, 531))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../../Downloads/background1 (1).jpg"))
        self.background.setObjectName("background")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 251, 51))
        self.label_2.setStyleSheet("font: 30pt \"Yu Gothic\";\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(50, 70, 781, 81))
        self.widget_2.setObjectName("widget_2")
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setGeometry(QtCore.QRect(0, 10, 339, 109))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FROMBOX = QtWidgets.QComboBox(self.frame)
        self.FROMBOX.setGeometry(QtCore.QRect(0, 0, 341, 61))
        self.FROMBOX.setStyleSheet("color: white;\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(85,177,218,255)")
        self.FROMBOX.setObjectName("FROMBOX")
        self.FROMBOX.addItem("")
        self.FROMBOX.setItemText(0, "")
        self.FROMBOX.addItem("")
        self.FROMBOX.addItem("")
        self.FROMBOX.addItem("")
        self.frame_3 = QtWidgets.QFrame(self.widget_2)
        self.frame_3.setGeometry(QtCore.QRect(440, -20, 683, 109))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.TOBOX = QtWidgets.QComboBox(self.frame_3)
        self.TOBOX.setGeometry(QtCore.QRect(0, 30, 341, 61))
        self.TOBOX.setStyleSheet("color: white;\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(85,177,218,255)")
        self.TOBOX.setObjectName("TOBOX")
        self.TOBOX.addItem("")
        self.TOBOX.setItemText(0, "")
        self.TOBOX.addItem("")
        self.TOBOX.addItem("")
        self.TOBOX.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setGeometry(QtCore.QRect(350, -10, 81, 109))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 20, 75, 61))
        self.pushButton.setStyleSheet("color: white;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: transparent\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 10, 81, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/convert.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.CONVERSIONBOX = QtWidgets.QLabel(self.widget)
        self.CONVERSIONBOX.setGeometry(QtCore.QRect(50, 270, 781, 51))
        self.CONVERSIONBOX.setStyleSheet("font: 30pt \"Verdana\";\n"
"color: rgba(20,42,121,255);\n"
"text-align: center;")
        self.CONVERSIONBOX.setObjectName("CONVERSIONBOX")
        self.AMOUNTBOX = QtWidgets.QTextEdit(self.widget)
        self.AMOUNTBOX.setGeometry(QtCore.QRect(50, 200, 781, 37))
        self.AMOUNTBOX.setMaximumSize(QtCore.QSize(16777215, 37))
        self.AMOUNTBOX.setStyleSheet("color: rgba(20,42,121,255);\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(85,177,218,255)")
        self.AMOUNTBOX.setObjectName("AMOUNTBOX")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(830, 10, 41, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/images/Downloads/error.png"))
        self.label_3.setObjectName("label_3")
        self.CLOSE = QtWidgets.QPushButton(self.widget)
        self.CLOSE.setGeometry(QtCore.QRect(820, 10, 51, 41))
        self.CLOSE.setStyleSheet("background: transparent\n"
"")
        self.CLOSE.setText("")
        self.CLOSE.setObjectName("CLOSE")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">CurrenSea Converter</span></p></body></html>"))
        self.FROMBOX.setItemText(1, _translate("Form", "USD"))
        self.FROMBOX.setItemText(2, _translate("Form", "CAD"))
        self.FROMBOX.setItemText(3, _translate("Form", "PKR"))
        self.TOBOX.setItemText(1, _translate("Form", "USD"))
        self.TOBOX.setItemText(2, _translate("Form", "CAD"))
        self.TOBOX.setItemText(3, _translate("Form", "PKR"))
        self.CONVERSIONBOX.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.AMOUNTBOX.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


    def clicked(self):
        print("CLICKED")
        TO = self.TOBOX.currentText()
        FROM = self.FROMBOX.currentText()
        AMOUNT = int(self.AMOUNTBOX.toPlainText())
        self.CONVERSIONBOX.setText(CurrencyConverter.driver(FROM, TO, AMOUNT))

    def closed(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    Form.setObjectName("CurrenSea Converter")
    Form.show()
    sys.exit(app.exec_())
