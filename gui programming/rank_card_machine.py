# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rank_card_machine.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 494)
        MainWindow.setMinimumSize(QtCore.QSize(543, 494))
        MainWindow.setMaximumSize(QtCore.QSize(543, 494))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.rank_card_machine = QtWidgets.QLabel(self.centralwidget)
        self.rank_card_machine.setMinimumSize(QtCore.QSize(471, 20))
        self.rank_card_machine.setMaximumSize(QtCore.QSize(471, 20))
        self.rank_card_machine.setAlignment(QtCore.Qt.AlignCenter)
        self.rank_card_machine.setObjectName("rank_card_machine")
        self.gridLayout.addWidget(self.rank_card_machine, 0, 0, 1, 6)
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setMinimumSize(QtCore.QSize(91, 31))
        self.name.setMaximumSize(QtCore.QSize(91, 31))
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)
        self.nameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.nameBox.setObjectName("nameBox")
        self.gridLayout.addWidget(self.nameBox, 1, 1, 1, 2)
        self.roll_no = QtWidgets.QLabel(self.centralwidget)
        self.roll_no.setMinimumSize(QtCore.QSize(91, 31))
        self.roll_no.setMaximumSize(QtCore.QSize(91, 31))
        self.roll_no.setObjectName("roll_no")
        self.gridLayout.addWidget(self.roll_no, 2, 0, 1, 1)
        self.rollnoBox = QtWidgets.QLineEdit(self.centralwidget)
        self.rollnoBox.setObjectName("rollnoBox")
        self.gridLayout.addWidget(self.rollnoBox, 2, 1, 1, 1)
        self.sex = QtWidgets.QLabel(self.centralwidget)
        self.sex.setMinimumSize(QtCore.QSize(71, 31))
        self.sex.setMaximumSize(QtCore.QSize(71, 31))
        self.sex.setObjectName("sex")
        self.gridLayout.addWidget(self.sex, 2, 2, 1, 1)
        self.Female = QtWidgets.QRadioButton(self.centralwidget)
        self.Female.setMinimumSize(QtCore.QSize(61, 31))
        self.Female.setMaximumSize(QtCore.QSize(61, 31))
        self.Female.setObjectName("Female")
        self.gridLayout.addWidget(self.Female, 2, 3, 1, 1)
        self.Male = QtWidgets.QRadioButton(self.centralwidget)
        self.Male.setMinimumSize(QtCore.QSize(61, 31))
        self.Male.setMaximumSize(QtCore.QSize(61, 31))
        self.Male.setObjectName("Male")
        self.gridLayout.addWidget(self.Male, 2, 4, 1, 1)
        self.Others = QtWidgets.QRadioButton(self.centralwidget)
        self.Others.setMinimumSize(QtCore.QSize(71, 31))
        self.Others.setMaximumSize(QtCore.QSize(71, 31))
        self.Others.setObjectName("Others")
        self.gridLayout.addWidget(self.Others, 2, 5, 1, 1)
        self.enter_the_student_details = QtWidgets.QLabel(self.centralwidget)
        self.enter_the_student_details.setMinimumSize(QtCore.QSize(471, 20))
        self.enter_the_student_details.setMaximumSize(QtCore.QSize(471, 20))
        self.enter_the_student_details.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_the_student_details.setObjectName("enter_the_student_details")
        self.gridLayout.addWidget(self.enter_the_student_details, 3, 0, 1, 6)
        self.lang = QtWidgets.QLabel(self.centralwidget)
        self.lang.setMinimumSize(QtCore.QSize(91, 31))
        self.lang.setMaximumSize(QtCore.QSize(91, 31))
        self.lang.setObjectName("lang")
        self.gridLayout.addWidget(self.lang, 4, 0, 1, 1)
        self.langBox = QtWidgets.QLineEdit(self.centralwidget)
        self.langBox.setObjectName("langBox")
        self.gridLayout.addWidget(self.langBox, 4, 1, 1, 2)
        self.eng = QtWidgets.QLabel(self.centralwidget)
        self.eng.setMinimumSize(QtCore.QSize(91, 31))
        self.eng.setMaximumSize(QtCore.QSize(91, 31))
        self.eng.setObjectName("eng")
        self.gridLayout.addWidget(self.eng, 5, 0, 1, 1)
        self.engBox = QtWidgets.QLineEdit(self.centralwidget)
        self.engBox.setObjectName("engBox")
        self.gridLayout.addWidget(self.engBox, 5, 1, 1, 2)
        self.mat = QtWidgets.QLabel(self.centralwidget)
        self.mat.setMinimumSize(QtCore.QSize(91, 31))
        self.mat.setMaximumSize(QtCore.QSize(91, 31))
        self.mat.setObjectName("mat")
        self.gridLayout.addWidget(self.mat, 6, 0, 1, 1)
        self.matBox = QtWidgets.QLineEdit(self.centralwidget)
        self.matBox.setObjectName("matBox")
        self.gridLayout.addWidget(self.matBox, 6, 1, 1, 2)
        self.sci = QtWidgets.QLabel(self.centralwidget)
        self.sci.setMinimumSize(QtCore.QSize(91, 31))
        self.sci.setMaximumSize(QtCore.QSize(91, 31))
        self.sci.setObjectName("sci")
        self.gridLayout.addWidget(self.sci, 7, 0, 1, 1)
        self.sciBox = QtWidgets.QLineEdit(self.centralwidget)
        self.sciBox.setObjectName("sciBox")
        self.gridLayout.addWidget(self.sciBox, 7, 1, 1, 2)
        self.soc = QtWidgets.QLabel(self.centralwidget)
        self.soc.setMinimumSize(QtCore.QSize(91, 31))
        self.soc.setMaximumSize(QtCore.QSize(91, 31))
        self.soc.setObjectName("soc")
        self.gridLayout.addWidget(self.soc, 8, 0, 1, 1)
        self.socBox = QtWidgets.QLineEdit(self.centralwidget)
        self.socBox.setObjectName("socBox")
        self.gridLayout.addWidget(self.socBox, 8, 1, 1, 2)
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setMinimumSize(QtCore.QSize(111, 31))
        self.Enter.setMaximumSize(QtCore.QSize(111, 31))
        self.Enter.setObjectName("Enter")
        self.gridLayout.addWidget(self.Enter, 9, 3, 1, 1)
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setObjectName("Cancel")
        self.gridLayout.addWidget(self.Cancel, 9, 4, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Enter.clicked.connect(MainWindow.update)
        self.Cancel.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.nameBox, self.Female)
        MainWindow.setTabOrder(self.Female, self.Male)
        MainWindow.setTabOrder(self.Male, self.Others)
        MainWindow.setTabOrder(self.Others, self.rollnoBox)
        MainWindow.setTabOrder(self.rollnoBox, self.langBox)
        MainWindow.setTabOrder(self.langBox, self.engBox)
        MainWindow.setTabOrder(self.engBox, self.matBox)
        MainWindow.setTabOrder(self.matBox, self.sciBox)
        MainWindow.setTabOrder(self.sciBox, self.socBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rank_card_machine.setText(_translate("MainWindow", "RANK CARD MACHINE"))
        self.name.setText(_translate("MainWindow", "Name                :"))
        self.roll_no.setText(_translate("MainWindow", "Roll No             :"))
        self.sex.setText(_translate("MainWindow", "Sex / Gender"))
        self.Female.setText(_translate("MainWindow", "Female"))
        self.Male.setText(_translate("MainWindow", "Male"))
        self.Others.setText(_translate("MainWindow", "Others"))
        self.enter_the_student_details.setText(_translate("MainWindow", "ENTER THE STUDENTS MARK DETAILS"))
        self.lang.setText(_translate("MainWindow", "Language        :"))
        self.eng.setText(_translate("MainWindow", "English            :"))
        self.mat.setText(_translate("MainWindow", "Maths             :"))
        self.sci.setText(_translate("MainWindow", "Science          :"))
        self.soc.setText(_translate("MainWindow", "Social             :"))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.Cancel.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

