import json
from abc import ABC, abstractmethod
from pathlib import Path

# Create Database
database = Path(__file__).resolve().parent /"school_data.json"
data = {
    "students": [], 
    "teachers": []
}

if database.exists():
    with open(database, 'r') as file:
        content = file.read()
        
        if content:
            data = json.loads(content)
    

# Save info in database: 
def save():
    with open(database, 'w') as file:
        json.dump(data, file, indent=4)


class Persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass
    
    @abstractmethod
    def register(self):
        pass
    
    def show_details(self):
        pass
    

class Student(Persons):
    def get_roles(self):
        return "students"
    
    def register(self):
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("Sorry! Student id should not be empty.")
            return
        name = input("Enter student name: ").strip()
        if not name: 
            print("Sorry! Student name should not be empty.")
            return
        
        try:
            age = int(input("Enter student age: ").strip())

            if age <= 0 or age >= 120:
                print("Sorry! student age must be between 1 to 119.")
                return

        except ValueError:
            print("Error! Enter valid student age.")
            return
        
        gender = input("Enter student gender: ").strip()
        if not gender:
            print("Sorry! Gender should not be empty.")
            return
        
        grade = input("Enter student class: ").strip()
        if not grade:
            print("Sorry! Student grade should not be empty.")
            return
        
        address = input("Enter student address: ").strip()
        if not address:
            print("Sorry! Student addrerss should not be empty.")
            return
        
        for student in data['students']:
            if student['student_id'] == student_id:
                print("Sorry! Student id already exist")
                return
        
        # Add Student.
        data['students'].append({
            "student_id":student_id,
            "name": name,
            "age": age,
            "gender": gender,
            "class": grade,
            "address":address,
            "grades": {}  
        })
            
        save()
        print("\nStudent information added successfully.")
    
      
    def show_details(self):
        try:  
            student_id = input("Enter student id: ").strip()
            
            for student in data['students']:
                if student['student_id']==student_id.strip():
                    grades = student['grades']
                    average_marks = sum(grades.values())/len(grades) if grades else 0
                    print(f"\n{student['name']} Data.")
                    print(
                        f"Student Name      : {student['name']}\n"
                        f"Student Age       : {student['age']}\n"
                        f"Student Gender    : {student['gender']}\n"
                        f"Student Class     : {student['class']}\n"
                        f"Student Address   : {student['address']}\n"
                        f"===========================================\n"
                        f"Student Gradde :{grades}\n"
                        f"Student Gradde :{average_marks}\n"
                    )
                    print("Student Information viewed successfully")
                else:
                    print("Sorry! Student information does not exist.1")
        except PermissionError:
            print("Error! You have no permission to add student data.")
        except OSError as err:
            print(f"Error! File system error: {err}")
    
    
    def add_grades(self):
        try: 
            student_id = input("Enter student ID: ").strip()
            if not student_id:
                print("Sorry! Student id should not be empty.")
                return
            subject = input("Enter subject: ").strip()
            if not subject:
                print("Sorry! subject should not be empty.")
                return
            
            try:
                marks = float(input("Enter mark: ").strip())
                if marks<0 or marks>100:
                    print("sorry! student marks should not be less then 0 or more then 100")
                    return
            except ValueError:
                print("Error! Enter valid marks")
                return
            for student in data['students']:
                if student['student_id']==student_id.strip():
                    student['grades'] [subject] = marks
                    save()
                    print("Grade added successfully")
                else:
                    print("Sorry! Student information does not exist.")
                    return
        except PermissionError:
            print("Error! You have no permission to add student marks.")
        except OSError as err:
            print(f"Error! File system error: {err}")            
                
    def update_student(self):
        try:
            student_id_found = False
            student_id = input("Enter student id: ").strip()
            if not student_id:
                print("Sorry! Student id should not be empty.")
                return
            
            for student in data['students']:
                if student['student_id']==student_id.strip():
                    student_id_found = True
                    print(f"\nCurrent {student['name']} information:-")
                    print(
                        f"Student Name      : {student['name']}\n"
                        f"Student Age       : {student['age']}\n"
                        f"Student Gender    : {student['gender']}\n"
                        f"Student Class     : {student['class']}\n"
                        f"Student Address   : {student['address']}\n"
                        # f"===========================================\n"
                        # f"Student Gradde :{student['grades']}\n"
                        # f"Student Gradde :{student['average_marks']}\n"
                    )
                    
                    print(f"\nUpdate {student['name']} information")
                    print("1. for update name.")
                    print("2. for update Age.")
                    print("3. for update Gender.")
                    print("4. for update student class.")
                    print("5. for update Addrerss.")
                    print("6. for update Grades.")
                    print("7. for update Average marks.")
                    
                    try:
                        choice = int(input("Enter number which you want to update: ").strip())
                    except ValueError:
                        print("Error! Enter valid number for update student information.")
                        return
                    
                    if choice==1:
                        name = input("Update student name: ").strip()
                        if not name:
                            print("Sorry! name should not be empty.")
                            return
                        student["name"] = name
                        
                    elif choice ==2:
                        try:
                            age = int(input("Update student age.").strip())
                            if age<=0 or age>=120:
                                print("Sorry! student age must be grater than 0 and less than 119")
                                return
                        except ValueError:
                            print("Error! enter valid student age.")
                            return
                        student['age']= age
                            
                    elif choice == 3:
                        gender = input("Update student gender: ").strip()
                        if not gender:
                            print("Sorry! Student gender should not be empty.")
                            return
                        student["gender"] = gender
                    
                    elif choice == 4:
                        student_class = input("Update student class: ").strip()
                        if not student_class:
                            print("Sorry! Student class should not be empty.")
                            return
                        
                        student["class"] = student_class
                    
                    elif choice == 5:
                        address = input("Update student address: ").strip()
                        if not address:
                            print("Sorry! Student address should not be empty.")
                            return
                        
                        student["address"] = address
                        
                    else:
                        print("Sorry! Please selected a number 1 to 5.")
                        return
                    
                    save()
                    print("Student infromation updated successfully.")
                    return
                
            if not student_id_found:
                print("Sorry! Student information does not exist.")
                return
        except PermissionError:
            print("Error! You have no permission to update student information.")
            return
        
        except OSError as err:
            print(f"Error! File system error: {err}")
        
    def delete_student(self):
        student_id_found = False
        student_id = input("Enter student id for delete information: ").strip()
        if not student_id:
            print("Sorry! Student id should not be empty.")
            return
        
        for index, student in enumerate(data['students']):
            if student['student_id'] == student_id.strip():
                student_id_found = True
                print("\nStudent found")
                print(
                    f"Student Name      : {student['name']}\n"
                    f"Student Age       : {student['age']}\n"
                    f"Student Gender    : {student['gender']}\n"
                    f"Student Class     : {student['class']}\n"
                    f"Student Address   : {student['address']}\n"
                )
                conformation = input("\nAre you sure you want to delete this student? (yes/no): ").strip().lower()
                
                if conformation != "yes":
                    print("\nDelete operation cancelled.")
                    return
                else:
                    data['students'].pop(index)
                    save()
                    print("\nStudent information deleted successfully.")
                    return
        if not student_id_found:
            print("Sorry! Student information does not exist.")
            return
        
        
                
                
                              
            
                    
                
                    
                    
                    
                    
                
                
                
                
                
                



student_information = Student()  
          

while  True:
    print("======School Management System======")
    print("Enter 1 to Add students information")
    print("Enter 2 to View students information")
    print("Enter 3 to Add students grade")
    print("Enter 4 to Search students information")
    print("Enter 5 to Update students information")
    
    
    try: 
        choice = int(input("Enter number, what you want to make: ").strip())
    except ValueError:
        print("Error! Please enter valid number.")
        continue
        
    
    if choice == 1:
        student_information.register()
           
    elif choice == 2:
        student_information.show_details()
     
    elif choice == 3:
        student_information.add_grades()
        
    
    elif choice == 4:
        student_information.update_student()
        
    elif choice == 5:
        student_information.delete_student()
    
    
    
