import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
import os 
seriallist = os.listdir("/sys/class/tty")
serialmem = []
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
                
        combo = QComboBox(self)
        #combo.addItem("Apple")
        #combo.addItem("Pear")
        #combo.addItem("Lemon")
        for i in range(0,len(seriallist)):
              if len(str(seriallist[i]).split("USB")) >= 2:
                        serialmem.append(str(seriallist[i])) 
              if len(str(seriallist[i]).split("ACM")) >=2:
                        serialmem.append(str(seriallist[i])) 
        combo.addItems(serialmem)   #Add list of serial port 
        combo.move(50, 50)

        self.qlabel = QLabel(self)
        self.qlabel.move(50,16)

        combo.activated[str].connect(self.onChanged)      

        self.setGeometry(50,50,320,200)
        self.setWindowTitle("QLineEdit Example")
        self.show()

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
