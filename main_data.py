import random
import datetime

list_names = []

#Question 3

def Q3_AboutDaiict():
	pos = [0,0,0,0]
	f = open("About-DAIICT.txt",'r')
	read_line = f.readlines()

	for i in read_line:
		if i == "History\n":
			pos[0] = read_line.index(i)
		if i == "Environment\n":
			pos[1] = read_line.index(i)
		if i == "Recognition\n":
			pos[2] = read_line.index(i)
		if i == "Accreditation\n":
			pos[3] = read_line.index(i)
	f.close()


	f = open("History.txt",'w')
	f.writelines(read_line[pos[0]:pos[1]])
	f.close()

	f = open("Environment.txt",'w')
	f.writelines(read_line[pos[1]:pos[2]])
	f.close()

	f = open("Recognition.txt",'w')
	f.writelines(read_line[pos[2]:pos[3]])
	f.close()

	f = open("Accreditation.txt",'w')
	f.writelines(read_line[pos[3]:])
	f.close()



# Question 4

def Q4_Student_name_list():
	f = open("student_name_list.txt","r")
	global list_names 
	list_names = f.readlines()
	for i in range(0,len(list_names)):
		list_names[i] = list_names[i].strip('\n')
	print(list_names)


Q4_Student_name_list()

# Question 5

list_emails = list(range(1,21))
for y in range(1,16) : 
	a = random.choice(list_emails)
	f = open("email-" + str(a) + ".txt", "w")
	list_emails.remove(a)
	x = datetime.datetime.now()
	b = "Received at " + str(x.strftime("%X")) + " hrs " + str(x.strftime("%B")) + " " + str(x.strftime("%d")) + ", " + str(x.strftime("%Y")) + " from " + (random.choice(list_names)).lower().replace(" ","_") + "@daiict.ac.in"
	list_files = {"History.txt", "Environment.txt", "Recognition.txt", "Accreditation.txt"}
	list_lines = [b +"\n", "\n"]
	
	for z in list_files :
		f1 = open(z,"r")
		list_lines.append(random.choice(f1.readlines()))
		f1.close()
	f.writelines(list_lines)
	f.close()

	
	
	
	
	
	
	
	
	
	
	
	
