import os
import csv

FILE_NAME = "marks.csv"
SUBJECTS = ["SE","OOS","CN","GTC","GGM","MATH"]

def initialize():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["roll","name"]+SUBJECTS+["total"])

def add_student():
    roll=input("Enter roll no: ")
    name=input("Enter name: ")
    marks=[]
    total=0
    for subject in SUBJECTS:
        while True:
            try:
                m=int(input(f"Enter marks for {subject}: "))
                if 0<=m<=100:
                    break
                else:
                    print("Marks must be between 0 and 100")
            except:
                print("Enter valid number")
        marks.append(m)
        total+=m
    with open(FILE_NAME,"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([roll,name]+marks+[total])
    print("Student added successfully")

def display_students():
    with open(FILE_NAME,"r",newline="") as f:
        reader=csv.reader(f)
        next(reader)
        print("Roll\tName")
        for row in reader:
            print(f"{row[0]}\t{row[1]}")

def update_student_marks(subject_index):
    roll=input("Enter roll no: ")
    with open(FILE_NAME,"r",newline="") as f:
        rows=list(csv.reader(f))
    header=rows[0]
    data=rows[1:]
    for row in data:
        if row[0]==roll:
            while True:
                try:
                    new_mark=int(input("Enter new marks: "))
                    if 0<=new_mark<=100:
                        break
                    else:
                        print("Marks must be between 0 and 100")
                except:
                    print("Enter valid number")
            row[2+subject_index]=str(new_mark)
            marks=list(map(int,row[2:2+len(SUBJECTS)]))
            row[2+len(SUBJECTS)]=str(sum(marks))
            with open(FILE_NAME,"w",newline="") as f:
                writer=csv.writer(f)
                writer.writerow(header)
                writer.writerows(data)
            print("Marks updated")
            return
    print("Student not found")

def sort_database():
    with open(FILE_NAME,"r",newline="") as f:
        reader=csv.DictReader(f)
        rows=list(reader)
    rows=sorted(rows,key=lambda x:int(x["total"]),reverse=True)
    with open(FILE_NAME,"w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def show_results():
    with open(FILE_NAME,"r",newline="") as f:
        reader=csv.reader(f)
        for row in reader:
            print("\t".join(row))

def teacher_menu():
    print("1.SE")
    print("2.OOS")
    print("3.CN")
    print("4.GTC")
    print("5.GGM")
    print("6.MATH")
    try:
        ch=int(input("Enter subject choice: "))
        if 1<=ch<=6:
            display_students()
            update_student_marks(ch-1)
        else:
            print("Invalid subject choice")
    except:
        print("Enter valid number")

def main():
    initialize()
    while True:
        print("\nStudent Marks Management System")
        print("1.Add Student")
        print("2.Teacher Login")
        print("3.Finalize and Sort Result")
        print("4.View Results")
        print("5.Exit")
        try:
            choice=int(input("Enter choice: "))
        except:
            print("Enter valid number")
            continue
        if choice==1:
            add_student()
        elif choice==2:
            teacher_menu()
        elif choice==3:
            sort_database()
            print("Database sorted by total marks")
        elif choice==4:
            show_results()
        elif choice==5:
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
