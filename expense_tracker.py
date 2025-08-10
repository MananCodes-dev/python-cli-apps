import csv
import datetime

FILE = 'expenses.csv'

def add_expense():
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    note = input("Enter a note for the expense: ")

    with open(FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, category, amount, note])
    print("Expense added successfully.")

def view_expenses():
    try:
        with open(FILE, 'r') as file:
            reader = csv.reader(file)
            print("\nDate\t\tCategory\tAmount\tNote")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
                total += float(row[2])
            print(f"Total Expenses: {total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("Exiting the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")