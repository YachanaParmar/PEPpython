FILE_NAME = "employees.txt"

def add_employee():
    name = input("Enter name: ")
    if is_duplicate(name):
        print("Employee already exists!")
        return
    
    age = input("Enter age: ")
    designation = input("Enter designation (Programmer/Manager/Tester): ").lower()

    if designation not in ["programmer", "manager", "tester"]:
        print("Invalid designation.")
        return

    # Set salary based on designation
    if designation == "programmer":
        salary = 25000
    elif designation == "manager":
        salary = 30000
    elif designation == "tester":
        salary = 20000

    # Write to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{designation},{salary}\n")

    print("Employee added successfully.")


def is_duplicate(name):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                existing_name = line.strip().split(",")[0]
                if existing_name.lower() == name.lower():
                    return True
    except FileNotFoundError:
        return False
    return False


def display_employees():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No employee data found.")
                return
            for line in lines:
                name, age, designation, salary = line.strip().split(",")
                print(f"Name: {name}, Age: {age}, Designation: {designation.capitalize()}, Salary: ₹{salary}")
    except FileNotFoundError:
        print("No employee data found.")


def raise_salary():
    name = input("Enter employee name to raise salary: ")
    updated_lines = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[0].lower() == name.lower():
                    try:
                        percentage = float(input("Enter percentage to raise salary (max 30%): "))
                        if percentage > 30:
                            print("Error: Cannot increase salary by more than 30%.")
                            return
                        salary = int(parts[3])
                        new_salary = salary + int(salary * percentage / 100)
                        updated_line = f"{parts[0]},{parts[1]},{parts[2]},{new_salary}\n"
                        updated_lines.append(updated_line)
                        found = True
                        print(f"Salary updated to ₹{new_salary}")
                    except ValueError:
                        print("Invalid percentage input.")
                        return
                else:
                    updated_lines.append(line)
    except FileNotFoundError:
        print("No data found.")
        return

    if not found:
        print("Employee not found.")
        return

    # Write updated data back to file
    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)


# ===== Main Menu Loop =====
while True:
    print("\n1. Create")
    print("2. Display")
    print("3. Raise Salary")
    print("4. Exit")
    choice = input("Press your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        raise_salary()
    elif choice == "4":
        print("Thank you for using this application.")
        break
    else:
        print("Invalid option. Try again.")
