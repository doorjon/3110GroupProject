from faker import Faker

fake = Faker()

class Student:
    def __init__(self, id, name, dob, address):
        self.id = id
        self.name = name
        self.dob = dob
        self.address = address
        self.left = None  # For BST
        self.right = None  # For BST


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

bst = BST()

# Insert 100,000 students
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



def delete_student_by_id(self, student_id):
    self.root = self._delet_from_bst(self.root, student_id)


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
        print(f"Found student: ID: {result.id}, Name: {result.name}, DOB: {result.dob}, Address: {result.address}")
    else:
        print("Student not found.")


def search_in_bst(node, student_id):
    if node is None or node.id == student_id:
        return node
    if student_id < node.id:
        return search_in_bst(node.left, student_id)
    return search_in_bst(node.right, student_id)


def search_student_by_name(self, name):
    return self._serach_by_name(self.root, name)


def _search_by_name(self, node, name):
    if node is None:
        return node
    if node.name == name:
        return node
    left_result = self._search_by_name(node.left, name)
    right_result = self._search_by_name(node.right, name)
    return left_result if left_result else right_result


def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# Update student records
def update_student(student_id):
    # Find the student in the BST
    student = search_in_bst(bst.root, student_id)
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


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add a student")
        print("2. Delete a student")
        print("3. Search for a student")
        print("4. Update a student record")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

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
            bst.insert(student)
            print("Student added successfully.")
        elif choice == "2":
            # Delete a student
            student_id = int(input("Enter the student ID to delete: "))
            delete_student_by_id(student_id)
            print("Student deleted successfully.")
        elif choice == "3":
            # Search for a student
            search_option = input("Do you know the student ID? (yes/no): ")
            if search_option.lower() == "yes":
                student_id = int(input("Enter the student ID: "))
                search_student_by_id(student_id)
            else:
                name = input("Enter the student's name: ")
                search_student_by_name(name)
        elif choice == "4":
            # Update a student record
            student_id = int(input("Enter the student ID to update: "))
            update_student(student_id)
        elif choice == "5":
            # Exit the program
            print("Exiting the Student Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
