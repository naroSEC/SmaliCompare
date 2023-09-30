import sys
import os
from PyQt5.QtWidgets import *
from ui_setting import Ui_MainWindow
from CompareSmaliCode import *


class MainClass(QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.compareDirPath_1 = None
        self.compareDirPath_2 = None
        
        self.initUI()

    def initUI(self):
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)        
        self.main_ui.pushButton.clicked.connect(self.openDirectoryDialog)
        self.main_ui.pushButton_2.clicked.connect(self.openDirectoryDialog)
        self.main_ui.pushButton_3.clicked.connect(self.compareStart)

        self.show()

    def openDirectoryDialog(self):
        current_directory = os.getcwd()
        sender_button = self.sender()

        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.ShowDirsOnly

        if sender_button == self.main_ui.pushButton:
            self.compareDirPath_1 = QFileDialog.getExistingDirectory(self, "디렉터리 선택", current_directory, options=options)
            self.main_ui.textBrowser.append(f'1번 디렉터리 : {self.compareDirPath_1}')
        elif sender_button == self.main_ui.pushButton_2:
            self.compareDirPath_2 = QFileDialog.getExistingDirectory(self, "디렉터리 선택", current_directory, options=options)
            self.main_ui.textBrowser.append(f'2번 디렉터리 : {self.compareDirPath_2}')


    def compareStart(self):
        if self.compareDirPath_1 is not None and self.compareDirPath_2 is not None and self.compareDirPath_1 and self.compareDirPath_2:
            compare_file_list_1 = search_in_directory(self.compareDirPath_1)
            compare_file_list_2 = search_in_directory(self.compareDirPath_2)
            
            remove_or_add_smali = compare_smali(compare_file_list_1, compare_file_list_2)
            self.main_ui.progressBar.setValue(20)

            compare_func_1 = read_smali_Files(compare_file_list_1, self.compareDirPath_1)
            compare_func_2 = read_smali_Files(compare_file_list_2, self.compareDirPath_2)
            self.main_ui.progressBar.setValue(50)

            change_results = compare_funcs(compare_func_1, compare_func_2)
            self.main_ui.progressBar.setValue(70)

            write_reporting(remove_or_add_smali, change_results)
            self.main_ui.progressBar.setValue(100)

            QMessageBox.information(self, 'Complete!','완료 되었습니다. 저장된 파일을 확인해주세요.', QMessageBox.Yes)

        else:
            QMessageBox.information(self,'Warning','디렉터리를 모두 선택해주세요.', QMessageBox.Yes)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()