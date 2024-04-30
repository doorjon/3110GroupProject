# importing Faker
from faker import Faker
fake = Faker()

# importing time record settings
import time
import sys
sys.setrecursionlimit(200000)

# class to contain all student record information
class Student:
    def __init__(self, id, name, dob, address):
        self.id = id
        self.name = name
        self.dob = dob
        self.address = address
        self.left = None  # For BST
        self.right = None  # For BST

# BST class, facilitates parent and children nodes structure
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, student):
        if not self.root:
            self.root = student
        else:
            self._insert_recursive(self.root, student)
    
    def _insert_recursive(self, current, student):
        if student.id < current.id:
            if current.left is None:
                current.left = student
            else:
                self._insert_recursive(current.left, student)
        else:
            if current.right is None:
                current.right = student
            else:
                self._insert_recursive(current.right, student)

# bst is what contains and represents the student recordes organized as a BST structure
bst = BST()

# Insert 100,000 students using the faker integration
for _ in range(100000):
    id = fake.unique.random_int(min=1, max=999999)
    name = fake.first_name()
    dob = fake.date_of_birth()
    address = {
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zip": fake.zipcode()
    }
    student = Student(id, name, dob, address)
    bst.insert(student)

# Function to delete student by id, takes a string variable as parameter, represents the id of the student they would like to delete 
def delete_student_by_id(student_id):
    bst.root = delete_from_bst(bst.root, student_id)

# Helper function for the delete_student_by_id functions, uses if statements to check on node 1)existence
# 2) its value compared to its right child, 3) value compared to left child 4) find the node that perfectly fits its value then removed,
# if none found, error message returned
def delete_from_bst(node, student_id):
    if node is None:
        return None
    if student_id < node.id:
        node.left = delete_from_bst(node.left, student_id)
    elif student_id > node.id:
        node.right = delete_from_bst(node.right, student_id)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp_val = find_min_value(node.right)
        node.id = temp_val.id
        node.right = delete_from_bst(node.right, temp_val.id)
    return node


# Search for a student by ID
def search_student_by_id(student_id):
    # Search in BST
    result = search_in_bst(bst.root, student_id)
    if result:
        print(f"Found student by ID: ID: {result.id}, Name: {result.name}, DOB: {result.dob}, Address: {result.address}")
    else:
        print("Student not found.")

# Function to search for node using student node id information
def search_in_bst(node, student_id):
    if node is None or node.id == student_id:
        return node
    if student_id < node.id:
        return search_in_bst(node.left, student_id)
    return search_in_bst(node.right, student_id)

# Function to search BST bst using student node name information
def search_student_by_name(name):
    result = _search_by_name(bst.root, name)
    if result:
        print(f"Found student by Name: ID: {result.id}, Name: {result.name}, DOB: {result.dob}, Address: {result.address}")
    else:
        print("Student not found.")


def _search_by_name(node, name):
    if node is None:
        return node
    if node.name == name:
        return node
    left_result = _search_by_name(node.left, name)
    right_result = _search_by_name(node.right, name)
    return left_result if left_result else right_result


def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Update student records
def update_student(student_id):
    # Find the student in the BST
    start_time = time.perf_counter()
    student = search_in_bst(bst.root, student_id)
    print("--- %s nanoseconds ---" % ((time.perf_counter() - start_time) * 1000000000))
    if student:
        print(f"Current information: ID: {student.id}, Name: {student.name}, DOB: {student.dob}, Address: {student.address}")
        # Update the student's information (except ID)
        student.name = input("Enter new name: ")
        student.dob = input("Enter new DOB: ")
        student.address = {
            "street": input("Enter new street address: "),
            "city": input("Enter new city: "),
            "state": input("Enter new state: "),
            "zip": input("Enter new zip code: ")
        }
        print("Student record updated.")
    else:
        print("Student not found.")

# Printing Out Student Records
def printBST(student):
    if student is None:
        print("NO STUDENTS IN THE BST DATA STRUCTURE")
    else:
        if student.left:
            printBST(student.left)
        print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}, Address: {student.address}")
        if student.right:
            printBST(student.right)


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add a student")
        print("2. Delete a student")
        print("3. Search for a student")
        print("4. Update a student record")
        print("5. Print BST of students")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Add a student
            id = fake.unique.random_int(min=1, max=999999)
            name = input("Enter student's name: ")
            dob = input("Enter student's DOB (YYYY-MM-DD): ")
            address = {
                "street": input("Enter student's street address: "),
                "city": input("Enter student's city: "),
                "state": input("Enter student's state: "),
                "zip": input("Enter student's zip code: ")
            }
            student = Student(id, name, dob, address)
            start_time = time.perf_counter()
            bst.insert(student)
            print("Student added successfully.")
            print("--- %s nanoseconds ---" % ((time.perf_counter() - start_time) * 1000000000))
        elif choice == "2":
            # Delete a student
            student_id = int(input("Enter the student ID to delete: "))
            start_time = time.perf_counter()
            delete_student_by_id(student_id)
            print("Student deleted successfully.")
            print("--- %s nanoseconds ---" % ((time.perf_counter() - start_time) * 1000000000))
        elif choice == "3":
            # Search for a student
            search_option = input("Do you know the student ID? (yes/no): ")
            if search_option.lower() == "yes":
                student_id = int(input("Enter the student ID: "))
                start_time = time.perf_counter()
                search_student_by_id(student_id)
            elif search_option.lower() == "no":
                name = input("Enter the student's name: ")
                start_time = time.perf_counter()
                search_student_by_name(name)
            else:
                print("Incorrect Input")
                continue
            print("--- %s nanoseconds ---" % ((time.perf_counter() - start_time) * 1000000000))
        elif choice == "4":
            # Update a student record
            student_id = int(input("Enter the student ID to update: "))
            update_student(student_id)
        elif choice == "5":
            # Printing the BST of student records
            print("Printing The BST of Student Recoreds:")
            printBST(bst.root)
        elif choice == "6":
            # Exit the program
            print("Exiting the BST Student Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
