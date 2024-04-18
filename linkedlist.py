# Create a Node class to create a node
class Student:
    def __init__(self, id, name, dob, address):
        self.id = id
        self.name = name
        self.dob = dob
        self.address = address
        self.next = None  # For linked list

class LinkedList:
    def __init__(self):
        self.head = None
    
    # add node at end of list
    def insert(self, student):
        if not self.head:
            self.head = student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = student
    
    # find node using identifier
    def search(self, node, identifier):
        if node is None or (node.id == identifier or node.name == identifier):
            return node
        else:
            return self.search(node.next, identifier)
    
    # find node using id
    def search_student_by_id(self, student_id):
        result = self.search(self.head, student_id)
        if result:
            print(f"Found student: ID: {result.id}, Name: {result.name}, DOB: {result.dob}, Address: {result.address}")
        else:
            print("Student not found.")
    
    # find node using name
    def search_student_by_name(self, name):
        result = self.search(self.head, name)
        if result:
            print(f"Found student: ID: {result.id}, Name: {result.name}, DOB: {result.dob}, Address: {result.address}")
        else:
            print("Student not found.")
    
    # find delete node using id
    def delete_student(self, node, student_id):
        current_student = node
        if (current_student.id == student_id and current_student == self.head): # if target node is head
            self.head = self.head.next
            print("Student removed.")
            return
        if (current_student.next != None):
            if (current_student.next.next == None and current_student.next.id != student_id): # if last node is not target
                print("Student not found.")
            elif(current_student != None and current_student.next.id != data): # if the next node is not the target
                self.search(current_student.next, student_id)
            else:                                           # if the next node is the target
                current_student.next = current_student.next.next
                print("Student removed.")
        else:
            print("Student not found.")
    
    # Update student records
    def update_student(self, student_id):
        student = self.search(self.head, student_id)
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
            print(f"Updated information: ID: {student.id}, Name: {student.name}, DOB: {student.dob}, Address: {student.address}")
        else:
            print("Student not found.")
    
    # print method for the linked list
    def printList(self):
        current_student = self.head
        while(current_student):
            print(f"{current_student.id}, Name: {current_student.name}, DOB: {current_student.dob}, Address: {current_student.address}")
            current_student = current_student.next



def main():
    # initialize list
    linked_list = LinkedList()
    
    student = Student(1, "john doe", "9/11/2001", "address1")
    linked_list.insert(student)
    student = Student(2, "jane doe", "9/12/2002", "address2")
    linked_list.insert(student)
    student = Student(3, "jeff doe", "9/13/2003", "address3")
    linked_list.insert(student)
    
    while True:
        print("\nStudent Management System")
        print("1. Add a student")
        print("2. Delete a student")
        print("3. Search for a student")
        print("4. Update a student record")
        print("5. Print list of students")
        print("6. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Add a student
            id = input("Enter student's id: ") # remove once faker implemented
            name = input("Enter student's name: ")
            dob = input("Enter student's DOB (YYYY-MM-DD): ")
            address = {
                "street": input("Enter student's street address: "),
                "city": input("Enter student's city: "),
                "state": input("Enter student's state: "),
                "zip": input("Enter student's zip code: ")
            }
            student = Student(id, name, dob, address)
            linked_list.insert(student)
            print("Student added successfully.")
        elif choice == "2":
            # Delete a student
            student_id = int(input("Enter the student ID to delete: "))
            linked_list.delete_student(linked_list.head, student_id)
        elif choice == "3":
            # Search for a student
            search_option = input("Do you know the student ID? (yes/no): ")
            if search_option.lower() == "yes":
                student_id = int(input("Enter the student ID: "))
                linked_list.search_student_by_id(student_id)
            else:
                name = input("Enter the student's name: ")
                linked_list.search_student_by_name(name)
        elif choice == "4":
            # Update a student record
            student_id = int(input("Enter the student ID to update: "))
            linked_list.update_student(student_id)
        elif choice == "5":
            linked_list.printList()
        elif choice == "6":
            # Exit the program
            print("Exiting the Student Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
