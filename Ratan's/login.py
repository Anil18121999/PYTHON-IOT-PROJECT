# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RQtSignin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from Administration import Ui_Administration
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 70, 541, 361))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 341))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-image: url(Images/17973908.jpg);\n"
"border-radius: 30px;\n"
"border: 1px solid black;"
)
        self.label.setMidLineWidth(9)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 441, 41))
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("border-radius: 10px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,  stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"border:1px solid black;")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(100, 110, 331, 161))
        self.frame.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"\n"
"border-radius: 15px;\n"
"border:2px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.LoginID = QtWidgets.QLineEdit(self.frame)
        self.LoginID.setGeometry(QtCore.QRect(130, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LoginID.setFont(font)
        self.LoginID.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LoginID.setAutoFillBackground(False)
        self.LoginID.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid black;")
        self.LoginID.setMaxLength(12)
        self.LoginID.setCursorPosition(0)
        self.LoginID.setPlaceholderText("")
        self.LoginID.setClearButtonEnabled(False)
        self.LoginID.setObjectName("LoginID")
        self.PassWord = QtWidgets.QLineEdit(self.frame)
        self.PassWord.setGeometry(QtCore.QRect(130, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PassWord.setFont(font)
        self.PassWord.setAutoFillBackground(False)
        self.PassWord.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid black;")
        self.PassWord.setMaxLength(16)
        self.PassWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassWord.setCursorPosition(0)
        self.PassWord.setPlaceholderText("")
        self.PassWord.setClearButtonEnabled(False)
        self.PassWord.setObjectName("pass")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(130, 102, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 15px;")
        self.loginButton.setObjectName("loginButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: none;")
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(80, 80, 300, 20))
        self.label_5.hide()
        
        
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(330, 80, 191, 21))
        self.label_6.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.label_6.setObjectName("DateAndTime")
        self.resetButton = QtWidgets.QPushButton(self.frame)
        self.resetButton.setGeometry(QtCore.QRect(240, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 15px;")
        self.resetButton.setObjectName("resetButton")
        
        self.sdButton = QtWidgets.QPushButton(self.widget)
        self.sdButton.setGeometry(QtCore.QRect(300, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sdButton.setFont(font)
        self.sdButton.setStyleSheet("background-color: rgb(255, 142, 144);\n"
"border-radius: 15px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.sdButton.setObjectName("sdButton")
        self.rebootButton = QtWidgets.QPushButton(self.widget)
        self.rebootButton.setGeometry(QtCore.QRect(420, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rebootButton.setFont(font)
        self.rebootButton.setStyleSheet("background-color: rgb(255, 142, 144);\n"
"border-radius: 15px;\n"
"border: 1px solid black;")
        self.rebootButton.setObjectName("rebootButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Page"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">RATAN\'S ELECTRONICS</span></p></body></html>"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))
        self.label_2.setText(_translate("MainWindow", "Login ID :"))
        self.label_4.setText(_translate("MainWindow", "Password :"))
        self.label_5.setText(_translate("MainWindow", "Please Enter LoginID And Password"))
        self.resetButton.setText(_translate("MainWindow", "RESET"))
        self.sdButton.setText(_translate("MainWindow", "SHUT DOWN"))
        self.rebootButton.setText(_translate("MainWindow", "REBOOT"))
        self.resetButton.clicked.connect(self.reset_fun)
        self.loginButton.clicked.connect(self.login)
        self.label_6.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.timer=QtCore.QTimer()
        self.timer.start(1)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.device_date)
        self.input_fild()

        
    def input_fild(self):
        self.login_id = str(self.LoginID.text())
        
        self.Pas_=str(self.PassWord.text())



        print("input field data :" , "Login id :"+str(self.login_id)+" Passwod :"+str(self.Pas_))
         
        

       
    def device_date(self):
        self.label_6.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))


    def login(self):

        self.go_ahead=0
        
        self.login_id = str(self.LoginID.text())
        
        self.Pas_=str(self.PassWord.text())
        #self.input_fild()""
        if( str(self.login_id) == "SU"  and str(self.Pas_) == "12345"):
                self.go_ahead = 1 

        else:
                print("Login id :"+str(self.LoginID.text())+" Passwod :"+str(self.PassWord.text()))
                connection = sqlite3.connect("RATAN'S_ELECTRONICS.db")
                results = connection.execute("SELECT LOGIN_ID, PASSWORD FROM USER_MST WHERE LOGIN_ID='"+str(self.login_id)+"' and PASSWORD='"+str(self.Pas_)+"'") 
                
                for x in results:
                        if ( str(x[0]) == str(self.login_id) and str(x[1]) == str(self.Pas_)):
                                print("USER_ID :"+str(x[0])+"   PASSWORD :"+str(x[1]))
                                self.go_ahead=1
                        else: 
                                self.go_ahead = 0 
                 
                     
   
        if (int(self.go_ahead) == 1): 
                      
                self.new_window_administration()
                 
                connection = sqlite3.connect("RATAN'S_ELECTRONICS.db")
                cursor = connection.cursor()
                cursor.execute("UPDATE GLOBAL_VAR SET LOGIN_ID= '"+str(self.login_id)+"',  PASSWORD= '"+str(self.Pas_)+"' ") 
                connection.commit()
                connection.close() 
                # print("AFTER LOGIN ID :"+str(self.login_id)+"  Passwod :"+str(self.Pas_))


        elif (self.login_id == "" and self.Pas_ == "" ):
             self.label_5.setText("Please Enter Credentials") 
             self.label_5.show()
             

        elif (self.login_id == ""):
             self.label_5.setText("Please Enter Login ID") 
             self.label_5.show()
                  

        elif (self.Pas_ == ""):
             self.label_5.setText("Please Enter Password") 
             self.label_5.show()          
        else:
             self.label_5.setText("Incorrect Credentials") 
             self.label_5.show()

             
        

           
    def new_window_administration(self): 
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_Administration()    
        self.ui.setupUi(self.window)
        self.window.show()
    


        # self.login()
    def reset_fun(self):
        self.LoginID.setText("")
        self.PassWord.setText("")
        self.label_5.hide()
         

# import resource file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
