########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from gui_interface_pyqt5_sqlite.ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
from gui_interface_pyqt5_sqlite.funcao import AppFunctions
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################



########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        # settings = QSettings()
        # # CHANGE THE THEME NAME IN SETTINGS
        # # Use one of the app themes from your JSON file
        # settings.setValue("THEME", "Defaut-Dark")
            
        # # RE APPLY THE NEW SETINGS
        # # CompileStyleSheet might also work
        # # CompileStyleSheet.applyCompiledSass(self)
        # QAppSettings.updateAppSettings(self)

        #dataBase
        self.parentDirectory = os.getcwd()
        dir_data = os.path.join(self.parentDirectory, 'DataBase\\')
        dbFolder =dir_data + 'Spinn_DB.db'
        # dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'DataBase\Spinn_DB.db'))
        AppFunctions.main(dbFolder)
        AppFunctions.displayUsers(self, AppFunctions.get_users(dbFolder))
        self.ui.addUsuarioBtn.clicked.connect(lambda: AppFunctions.insert_users(self, dbFolder))


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
