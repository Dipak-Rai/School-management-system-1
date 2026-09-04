from pathlib import Path

def create_student_file():
    try: 
        student_file_name = input("Enter student file name: ").strip()
        if not student_file_name:
            print("Sorry! student file name should not be empty.")
            return
        
        student_file_path = Path(student_file_name)
        
        if student_file_path.suffix=="":
            student_file_path = student_file_path.with_suffix(".txt")
            
        if student_file_path.exists():
            print(f"Sorry! {student_file_path} file name already exist.")
            return
        
        with open(student_file_path, 'w') as file:
            pass
        print("Student file created successfully.")
        
    except PermissionError:
        print("Error! You have no permission to create student file.")
    except OSError as err:
        print(f"Error! File system error: {err}")



def add_student_information():
    file_name = input("Enter file name to add student: ").strip()
    
    #check file name is empty or not
    if not file_name:
        print("Sorry! File name should not be empty: ")
        return
    
    #Create path 
    student_path = Path(file_name)
    
    #Add extension .txt autometically
    if student_path.suffix == "":
        student_path = student_path.with_suffix(".txt")
    
    #check if file not exist:
    if not student_path.exists():
        print(f"Sorry! {student_path} file does not exist")
        return
    
    if not student_path.is_file():
        print(f"Sorry! {student_path} file is not a file.")
        return
    
    try: 
        student_id_found = False
        student_id = input("Enter student id: ").strip()
        if not student_id:
            print("Sorry! student id should not be empty.")
            return
        
        with open(student_path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                info = line.strip().split(",")
                
                if info[0].strip()==student_id:
                    student_id_found = True
        if student_id_found:
            print(f"Sorry! {student_id} student id already exist")
            return
        else:
            pass
        
        student_name = input("Enter student name: ").strip()
        if not student_name:
            print("Sorry! student name should not be empty.")
            return
        
        try:
            student_age = int(input("Enter student age: ").strip())
            if student_age<=0 and student_age>=120:
                print("Sorry! Enter valid age number which is not less or equal to 0 and grater or equal to 120 years old.")
                return
        except ValueError:
            print("Sorry! enter valid age number")
            return
        
        student_gender = input("Enter student gender: ").strip()
        if not student_gender:
            print("Sorry! student gender should not be empty.")
            return
        
        student_class = input("Enter student class: ").strip()
        if not student_class:
            print("Sorry! student class should not be empty.")
            return
        
        student_address = input("Enter student address: ").strip()
        if not student_address:
            print("Sorry! student address should not be empty.")
            return
        
        student_info = (
            f"{student_id}, {student_name}, {student_age}, {student_gender}, {student_class}, {student_address}\n"
        )
        
        with open(student_path, 'a') as file:
            file.write(student_info)
        
        print("\nStudent information added successfully.")
    except PermissionError:
        print("Error! You have no permission to add student.")
    except OSError as err:
        print(f"File system error! {err}")
    
                
            
     
     
        
    
    






while  True:
    print("======School Management System======")
    print("\nEnter 1 to Create student file")
    print("Enter 2 to Add student information")
    print("Enter 3 to View student information")
    print("Enter 4 to Search student information")
    print("Enter 5 to Update student information")
    print("Enter 6 to Delete student information")
    
    
    try: 
        choice = int(input("Enter number, what you want to make: ").strip())
    except ValueError:
        print("Error! Please enter valid number.")
        
    
    if choice == 1:
        create_student_file()
           
    elif choice == 2:
        add_student_information()
     
    elif choice == 3:
        view_student_information()
        
    elif choice == 4:
        search_student_information()
    
    elif choice == 5:
        update_student_information()
    
    elif choice == 6:
        delete_student_information()