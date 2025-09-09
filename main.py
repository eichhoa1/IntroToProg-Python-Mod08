# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Adam Eichholz, 9/3/2025, Converted script into a multi-mode application.
# Adam Eichholz, 9/8/2025, Added testing functions.
# ------------------------------------------------------------------------------------------------- #


import json
from datetime import date
try:
    if __name__ == "__main__":
        import data_classes as data
        import processing_classes as proc
        import presentation_classes as pres
    else:
        raise Exception("This file starts the application and should not be imported.")
except Exception as e:
    print(e.__str__())


# Beginning of the main body of this script
try:
    data.employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME,
                                                       employee_data=data.employees,
                                                       employee_type=data.Employee)  # Note this is the class name (ignore the warning)

except FileNotFoundError as e:
    pres.IO.output_error_messages(e)
except Exception as e:
    pres.IO.output_error_messages(e)


# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=data.employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=data.employees, employee_type=data.Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=data.employees)
            print(f"Data was saved to the {data.FILE_NAME} file.")
        except Exception as e:
            proc.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop