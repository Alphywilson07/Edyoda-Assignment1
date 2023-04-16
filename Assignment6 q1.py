import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name} ({self.dob}), {self.height}, {self.city}, {self.state}"

# Read data from employee.json file
with open('employee.json') as f:
    data = json.load(f)

# Create a list of Employee objects
employees = []
for emp in data['employees']:
    emp_obj = Employee(emp['Name'], emp['DOB'], emp['Height'], emp['City'], emp['State'])
    employees.append(emp_obj)

# Print the list of Employee objects
for emp in employees:
    print(emp)
