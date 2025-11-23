import csv
import os

CSV_FILE = 'data1.csv'

def initialize_csv():
    if not os.path.exists(CSV_FILE) or os.stat(CSV_FILE).st_size == 0:
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['EmpID', 'Name', 'Salary'])

def add_employee_details():
    try:
        n = int(input("Enter number of employees to add: "))
        if n <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        for _ in range(n):
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            salary = input("Enter Employee Salary: ")
            writer.writerow([emp_id, name, salary])
    print(f"{n} Employee(s) added successfully.")

def search_employee_details():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None) # Skip header
            if header is None:
                print("CSV file is empty or header is missing.")
                return

            for row in reader:
                if row and len(row) > 0 and row[0] == emp_id:
                    print(f"Employee Found: ID={row[0]}, Name={row[1]}, Salary={row[2]}")
                    found = True
                    break
    except FileNotFoundError:
        print("data.csv not found. Please add employees first.")
        return
    if not found:
        print("Employee not found.")

def display_all_employee_details():
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None) # Skip header
            if header is None:
                print("No employee details to display.")
                return

            print("\n--- All Employee Details ---")
            for row in reader:
                if row and len(row) > 0: # Ensure row is not empty
                    print(f"EmpID: {row[0]}, Name: {row[1]}, Salary: {row[2]}")
            print("--------------------------")
    except FileNotFoundError:
        print("data.csv not found. Please add employees first.")

def delete_employee_details():
    emp_id_to_delete = input("Enter Employee ID to delete: ")
    rows = []
    found = False
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if header:
                rows.append(header) # Keep header
            for row in reader:
                if row and len(row) > 0 and row[0] == emp_id_to_delete:
                    found = True
                else:
                    rows.append(row)
    except FileNotFoundError:
        print("data.csv not found. No employees to delete.")
        return

    if found:
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print("Employee record deleted successfully.")
    else:
        print("Employee not found.")

def update_employee_details():
    emp_id_to_update = input("Enter Employee ID to update: ")
    rows = []
    found = False
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if header:
                rows.append(header) # Keep header
            for row in reader:
                if row and len(row) > 0 and row[0] == emp_id_to_update:
                    name = input(f"Enter new Name for Employee ID {emp_id_to_update}: ")
                    salary = input(f"Enter new Salary for Employee ID {emp_id_to_update}: ")
                    rows.append([emp_id_to_update, name, salary])
                    found = True
                else:
                    rows.append(row)
    except FileNotFoundError:
        print("data.csv not found. No employees to update.")
        return

    if found:
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print("Employee record updated successfully.")
    else:
        print("Employee not found.")

def main_menu():
    initialize_csv() # Ensure CSV file and header exist

    while True:
        print("\nChoose the following function to be performed:")
        print("1. Add Employee Details")
        print("2. Search Employee Details")
        print("3. Display All Employee Details")
        print("4. Delete Employee Details")
        print("5. Update Employee Details")
        print("6. Exit")

        try:
            opt = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if opt == 1:
            add_employee_details()
        elif opt == 2:
            search_employee_details()
        elif opt == 3:
            display_all_employee_details()
        elif opt == 4:
            delete_employee_details()
        elif opt == 5:
            update_employee_details()
        elif opt == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

# Call the main menu function to start the program
main_menu()