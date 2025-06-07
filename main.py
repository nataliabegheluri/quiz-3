import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from quiz3 import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dasruleba.clicked.connect(self.check_answers)

#პასუხების შემოწმება:
    def check_answers(self):
        # კითხვა 1
        if self.tbilisi.isChecked():
            self.pasuxi1.setText("სწორია")
            self.pasuxi1.show()
        elif self.qutaisi.isChecked() or self.telavi.isChecked():
            self.pasuxi1.setText("არასწორია")
            self.pasuxi1.show()
        else:
            self.pasuxi1.hide()

        # კითხვა 2
        if self.shavizghva.isChecked():
            self.pasuxi2.setText("სწორია")
            self.pasuxi2.show()
        elif self.kaspiis.isChecked() or self.xmeltashua.isChecked():
            self.pasuxi2.setText("არასწორია")
            self.pasuxi2.show()
        else:
            self.pasuxi2.hide()

            # კითხვა 3:
        if self.xuti.isChecked():
            self.pasuxi3.setText("სწორია")
            self.pasuxi3.show()
        elif self.erti.isChecked() or self.shvidi.isChecked():
            self.pasuxi3.setText("არასწორია")
            self.pasuxi3.show()
        else:
            self.pasuxi3.hide()

            # კითხვა 4:
        if self.xinkali.isChecked():
            self.pasuxi4.setText("სწორია")
            self.pasuxi4.show()
        elif self.pica.isChecked() or self.burgeri.isChecked():
            self.pasuxi4.setText("არასწორია")
            self.pasuxi4.show()
        else:
            self.pasuxi4.hide()

            # კითხვა 5:
        if self.tamari.isChecked():
            self.pasuxi5.setText("სწორია")
            self.pasuxi5.show()
        elif self.rusudani.isChecked() or self.nino.isChecked():
            self.pasuxi5.setText("არასწორია")
            self.pasuxi5.show()
        else:
            self.pasuxi5.hide()


app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())