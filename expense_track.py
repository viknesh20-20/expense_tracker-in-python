import json
import datetime

FILE_NAME = "C:\\expense_tracker\\expense_data.json"


def load_expense():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expense(expense):
    with open(FILE_NAME, "w") as file:
        json.dump(expense, file, indent=4)


def add_expense(expense):
    description = input("Enter Description:")
    amount = float(input("Enter amount:"))
    date = input("Enter date(dd-mm-yyyy) (or) press enter for today:")
    if not date:
        date = datetime.date.today().strftime("%d-%m-20%y")
    exp_id = str(int(max(expense.keys(), default=0)) + 1)
    expense[exp_id] = {"description": description, "amount": amount, "date": date}
    print(f"The expense added {exp_id}")


def view_expense(expense):
    print(f"{'ID':<5}{'Description':<20}{'Amount':<10}{'Date':<12}")
    for id1, data in expense.items():
        print(f"{id1:<5}{data['description']:<20}{data['amount']:<10}{data['date']:<12}")
    print()


def monthly_expenditure(expense):
    tot = 0
    m_y = input("Enter month and year(mm-yyyy):")
    for id1, data in expense.items():
        if m_y in data["date"]:
            tot += data['amount']
    print(f"Expenditure for the month {m_y} is {tot}")


def edit_expense(expense):
    id1 = input("Enter the expense id:")
    if id1 not in expense:
        print("Invalid Id")
        return
    print(f"Current data: {expense[id1]}")
    ch1 = input("Do you want to modify or delete(m\\d):").lower()
    if ch1 == "m":
        description = input("Enter Description (or) press enter to skip:")
        if description:
            expense[id1]["description"] = description
        amount = input("Enter amount (or) press enter to skip:")
        if amount:
            expense[id1]["amount"] = float(amount)
        date = input("Enter date(dd-mm-yyyy) (or) press enter for today:")
        if not date:
            date = datetime.date.today().strftime("%d-%m-%y")
        expense[id1]["date"] = date
        print(f"The data is modified for {id1}")
    elif ch1 == 'd':
        del expense[id1]
        print(f"{id1} is deleted successfully")


expense = load_expense()
print("\t\tExpense Tracker")
while 1:
    print()
    print("1.View Expense")
    print("2.Add Expense")
    print("3.Edit Expense")
    print("4.Monthly Expense")
    print("5.Exit")
    ch = int(input("Choose a option(1,2,3,4):"))
    if ch == 1:
        view_expense(expense)
    elif ch == 2:
        add_expense(expense)
    elif ch == 3:
        edit_expense(expense)
    elif ch == 4:
        monthly_expenditure(expense)
    elif ch == 5:
        save_expense(expense)
        quit(0)
    else:
        print("Enter right option!")
