
import sys
import os 
from untitled_python import * 
from PyQt5.QtWidgets import *
 
from PyQt5.QtCore import *
from mail_ara_python import * 
from Hakkinda_python import * 
app =QApplication (sys.argv)


pen_ana = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pen_ana)

pen_ana.show()





#--------------------------HAKKIDA---------------#
pen_kakında =QDialog()
ui_hakkinda = Ui_Dialog()
ui_hakkinda.setupUi(pen_kakında)



def hakkinda ():
    pen_kakında .show()


#------------------------Dosya aç --------------#



#----------------------------Mail Ara -------------#
pen_mail_ara  = QWidget()
ui_mail_ara = Ui_mail_ara()
ui_mail_ara.setupUi(pen_mail_ara)




def mail_ara ():
    pen_mail_ara.show()
    


def  ac ():
    dosya = QFileDialog.getOpenFileName("action_Ac",os.getenv("Desktop"))
    with open(dosya[1],"r+") as file:
        ui.textEdit.setText(file.read())
    
        


#--------------------Sinyal Slot Bağlantısı---------- #
ui.actionHakkinda.triggered.connect(hakkinda)
ui.action_Ac.triggered.connect(ac)
ui.pbt_ara.clicked.connect(mail_ara)

sys.exit(app.exec_())


