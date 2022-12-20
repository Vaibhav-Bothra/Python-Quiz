#                                          *****ST.COLUMBO PUBLIC SCHOOL*****
#                                        *****PITAMPURA, NEW DELHI-110034*****
#                                           STUDENT MANAGEMENT SYSTEM....
#                                           ****Designed and Maintained By:****
#                                      VAIBHAVI SHARMA , CLASS-XII A, ROLL NO.
#=======================================================================#

import mysql.connector
# Global variable declaration
mydb=" "
cursor=" "
userName=" "
password=" "
# MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck():
    global mydb
    global userName
    global password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME :")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD :")
    mydb=mysql.connector.connect(host='localhost',user='root',password='17June2004')
    if mydb:
        print('\n You have successfully established a connection in MySQL !')
        cursor=mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS std_dms")
        cursor.execute("COMMIT")
        cursor.close()
        return mydb
    else:
        print('\n SORRY THERE IS AN ERROR IN ESTABLISHING A CONNECTION IN MYSQL !')
#******************************************************************************************************************************#
#MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection():
    global userName
    global password
    global mydb
    mydb=mysql.connector.connect(host="localhost",user="root",password="17June2004",database="std_dms")
    if mydb:
        return mydb
    else:
        print("\n SORRY THERE IS AN ERROR IN ESTABLISHING A CONNECTION IN MYSQL !")
    mydb.close()
#*****************************************************************************************************************************#
#MODULE FOR NEW ADMISSION
def newstudent():
    if mydb:
        cursor=mydb.cursor()
        createtable="""CREATE TABLE IF NOT EXISTS STUDENT_DATA(ADMISSION_NO INT NOT NULL PRIMARY KEY,ROLL_NO VARCHAR(3),
                                    STD_NAME CHAR(15),FATHER_NAME CHAR(15),MOTHER_NAME CHAR(15),PHONE_NO INT,
                                    STD_ADDRESS VARCHAR(12),STD_CLASS VARCHAR(3),STD_SECTION VARCHAR(2))"""
        cursor.execute(createtable)
        admission_no=int(input("ENTER ADMISSION_NO OF THE STUDENT:"))
        roll_no=input("ENTER ROLL_NO OF THE STUDENT:")
        name=input("\n ENTER STUDENT'S NAME:")
        father_name=input("enter student's father's name:")
        mother_name=input("enter student's mother's name:")
        phone_no=int(input ("enter student's phone no.:"))
        std_address=input("enter address of the student:")
        std_class=input("enter class in which the student is in-in batch 2021-2022:")
        std_section=input("enter section:")
        cursor.execute("INSERT INTO STUDENT_DATA VALUES('"+str(admission_no)+"','"+roll_no+"','"+name+"','"+father_name+"','"+mother_name+"','"+str(phone_no)+"','"+std_address+"','"+std_class+"','"+std_section+"')")
        cursor.execute("COMMIT")
        cursor.close()
        print('\nCONGRATULATION YOU ARE SUCCESSFUL IN ENROLLING A NEW STUDENT!')
    else:
            print("\nsorry there is an error in establishing connection in mysql !")
            print('\nplease try again')
#****************************************************************************************************************************************************#
#MODULE TO DISPLAY STUDENT'S DATA
def displaystudent():
    cursor=mydb.cursor()
    if mydb:
        cursor.execute("SELECT*FROM STUDENT_DATA")
        data=cursor.fetchall()

        for x in data:
            print(x)

        cursor.close()
    else:
        print("\n something went wrong !")
#***************************************************************************************************************************************
def updatestudent():
    cursor=mydb.cursor()
    if mydb:
        admission_num=input("enter admission no.:")
        sql=("SELECT *FROM STUDENT_DATA WHERE ADMISSION_NO=%S")
        cursor.execute(sql,(admission_num,))
        data=cursor.fetchall()
        if data:
            print("press 1 for name")
            print("press 2 for class")
            print("press 3 for roll no")
            choice =int(input("enter your choice:"))
            if choice==1:
                sname=("ENTER NAME OF THE STUDENT:")
                sql="UPDATE STUDENT_DATA SET NAME=%S WHERE ADMISSION_NO = %S"
                cursor.execute(sql,(sname,admission_num))
                cursor.execute("COMMIT")
                print("NAME UPDATED SUCCESSFULLY")
            elif choice==2:
                std=input("ENTER CLASS OF THE STUDENT:")
                sql="UPDATE STUDENT_DATA SET CLASS=%S WHERE ADMISSION_NO=%S"
                cursor.execute("COMMIT")
                print("class updated successfully")
            elif choice==3:
                roll_num=int(input("enter roll no of the student:"))
                sql="UPDATE STUDENT_DATA SET ROLL_NO=%S WHERE ADMISSION_NO=%S"
                cursor.execute(sql,(roll_num,admission_num))
                cursor.execute("COMMIT")
                print("ROLL NO UPDATED SUCCESSFULLY")
            else:
                print("record not found")
                cursor.close()
        else:
            print("something went wrong")
#**********************************************************************************************************************************
#MODULE TO ENTER MARKS OF THE STUDENT
def marksstudent():
    if mydb:
        cursor=mydb.cursor()
        createtable="""CREATE TABLE IF NOT EXISTS STD_MARKS(ADMISSION_NO INT NOT NULL PRIMARY KEY,PHYSICS INT,CHEMISTRY
                                   INT,MATHS INT,ENGLISH INT,COMP_SC INT,TOTAL_MARKS INT,AVERAGE INT)"""
        cursor.execute(createtable)
        admission_no=int(input("ENTER ADMISSION NO OF THE STUDENT:"))
        physics=int(input("enter marks of physics:"))
        chem=int(input("enter marks of chemistry:"))
        maths=int(input("enter marks of maths:"))
        eng=int(input("enter marks of english:"))
        comp=int(input("enter marks of computer:"))
        total=physics+chem+maths+eng+comp
        avrg=total/5
        sql='''INSERT INTO MARKS (ADMISSION_NO,PHYSICS,CHEMISTRY,MATHS,ENGLISH,COMP_SC,TOTAL_MARKS,AVERAGE)
                   VALUES(%S,%S,%S,%S,%S,%S,%S,%S)'''
        values=(admission_no,physics,chem,maths,eng,comp,total,avrg)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\n MARKS OF THE STUDENT ENTERED SUCCESSFULLY !")
    else:
        print("sorry something went wrong")
#*********************************************************************************************************************************
#MODULE TO GENERATE REPORT CARD OF ALL STUDENTS
def reportcardallstudent():
    cursor=mydb.cursor()
    if mydb:
        cursor.execute("SELECT*FROM STD_MARKS")
        data=cursor.fetchall()
        for i in data:
            print(i)
        cursor.close()
    else:
        print("something went wrong")
#************************************************************************************************************
#MODULE TO ENTER FEES OF THE STUDENTS
def feestudent():
    if mydb:
        cursor=mydb.cursor()
        createtable='''CREATE TABLE IF NOT EXISTS STD_FEES(ADMISSION _NO INT NOT NULL PRIMARY KEY,
                                MONTH INT,TUTION_FEES INT,COMPUTER_FEES,TOTAL INT)'''
        cursor.execute(createtable)
        adimission_no=int(input("ENTER ADMISSION NO OF THE STUDENT:"))
        month=int(input("/n ENTER MOTH IN NUMERIC FORM:"))
        tution_fees=int(input("ENTER TUTION FEES:"))
        computer_fees=int(input("ENTER COMPUTER FEES:"))
        total=tution_fees + computer_fees
        sql='''INSERT INTO STD_FEES(ADMISSION_NO,MONTH,TUTION_FEES,COMPUTER_FEES,TOTAL)
                    VALUES(%S,%S,%S,%S,%S)'''
        values=(adimission_no,month,tution_fees,computer_fees,total)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("/n Fees of student accepted successfully !")
    else:
        print(" something went wrong")
#***************************************************************************************************************
#MODULE TO GENERATE FEES RECEIPT OF ALL STUDENTS
def feereceiptallstudent():
    cursor=mydb.cursor()
    if mydb:
        cursor.execute("SELECT*FROM STD_FEES")
        data=cursor.fetchall()
        for a in data:
            print(a)
        cursor.close()
    else:
        print(" something went wrong please try again !")
#****************************************************************************************************************
#MODULE TO ISSUE TRANSFER CERTIFICATE
def transferstudent():
    cursor=mydb.cursor()
    if mydb:
        admission_num=int(input("ENTER ADMISSION NO OF STUDENT:"))
        cursor=mydb.cursor()
        sql="SELECT*FROM STUDENT_DATA WHERE ADMISSION_NO=%S"
        cursor.execute(sql,(admission_num))
        data=cursor.fetchall()
        if data:
            sql=("DELETE FROM STUDENT_DATA WHERE ADMISSION_NO=%S")
            cursor.execute(sql,(admission_num,))
            cursor.execute("COMMIT")
            print("student's transfer certificate generated !")
        else:
            print("record not found , please try again!")
        cursor.close()
    else:
        print("/n something went wrong , please try again!")
#**********************************************************************************************************
#MAIN SCREEN OF THE SYSTEM
print("################################################################")
print("/n ------------------------------------------------------WELCOME--------------------------------------------------")
print("/n-----------------------------------------------ST.COLUMBO PUBLIC SCHOOL----------------------------------")
print("/n---------------------------------------------STUDENT MANAGEMENT SYSTEM--------------------------------")

#STARTING POINT OF THE SYSTEM
mydb=MYSQLconnectionCheck()
if mydb:
    MYSQLconnection()
    while(1):
        print(" enter 1- New Admission")
        print(" enter 2- Display student's data")
        print(" enter 3-Update student's data")
        print(" enter 4- issue transfer certificate")
        print(" enter 5- add student's maks detail")
        print(" enter 6- generate all student report card")
        print(" enter 7- pay student's fee")
        print(" enter 8- generate all student's fee receipt")
        print(" enter 9- exit!")
        print("********************************************************")
        choice=int(input("PLEASE ENTER YOUR CHOICE:"))
        if choice==1:
            newstudent()
            choice=int(input("do you want to continue or not? press'0' for 'no'"))
            if choice==0:
                break
        elif choice==2:
            displaystudent()
            choice=int(input("do you want to continue or not? press'0' for 'no'"))
            if choice==0:
                break
        elif choice==3:
            updatestudent()
            choice=int(input("do you want to continue or not? press '0' for 'no'"))
            if choice==0:
                break
        elif choice==4:
            transferstudent()
            choice=int(input("do you want to continue or not? press '0' for 'no'"))
            if choice==0:
                break
        elif choice==5:
            marksstudent()
            choice=int(input("do you want to continue or not? press '0' for 'no'"))
            if choice==0:
                break
        elif choice==6:
            reportcardallstudent()
            choice=int(input("do you want to continue or not? press '0' for 'no'"))
            if choice==0:
                break
        elif choice==7:
            feestudent()
            choice=int(input("do you want to continue or not? press '0' for 'no'"))
            if choice==0:
                break
        elif choice==8:
            feereceiptallstudent()
            choice=int(input("do you want to continue or not? press '0' for 'no'"))
            if choice==0:
                break
        elif choice==9:
            break
        else:
            print("sorry,may be you are giving me a wrong input")
    else:
        print("please check your mysql connection first !!!")

#END OF PROJECT
        
        
    
        
        

    
     
