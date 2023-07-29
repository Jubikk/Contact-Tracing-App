# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from contact_tracing_form import ContactTracingForm
from contact_tracing_data import ContactTracingData
from admin_window import AdminWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("COVID-19 Contact Tracing App")
        self.setFixedSize(800, 600)

        # Create actions for the menu bar
        new_form_action = QAction(QIcon("icons/new_form.png"), "New Form", self)
        new_form_action.triggered.connect(self.new_form)

        save_data_action = QAction(QIcon("icons/save_data.png"), "Save Data", self)
        save_data_action.triggered.connect(self.save_data)

        load_data_action = QAction(QIcon("icons/load_data.png"), "Load Data", self)
        load_data_action.triggered.connect(self.load_data)

        admin_action = QAction(QIcon("icons/admin.png"), "Admin", self)
        admin_action.triggered.connect(self.admin)

        exit_action = QAction(QIcon("icons/exit.png"), "Exit", self)
        exit_action.triggered.connect(self.close)

        # Create menu bar and add actions
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(new_form_action)
        file_menu.addAction(save_data_action)
        file_menu.addAction(load_data_action)
        file_menu.addAction(exit_action)

        admin_menu = menu_bar.addMenu("Admin")
        admin_menu.addAction(admin_action)

        # Create toolbar and add actions
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(new_form_action)
        toolbar.addAction(save_data_action)
        toolbar.addAction(load_data_action)
        toolbar.addAction(admin_action)
        toolbar.addAction(exit_action)

        # Create a central widget and set it as the main window's central widget
        self.central_widget = ContactTracingData()
        self.setCentralWidget(self.central_widget)

    def new_form(self):
        form = ContactTracingForm()
        form.exec_()
        self.central_widget.refresh()

    def save_data(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Data", "", "CSV Files (*.csv)")
        if filename:
            if self.central_widget.save_data(filename):
                QMessageBox.information(self, "Save Data", "Data saved successfully!")
            else:
                QMessageBox.warning(self, "Save Data", "Error saving data!")

    def load_data(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Data", "", "CSV Files (*.csv)")
        if filename:
            if self.central_widget.load_data(filename):
                QMessageBox.information(self, "Load Data", "Data loaded successfully!")
            else:
                QMessageBox.warning(self, "Load Data", "Error loading data!")

    def admin(self):
        admin_window = AdminWindow()
        admin_window.exec_()