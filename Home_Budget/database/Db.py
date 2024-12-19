import MySQLdb as mdb


class Db:
    def __init__(self):
        self.con = mdb.connect(
            host="localhost",
            user="root",
            password="",
            db="HomeBudget",
            charset="utf8"
        )
        self.cursor = self.con.cursor()

    def calculate_monthly_budget(self, year, month):
        """
            Рассчитывает бюджет по категориям и подкатегориям расходов за месяц и год.
            Параметры:
                year (int): Год
                month (int): Месяц
            Возвращает:
                list: Список словарей (категория, расходы)
            """
        query = """
        SELECT ec.Name, SUM(e.Quantity * e.Price) AS TotalAmount
        FROM Expenses e
        JOIN Sections s ON e.SectionID = s.SectionID
        JOIN ExpenseCategories ec ON s.CategoryID = ec.CategoryID
        WHERE YEAR(e.Date) = %s AND MONTH(e.Date) = %s
        GROUP BY ec.Name
        """
        self.cursor.execute(query, (year, month))
        results = self.cursor.fetchall()
        return results

    def calculate_monthly_budget_all(self, year, month):
        """
            Рассчитывает бюджет по категориям и подкатегориям расходов за месяц и год.
            Параметры:
                year (int): Год
                month (int): Месяц
            Возвращает:
                list: Список словарей (категория, подкатегория, расходы)
            """
        query = """
        SELECT
            ec.Name AS category,               -- Категория
            s.Name AS subcategory,             -- Раздел (подкатегория)
            SUM(e.Quantity * e.Price) AS total_amount -- Сумма расходов
        FROM
            ExpenseCategories ec
        LEFT JOIN
            Sections s ON ec.CategoryID = s.CategoryID
        LEFT JOIN
            Expenses e ON s.SectionID = e.SectionID
        WHERE
            YEAR(e.Date) = %s AND MONTH(e.Date) = %s
        GROUP BY
            ec.Name, s.Name
        ORDER BY
            ec.Name, s.Name;
        """
        self.cursor.execute(query, (year, month))
        results = self.cursor.fetchall()

        return results

    def get_available_years_and_months(self):
        """Возвращает доступные года и месяцы из бд"""
        query = """
        SELECT DISTINCT YEAR(Date) AS Year, MONTH(Date) AS Month
        FROM Expenses
        ORDER BY Year, Month
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        years = sorted(set(row[0] for row in results))
        months = sorted(set(row[1] for row in results))

        # Переводим номера месяцев в названия
        month_names = [
            "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ]
        months_named = [month_names[month - 1] for month in months]

        return years, months_named

