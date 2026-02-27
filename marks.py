import os

import csv


FILE_NAME = "marks.csv"
SUBJECTS = ["SE","OOS","CN","GTC","GGM","MATH"]


def initialize():
	if os.path.exists(FILE_NAME):
		with open(FILE_NAME,"w",newline="") as f:
			writer = csv.writer(f)
			writer.writerow(["roll","name"]+SUBJECTS+["total"])


def add_student():
	roll = input("Enter roll no:")
	name = str(input("Enter name:"))
	total=0
	marks = []
	for subject in SUBJECTS:
		mark = int(input(f"{subject} mark:"))
		total += mark
		marks.append(mark)
	with open(FILE_NAME,"a",newline="") as f:
		writer = csv.writer(f)
		writer.writerow([roll,name]+marks+[str(total)])
	print("Student data inserted successfully")

def update_student_marks(index):
	roll = input("Enter roll no:")
	data = []
	header = []
	with open(FILE_NAME,"r",newline="") as f:
		rows = list(csv.reader(f))
		header = rows[0]	
	
	with open(FILE_NAME,"r",newline="") as f:
		reader = csv.reader(f)
		for row in reader:
			data.append(row)
	for row in range(1,len(data)):
		if roll==data[row][0]:
			new_marks = int(input("Enter marks:"))
			total = int(data[row][8])
			old_marks = int(data[row][index])
			new_total = total-old_marks+new_marks
			data[row][index]=str(new_marks)
			data[row]["total"] = new_total
			with open(FILE_NAME,"w",newline="") as f:
				writer = csv.write(f)
				writer.writerow(header)
				writer.writerows(data)
			print("Marks Updated successfully!!!!!")
			return
		else:
			print("No student exists!!!")
			return	
def show_result():
    roll = input("Enter roll no: ")
    
   
    with open(FILE_NAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
  
    sorted_rows = sorted(rows, key=lambda x: int(x["Total Marks"]), reverse=True)
    
   
    found = False
    for row in sorted_rows:
        if row["Roll No"] == roll:   
            found = True
            print("Student Result (Sorted by Total Marks):")
            for key, value in row.items():
                print(f"{key}: {value}")
            break
    
    if not found:
        print(f"No record found for roll number {roll}")



def sort_csv_by_total():
    with open(FILE_NAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    
    sorted_rows = sorted(rows, key=lambda x: int(x["Total Marks"]), reverse=True)

   
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)

    with open(FILE_NAME, "r", newline="") as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
def sort_csv_by_total():
    # Read CSV
    with open(FILE_NAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Sort rows by 'total' column descending
    sorted_rows = sorted(rows, key=lambda x: int(x["total"]), reverse=True)

    # Write sorted CSV back to the same file
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)

    # Display the sorted CSV
    with open(FILE_NAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row) 

def main():
	print("----------------Welcome Marks Management System----------")
	initialize()
	while True:
		print("1. Add student data\n")
		print("2. Teacher login\n")
		print("3. Show result\n")
		choice = int(input("Enter choice:"))
		
		if choice==1 :
			add_student()
		elif choice==2 :
			print("1. SE\n")
			print("2. OOS\n")
			print("3. CN\n")
			print("4. GTC\n")
			print("5. GGM\n")
			print("6. MATH\n")
			ch = int(input("Enter choice:"))
			update_student_marks(ch)
		elif choice==3:
			sort_csv_by_total()
		else:
			print("Invalid choice!!!!!!")
			break


if __name__ == "__main__":
	main()
