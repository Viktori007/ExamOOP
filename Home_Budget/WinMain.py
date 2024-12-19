from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from database.Budget import load_monthly_budget_all, load_monthly_budget
from database.Db import Db
from utils.export_exel import export_to_excel


class WinMain(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(609, 483)
        self.setStyleSheet("background-color: rgb(228, 236, 255);")
        self.db = Db()

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.model = QStandardItemModel()
        self.tableView_expence.setModel(self.model)
        self.pushButton_load.clicked.connect(self.load_budget_data)
        self.pushButton_export_exel.clicked.connect(self.export_to_excel)

        self.populate_comboboxes()

    def load_budget_data(self):
        """Загрузка данных о расходах на основе выбранных месяца и года"""
        month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                       "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        month = self.comboBox_month.currentText()
        month_int = month_names.index(month) + 1
        year = int(self.comboBox_year.currentText())

        budget_data = load_monthly_budget_all(year, month_int)
        self.display_data_in_table(budget_data)

    def display_data_in_table(self, data):
        """Отображение категорий и их содержимого в QTableView"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Категория/Раздел", "Сумма"])

        categories = {}
        for row in data:
            if row["category"] not in categories:
                categories[row["category"]] = 0
            categories[row["category"]] += row["amount"]

        for category, total_amount in categories.items():
            category_item = QStandardItem(category)
            total_amount_item = QStandardItem(f"{total_amount:.2f}")

            category_item.setBackground(QtGui.QColor("lightblue"))
            total_amount_item.setBackground(QtGui.QColor("lightblue"))
            self.model.appendRow([category_item, total_amount_item])

            for row in data:
                if row["category"] == category:
                    subcategory_item = QStandardItem(f"  {row['subcategory']}")  # Отступ для подкатегорий
                    amount_item = QStandardItem(f"{row['amount']:.2f}")
                    self.model.appendRow([subcategory_item, amount_item])

        header = self.tableView_expence.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def populate_comboboxes(self):
        """Заполняем списки значениями месяца и года"""
        years_int, months = self.db.get_available_years_and_months()
        years = [str(year) for year in years_int]
        self.comboBox_month.addItems(months)
        self.comboBox_year.addItems(years)

    def export_to_excel(self):
        """Экспорт данных в Excel"""
        month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                       "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        month = self.comboBox_month.currentText()
        month_int = month_names.index(month) + 1
        year = int(self.comboBox_year.currentText())

        budget_data = load_monthly_budget(year, month_int)
        export_to_excel(budget_data, year, month_int)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_export_exel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_exel.setGeometry(QtCore.QRect(450, 430, 121, 31))
        self.label_home_budget = QtWidgets.QLabel(self.centralwidget)
        self.label_home_budget.setGeometry(QtCore.QRect(170, 20, 231, 41))
        self.label_home_budget.setMaximumSize(QtCore.QSize(16777215, 41))
        self.label_home_budget.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.tableView_expence = QtWidgets.QTableView(self.centralwidget)
        self.tableView_expence.setGeometry(QtCore.QRect(50, 190, 461, 221))
        self.label_month = QtWidgets.QLabel(self.centralwidget)
        self.label_month.setGeometry(QtCore.QRect(100, 70, 131, 21))
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(350, 70, 131, 21))
        self.comboBox_month = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_month.setGeometry(QtCore.QRect(80, 100, 141, 31))
        self.comboBox_year = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_year.setGeometry(QtCore.QRect(330, 100, 141, 31))
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(20, 430, 121, 31))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 150, 161, 31))

        self.setWindowTitle(_translate("MainWindow", "Home Budget"))
        self.pushButton_export_exel.setText(_translate("MainWindow", "Вывести в Exel"))
        self.label_home_budget.setText(_translate("MainWindow", "Домашний бюджет"))
        self.label_month.setText(_translate("MainWindow", "Выберите месяц"))
        self.label_year.setText(_translate("MainWindow", "Выберите год"))
        self.pushButton_load.setText(_translate("MainWindow", "Загрузить"))
