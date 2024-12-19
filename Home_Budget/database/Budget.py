from database.Db import Db


def load_monthly_budget(year, month):
    """Загружаем данные бюджета за указанный месяц и год"""
    db = Db()
    data = db.calculate_monthly_budget(year, month)
    for row in data:
        print({"category": row[0], "amount": float(row[1])})
    budget_data = [{"category": row[0], "amount": float(row[1])} for row in data]
    total_budget = sum(float(row[1]) for row in data)
    budget_data.append({"category": "Итого", "amount": total_budget})
    return budget_data


def load_monthly_budget_all(year, month):
    """Загружаем данные бюджета за указанный месяц и год с подкатегориями"""
    db = Db()
    data = db.calculate_monthly_budget_all(year, month)
    for row in data:
        print({"category": row[0], "subcategory": row[1], "amount": float(row[2])} )
    budget_data = [{"category": row[0], "subcategory": row[1], "amount": float(row[2])} for row in data]
    return budget_data
