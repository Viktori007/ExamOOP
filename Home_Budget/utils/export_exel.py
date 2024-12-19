import openpyxl


def export_to_excel(data, year, month):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Category", "Amount", "Percentage"])
    total_budget = float(data[-1]['amount'])
    for row in data:
        ws.append([row["category"], f"{row['amount']:.2f}", f"{row['amount'] / total_budget * 100:.2f}%"])
    filename = f"Monthly_Budget_{year}_{month}.xlsx"
    wb.save(filename)
    print(f"Файл сохранён: {filename}")
