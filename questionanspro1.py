import random as rd
#Database connection details
import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Probal@555",
    database="exam_qans1")
cur_obj=conn_obj.cursor()

#Define function data_entry_sql


#Define function data_retrieve
def data_retrieve(question_id):
    # Build the query with user-provided name using LIKE operator
    #select * from students_details WHERE Roll_no=1;
    query = f"select * from  exam_questions WHERE question_id={question_id}"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Print or process the retrieved data using list unpacking
    if result:
        question_id, multiple_questions, answers  = result  # Unpacking the row into variables
        # Print data in proper sequence using f-strings
        print(result[1])
        return result[-1]
    else:
        print("No question found with the provided id.")
x=int(input("choose less than 100 questions you want to give exam......."))
score=0
i=1
while i<=x:
    y=rd.randint(1,100)
    p=data_retrieve(y)
    z=input("enter your choice").upper()
    if z==p:
        score+=1
    print(f"correct answer is ->{p}")


    i=i+1
print(f"your total score is{score}/{x}")



conn_obj.close()