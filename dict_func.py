def employee_print(employee_info):
    print("Name:", employee_info["Name"])  
    print("Salary:", employee_info["Salary"])
    print("Role:", employee_info["Role"])

    for key in employee_info:
        print(key, employee_info[key])  