class Expense:
    def __init__(self, category, amount, date, expense_id=None, category_id=None):
        self.category = category
        self.amount = amount
        self.date = date
        self.expense_id = expense_id
        self.category_id = category_id

    def __str__(self):
        return f"{self.date}: {self.category} — {self.amount:.2f}"

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def expense_id(self):
        return self._expense_id

    @expense_id.setter
    def expense_id(self, value):
        self._expense_id = value

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value