import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
import pyttsx3
from datetime import date


# Setting up the sound
engine = pyttsx3.init()
sound = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Connection with database
db = mysql.connector.connect(
    host="localhost", user="root", password="********")
if db.is_connected() == False:
    print('error connecting to MYSQL database')
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS project")
cursor.execute("USE project")


# Setting up root
root = Tk()
root.title("Achiever's Club")
root.iconbitmap(r"#Location of theimage of icon")
root.geometry("400x500")


# Creating Tables
cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENT_PROFILE(
    reg_no BIGINT NOT NULL AUTO_INCREMENT,
    stu_name VARCHAR(100) NOT NULL,
    stu_class BIGINT NOT NULL,
    stu_stream VARCHAR(15),
    stu_father VARCHAR(100) NOT NULL,
    stu_mother VARCHAR(100) NOT NULL,
    d_o_b DATE NOT NULL,
    d_o_j DATE NOT NULL,
    phn_no BIGINT NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (reg_no, stu_name, stu_class, stu_stream)
    )
    ENGINE = INNODB
    AUTO_INCREMENT = 1""")

cursor.execute("""CREATE TABLE IF NOT EXISTS FEE_DETAILS(
    reg_no BIGINT NOT NULL,
    stu_name VARCHAR(100) NOT NULL, 
    stu_class BIGINT NOT NULL, 
    stu_stream VARCHAR(15), 
    total_fee BIGINT, 
    fee_due BIGINT, 
    fee_paid BIGINT, 
    FOREIGN KEY (reg_no, stu_name, stu_class, stu_stream) 
    REFERENCES STUDENT_PROFILE(reg_no, stu_name, stu_class, stu_stream) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
    )
    ENGINE = INNODB
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS ATTENDANCE_DETAILS(
    reg_no BIGINT NOT NULL, 
    stu_name VARCHAR(100) NOT NULL, 
    FOREIGN KEY (reg_no, stu_name) 
    REFERENCES STUDENT_PROFILE(reg_no, stu_name) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
    )
    ENGINE = INNODB
    """)


# Functions to Insert Record in Database
def add_in_database():
    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    stu_name = stu_name_entry.get()
    stu_class = int(stu_class_entry.get())
    stu_stream = stu_stream_entry.get()
    stu_father = stu_father_entry.get()
    stu_mother = stu_mother_entry.get()
    d_o_b = d_o_b_entry.get()
    phn_no = int(phn_no_entry.get())
    email = email_entry.get()
    d_o_j = date.today()

    cursor.execute("""INSERT INTO STUDENT_PROFILE (
        stu_name, 
        stu_class, 
        stu_stream, 
        stu_father, 
        stu_mother, 
        d_o_b, 
        d_o_j, 
        phn_no, 
        email) 
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
                   .format(
                       stu_name,
                       stu_class,
                       stu_stream,
                       stu_father,
                       stu_mother,
                       d_o_b,
                       d_o_j,
                       phn_no,
                       email
                   ))

    cursor.execute("SELECT reg_no, stu_name, stu_class, stu_stream FROM STUDENT_PROFILE WHERE stu_name = '%s' AND stu_class = %s AND phn_no = %s" % (
        stu_name, stu_class, phn_no))
    inserted_record = cursor.fetchall()
    inserted_reg_no = int(inserted_record[0][0])
    inserted_name = inserted_record[0][1]
    inserted_class = inserted_record[0][2]
    inserted_stream = inserted_record[0][3]

    speak(inserted_name + ", your registration number is, " +
          str(inserted_reg_no) + ", please remeber it for future refrences")

    # Inserting the Values in Fee Table Accordingly
    cursor.execute("""INSERT INTO FEE_DETAILS(reg_no, stu_name, stu_class, stu_stream, fee_paid)
    VALUES(
        %s, 
        '%s',
        %s, 
        '%s', 
        %s 
    )
    """
                   % (
                       inserted_reg_no,
                       inserted_name,
                       inserted_class,
                       inserted_stream,
                       0
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    reg_no = %s
    """
                   % (
                       10000, 10000, 6, inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    reg_no = %s
    """
                   % (
                       15000, 15000, 7, inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    reg_no = %s
    """
                   % (
                       20000, 20000, 8, inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    reg_no = %s
    """
                   % (
                       30000, 30000, 9, inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    reg_no = %s
    """
                   % (
                       35000, 35000, 10, inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    AND
    reg_no = %s
    """
                   % (
                       45000, 45000, 11, "science", inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    AND
    reg_no = %s
    """
                   % (
                       40000, 40000, 11, "Commerce", inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    (stu_stream = '%s' OR stu_stream = '%s')
    AND
    reg_no = %s
    """
                   % (
                       40000, 40000, 11, "Humanities", "Arts", inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    AND
    reg_no = %s
    """
                   % (
                       50000, 50000, 12, "Science", inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    AND
    reg_no = %s
    """
                   % (
                       45000, 45000, 12, "Commerce", inserted_reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    (stu_stream = '%s' OR stu_stream = '%s')
    AND
    reg_no = %s
    """
                   % (
                       40000, 40000, 12, "Humanities", "Arts", inserted_reg_no
                   ))

    cursor.execute("""INSERT INTO ATTENDANCE_DETAILS(reg_no, stu_name)
    VALUES(%s, '%s')
    """
                   % (inserted_reg_no, inserted_name))

    # Closing Connection
    db.commit()
    db.close()
    add_student_window.destroy()


# Function to Remove Record from Database
def remove_from_database():
    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    reg_no = int(reg_no_delete_entry.get())

    cursor.execute("""DELETE FROM STUDENT_PROFILE WHERE
    reg_no = %s""" % (reg_no))

    # Closing Connection
    db.commit()
    db.close()
    remove_student_window.destroy()


# Updating Fee_details Table
def updating_fee():
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    fee_got = int(fee_amount.get())

    cursor.execute("""SELECT fee_due, fee_paid
    FROM FEE_DETAILS
    WHERE reg_no = %s"""
                   % (pay_fee_reg_no.get()))

    pay_fee_list1 = cursor.fetchall()

    updated_fee_due = int(pay_fee_list1[0][0]) - fee_got
    updated_fee_paid = int(pay_fee_list1[0][1]) + fee_got

    cursor.execute("""UPDATE FEE_DETAILS
    SET 
    fee_due = %s,
    fee_paid = %s
    WHERE 
    reg_no = %s"""
                   % (updated_fee_due, updated_fee_paid, pay_fee_reg_no.get()))

    cursor.execute("""SELECT fee_due, fee_paid
    FROM FEE_DETAILS
    WHERE reg_no = %s"""
                   % (pay_fee_reg_no.get()))
    pay_fee_list2 = cursor.fetchall()

    fee_due.delete(0, END)
    fee_paid.delete(0, END)
    fee_due.insert(0, pay_fee_list2[0][0])
    fee_paid.insert(0, pay_fee_list2[0][1])
    fee_amount.delete(0, END)

    speak("You Paid a amount of " + str(fee_got))

    # Closing Connection
    db.commit()
    db.close()


# Showing Data Related To fee
def fee_data():
    global fee_due
    global fee_paid
    global fee_amount

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    cursor.execute("""SELECT stu_name, total_fee, fee_due, fee_paid
    FROM FEE_DETAILS
    WHERE reg_no = %s"""
                   % (pay_fee_reg_no.get()))

    pay_fee_list = cursor.fetchall()

    Label(pay_fee_window, text="Student's Name").grid(row=2, column=0)
    Label(pay_fee_window, text="Total Fee").grid(row=3, column=0)
    Label(pay_fee_window, text="Fee Due").grid(row=4, column=0)
    Label(pay_fee_window, text="Fee Paid").grid(row=5, column=0)
    Label(pay_fee_window, text="Enter Amount").grid(row=6, column=0)

    stu_name_fee = Entry(pay_fee_window)
    fee_total = Entry(pay_fee_window)
    fee_due = Entry(pay_fee_window)
    fee_paid = Entry(pay_fee_window)
    fee_amount = Entry(pay_fee_window)

    stu_name_fee.grid(row=2, column=1)
    fee_total.grid(row=3, column=1)
    fee_due.grid(row=4, column=1)
    fee_paid.grid(row=5, column=1)
    fee_amount.grid(row=6, column=1)

    stu_name_fee.insert(0, pay_fee_list[0][0])
    fee_total.insert(0, pay_fee_list[0][1])
    fee_due.insert(0, pay_fee_list[0][2])
    fee_paid.insert(0, pay_fee_list[0][3])

    pay_button = Button(pay_fee_window, text="Pay Fee", command=updating_fee)
    pay_button.grid(row=7, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Adding Attendance in Database
def attendance_1(reg_no):
    global attendance_variable
    date = mark_attendance_date.get()
    attendance = attendance_given.get()

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    cursor.execute("""UPDATE ATTENDANCE_DETAILS
    SET 
    %s = '%s'
    WHERE reg_no = %s"""
                   % (date, attendance, reg_no))

    attendance_variable += 1
    attendance_2(attendance_variable)

    # Closing Connection
    db.commit()
    db.close()


def attendance_2(reg_no_index):
    global student_attendance_window
    global attendance_given

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    cursor.execute("""SELECT stu_name, reg_no FROM ATTENDANCE_DETAILS""")
    mark_attendance_list = cursor.fetchall()

    if reg_no_index < len(mark_attendance_list):
        global attendance_given

        name = mark_attendance_list[reg_no_index][0]
        reg_no = mark_attendance_list[reg_no_index][1]
        student_attendance_window = Tk()
        student_attendance_window.title(name)
        student_attendance_window.geometry("225x225")
        attendance_given = Entry(student_attendance_window)
        attendance_given.grid(row=0)
        attendance_given.insert(0, "Present")
        Button(student_attendance_window, text="Next",
               command=lambda: attendance_1(reg_no)).grid(row=1)


# Getting Attendance from User
def adding_date_column():
    global attendance_variable
    global attendance_given
    global student_attendance_window

    date = mark_attendance_date.get()

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    cursor.execute("""ALTER TABLE ATTENDANCE_DETAILS
    ADD %s VARCHAR(10)"""
                   % (date))

    cursor.execute("""SELECT stu_name, reg_no FROM ATTENDANCE_DETAILS""")
    mark_attendance_list = cursor.fetchall()

    name = mark_attendance_list[0][0]
    reg_no = mark_attendance_list[0][1]
    student_attendance_window = Tk()
    student_attendance_window.title(name)
    student_attendance_window.geometry("225x225")
    attendance_given = Entry(student_attendance_window)
    attendance_given.grid(row=0)
    attendance_given.insert(0, "Present")
    Button(student_attendance_window, text="Next",
           command=lambda: attendance_1(reg_no)).grid(row=1)

    attendance_variable = 0

    # Closing Connection
    db.commit()
    db.close()


# Function to Check the Attendance from Database
def check_attendance_from_database():
    attendance_date = check_attendance_date.get()
    attendance_reg_no = int(check_attendance_reg_no.get())

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    cursor.execute("""SELECT stu_name, %s
    FROM ATTENDANCE_DETAILS
    WHERE reg_no = %s"""
                   % (attendance_date, attendance_reg_no))
    check_attendance_list = cursor.fetchall()

    Label(check_attendance_window, text=check_attendance_list[0][0] +
          " was " + check_attendance_list[0][1]).grid(row=3, column=0, columnspan=2)
    Label(check_attendance_window, text="on " +
          attendance_date).grid(row=4, column=0, columnspan=2)

    speak(check_attendance_list[0][0] + " was " +
          check_attendance_list[0][1] + "on that day")

    # Closing Connection
    db.commit()
    db.close()


# Function to Check Record from Database
def check_profile_from_database():

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    # Creating and Placing Entry Box Labels
    Label(check_student_window, text="Reg. Number").grid(row=3, column=0)
    Label(check_student_window, text="Name").grid(row=4, column=0)
    Label(check_student_window, text="Class").grid(row=5, column=0)
    Label(check_student_window, text="Stream").grid(row=6, column=0)
    Label(check_student_window, text="Father Name").grid(row=7, column=0)
    Label(check_student_window, text="Mother Name").grid(row=8, column=0)
    Label(check_student_window, text="Date of Birth").grid(row=9, column=0)
    Label(check_student_window, text="Date of Joining").grid(row=10, column=0)
    Label(check_student_window, text="Phone Number").grid(row=11, column=0)
    Label(check_student_window, text="Email").grid(row=12, column=0)

    check_reg_no = Entry(check_student_window)
    check_stu_name = Entry(check_student_window)
    check_stu_class = Entry(check_student_window)
    check_stu_stream = Entry(check_student_window)
    check_stu_father = Entry(check_student_window)
    check_stu_mother = Entry(check_student_window)
    check_d_o_b = Entry(check_student_window)
    check_d_o_j = Entry(check_student_window)
    check_phn_no = Entry(check_student_window)
    check_email = Entry(check_student_window)

    check_reg_no.grid(row=3, column=1)
    check_stu_name.grid(row=4, column=1)
    check_stu_class.grid(row=5, column=1)
    check_stu_stream.grid(row=6, column=1)
    check_stu_father.grid(row=7, column=1)
    check_stu_mother.grid(row=8, column=1)
    check_d_o_b.grid(row=9, column=1)
    check_d_o_j.grid(row=10, column=1)
    check_phn_no.grid(row=11, column=1)
    check_email.grid(row=12, column=1)

    reg_no = check_profile_reg_no.get()
    cursor.execute("""SELECT * FROM STUDENT_PROFILE WHERE
    reg_no = {}""".format(reg_no))
    check_profile_list = cursor.fetchall()

    check_reg_no.insert(0, check_profile_list[0][0])
    check_stu_name.insert(0, check_profile_list[0][1])
    check_stu_class.insert(0, check_profile_list[0][2])
    check_stu_stream.insert(0, check_profile_list[0][3])
    check_stu_father.insert(0, check_profile_list[0][4])
    check_stu_mother.insert(0, check_profile_list[0][5])
    check_d_o_b.insert(0, check_profile_list[0][6])
    check_d_o_j.insert(0, check_profile_list[0][7])
    check_phn_no.insert(0, check_profile_list[0][8])
    check_email.insert(0, check_profile_list[0][9])

    # Closing Connection
    db.commit()
    db.close()


# Function to Edit Record in Database
def edit_profile_in_database():
    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    edited_stu_name = edit_stu_name.get()
    edited_stu_class = int(edit_stu_class.get())
    edited_stu_stream = edit_stu_stream.get()
    edited_stu_father = edit_stu_father.get()
    edited_stu_mother = edit_stu_mother.get()
    edited_d_o_b = edit_d_o_b.get()
    edited_d_o_j = edit_d_o_j.get()
    edited_phn_no = int(edit_phn_no.get())
    edited_email = edit_email.get()

    reg_no = int(edit_profile_reg_no.get())

    cursor.execute("""UPDATE STUDENT_PROFILE
    SET 
    stu_name = '%s',
    stu_class = %s,
    stu_stream = '%s',
    stu_father = '%s',
    stu_mother = '%s',
    d_o_b = '%s',
    d_o_j = '%s',
    phn_no = %s,
    email = '%s'
    WHERE reg_no = %s"""
                   % (
                       edited_stu_name,
                       edited_stu_class,
                       edited_stu_stream,
                       edited_stu_father,
                       edited_stu_mother,
                       edited_d_o_b,
                       edited_d_o_j,
                       edited_phn_no,
                       edited_email,
                       reg_no
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    """
                   % (
                       10000, 10000, 6
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    """
                   % (
                       15000, 15000, 7
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    """
                   % (
                       20000, 20000, 8
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    """
                   % (
                       30000, 30000, 9
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    """
                   % (
                       35000, 35000, 10
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    """
                   % (
                       45000, 45000, 11, "science"
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    """
                   % (
                       40000, 40000, 11, "Commerce"
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    (stu_stream = '%s' OR stu_stream = '%s')
    """
                   % (
                       40000, 40000, 11, "Humanities", "Arts"
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    """
                   % (
                       50000, 50000, 12, "Science"
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    stu_stream = '%s'
    """
                   % (
                       45000, 45000, 12, "Commerce"
                   ))

    cursor.execute("""UPDATE FEE_DETAILS 
    SET
    total_fee = %s,
    fee_due = %s
    WHERE 
    stu_class = %s
    AND
    (stu_stream = '%s' OR stu_stream = '%s')
    """
                   % (
                       40000, 40000, 12, "Humanities", "Arts"
                   ))

    speak("Details Edited Successfully")

    # Closing Connection
    db.commit()
    db.close()

    edit_student_window.destroy()


# Function to Show the Record Which is to be Edited
def show_profile_from_database():

    global edit_stu_name
    global edit_stu_class
    global edit_stu_stream
    global edit_stu_father
    global edit_stu_mother
    global edit_d_o_b
    global edit_d_o_j
    global edit_phn_no
    global edit_email

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    # Creating and Placing Entry Box and Labels
    Label(edit_student_window, text="Name").grid(row=3, column=0)
    Label(edit_student_window, text="Class").grid(row=4, column=0)
    Label(edit_student_window, text="Stream").grid(row=5, column=0)
    Label(edit_student_window, text="Father Name").grid(row=6, column=0)
    Label(edit_student_window, text="Mother Name").grid(row=7, column=0)
    Label(edit_student_window, text="Date of Birth").grid(row=8, column=0)
    Label(edit_student_window, text="Date of Joining").grid(row=9, column=0)
    Label(edit_student_window, text="Phone Number").grid(row=10, column=0)
    Label(edit_student_window, text="Email").grid(row=11, column=0)

    edit_stu_name = Entry(edit_student_window)
    edit_stu_class = Entry(edit_student_window)
    edit_stu_stream = Entry(edit_student_window)
    edit_stu_father = Entry(edit_student_window)
    edit_stu_mother = Entry(edit_student_window)
    edit_d_o_b = Entry(edit_student_window)
    edit_d_o_j = Entry(edit_student_window)
    edit_phn_no = Entry(edit_student_window)
    edit_email = Entry(edit_student_window)

    edit_stu_name.grid(row=3, column=1)
    edit_stu_class.grid(row=4, column=1)
    edit_stu_stream.grid(row=5, column=1)
    edit_stu_father.grid(row=6, column=1)
    edit_stu_mother.grid(row=7, column=1)
    edit_d_o_b.grid(row=8, column=1)
    edit_d_o_j.grid(row=9, column=1)
    edit_phn_no.grid(row=10, column=1)
    edit_email.grid(row=11, column=1)

    reg_no = edit_profile_reg_no.get()
    cursor.execute("""SELECT * FROM STUDENT_PROFILE WHERE
    reg_no = {}""".format(reg_no))
    edit_profile_list = cursor.fetchall()

    edit_stu_name.insert(0, edit_profile_list[0][1])
    edit_stu_class.insert(0, edit_profile_list[0][2])
    edit_stu_stream.insert(0, edit_profile_list[0][3])
    edit_stu_father.insert(0, edit_profile_list[0][4])
    edit_stu_mother.insert(0, edit_profile_list[0][5])
    edit_d_o_b.insert(0, edit_profile_list[0][6])
    edit_d_o_j.insert(0, edit_profile_list[0][7])
    edit_phn_no.insert(0, edit_profile_list[0][8])
    edit_email.insert(0, edit_profile_list[0][9])

    Button(edit_student_window, text="Save Changes",
           command=edit_profile_in_database).grid(row=12, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Function to Add Student
def add_student():

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')

    # Making the Variables as Global Variable
    global stu_name_entry
    global stu_class_entry
    global stu_stream_entry
    global stu_father_entry
    global stu_mother_entry
    global d_o_b_entry
    global phn_no_entry
    global email_entry
    global add_student_window

    # Creating New Window
    add_student_window = Tk()
    add_student_window.title("Add Student")
    add_student_window.iconbitmap(r"#Location of theimage of icon")
    add_student_window.geometry("225x225")

    # Creating and Placing Entry Box Labels
    Label(add_student_window, text="Name").grid(row=0, column=0)
    Label(add_student_window, text="Class").grid(row=1, column=0)
    Label(add_student_window, text="Stream").grid(row=2, column=0)
    Label(add_student_window, text="Father Name").grid(row=3, column=0)
    Label(add_student_window, text="Mother Name").grid(row=4, column=0)
    Label(add_student_window, text="Date of Birth").grid(row=5, column=0)
    Label(add_student_window, text="Phone Number").grid(row=6, column=0)
    Label(add_student_window, text="Email").grid(row=7, column=0)

    # Creating and Placing Entry Boxes
    stu_name_entry = Entry(add_student_window)
    stu_name_entry.grid(row=0, column=1)
    stu_class_entry = Entry(add_student_window)
    stu_class_entry.grid(row=1, column=1)
    stu_class_entry.insert(0, 'Only Digits')
    stu_stream_entry = Entry(add_student_window)
    stu_stream_entry.grid(row=2, column=1)
    stu_stream_entry.insert(0, "NONE")
    stu_father_entry = Entry(add_student_window)
    stu_father_entry.grid(row=3, column=1)
    stu_mother_entry = Entry(add_student_window)
    stu_mother_entry.grid(row=4, column=1)
    d_o_b_entry = Entry(add_student_window)
    d_o_b_entry.grid(row=5, column=1)
    d_o_b_entry.insert(0, "YYYY-MM-DD")
    phn_no_entry = Entry(add_student_window)
    phn_no_entry.grid(row=6, column=1)
    phn_no_entry.insert(0, "Only Digits")
    email_entry = Entry(add_student_window)
    email_entry.grid(row=7, column=1)

    add_button = Button(add_student_window,
                        text="Insert Record", command=add_in_database)
    add_button.grid(row=9, column=0, columnspan=2, pady = 15)

    # Closing Connection
    db.commit()
    db.close()


# Function to Remove Student
def remove_student():

    global reg_no_delete_entry
    global remove_student_window

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')

    # Creating New Window
    remove_student_window = Tk()
    remove_student_window.title("Remove Student")
    remove_student_window.iconbitmap(r"#Location of theimage of icon")
    remove_student_window.geometry("175x50")

    reg_no_delete_entry = Entry(remove_student_window)
    reg_no_delete_entry.grid(row=0, column=1)
    Label(remove_student_window, text="Enter ID").grid(row=0, column=0)

    Button(remove_student_window, text="Remove Record",
           command=remove_from_database).grid(row=1, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Function to Pay Fee
def pay_fee():

    global pay_fee_reg_no
    global pay_fee_window

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')

    # Creating New Window
    pay_fee_window = Tk()
    pay_fee_window.title("Pay Fee")
    pay_fee_window.iconbitmap(r"#Location of theimage of icon")
    pay_fee_window.geometry("225x200")

    pay_fee_reg_no = Entry(pay_fee_window)
    pay_fee_reg_no.grid(row=0, column=1)
    Label(pay_fee_window, text="Enter ID").grid(row=0, column=0)

    Button(pay_fee_window, text="Continue", command=fee_data).grid(
        row=1, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Function to Check Fee Structure
def check_fee_structure():

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')
    cursor = db.cursor()

    # Creating New Window
    fee_structure_window = Tk()
    fee_structure_window.title("Fee Student")
    fee_structure_window.iconbitmap(r"#Location of theimage of icon")
    fee_structure_window.geometry("200x240")

    cursor.execute("""CREATE TABLE IF NOT EXISTS FEE_STRUCTURE(
        class_6  BIGINT NOT NULL,
        class_7  BIGINT NOT NULL,
        class_8  BIGINT NOT NULL,
        class_9  BIGINT NOT NULL,
        class_10  BIGINT NOT NULL,
        class_11_science  BIGINT NOT NULL,
        class_11_commerce  BIGINT NOT NULL,
        class_11_humanities  BIGINT NOT NULL,
        class_12_science  BIGINT NOT NULL,
        class_12_commerce  BIGINT NOT NULL,
        class_12_humanities  BIGINT NOT NULL
        )
        ENGINE = INNODB
        """)

    cursor.execute("""INSERT INTO FEE_STRUCTURE (
        class_6,
        class_7,
        class_8,
        class_9,
        class_10,
        class_11_science,
        class_11_commerce,
        class_11_humanities,
        class_12_science,
        class_12_commerce,
        class_12_humanities
        ) 
        VALUES( {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})"""
                   .format(
                       10000,
                       15000,
                       20000,
                       30000,
                       35000,
                       45000,
                       40000,
                       40000,
                       50000,
                       45000,
                       40000
                   ))

    cursor.execute("select * from fee_structure")
    check_fee_list = cursor.fetchall()

    # Displaying Fees in Form of Labels
    Label(fee_structure_window, text="For Class 6").grid(row=0, column=0)
    Label(fee_structure_window, text="For Class 7").grid(row=1, column=0)
    Label(fee_structure_window, text="For Class 8").grid(row=2, column=0)
    Label(fee_structure_window, text="For Class 9").grid(row=3, column=0)
    Label(fee_structure_window, text="For Class 10").grid(row=4, column=0)
    Label(fee_structure_window, text="For Class 11(SCIENCE)").grid(row=5, column=0)
    Label(fee_structure_window, text="For Class 11(COMMERCE)").grid(row=6, column=0)
    Label(fee_structure_window, text="For Class 11(HUMANITIES)").grid(
        row=7, column=0)
    Label(fee_structure_window, text="For Class 12(SCIENCE)").grid(row=8, column=0)
    Label(fee_structure_window, text="For Class 12(COMMERCE)").grid(row=9, column=0)
    Label(fee_structure_window, text="For Class 12(HUMANITIES)").grid(
        row=10, column=0)

    Label(fee_structure_window, text=" : ").grid(row=0, column=1)
    Label(fee_structure_window, text=" : ").grid(row=1, column=1)
    Label(fee_structure_window, text=" : ").grid(row=2, column=1)
    Label(fee_structure_window, text=" : ").grid(row=3, column=1)
    Label(fee_structure_window, text=" : ").grid(row=4, column=1)
    Label(fee_structure_window, text=" : ").grid(row=5, column=1)
    Label(fee_structure_window, text=" : ").grid(row=6, column=1)
    Label(fee_structure_window, text=" : ").grid(row=7, column=1)
    Label(fee_structure_window, text=" : ").grid(row=8, column=1)
    Label(fee_structure_window, text=" : ").grid(row=9, column=1)
    Label(fee_structure_window, text=" : ").grid(row=10, column=1)

    Label(fee_structure_window, text=str(
        check_fee_list[0][0])).grid(row=0, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][1])).grid(row=1, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][2])).grid(row=2, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][3])).grid(row=3, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][4])).grid(row=4, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][5])).grid(row=5, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][6])).grid(row=6, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][7])).grid(row=7, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][8])).grid(row=8, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][9])).grid(row=9, column=2)
    Label(fee_structure_window, text=str(
        check_fee_list[0][10])).grid(row=10, column=2)

    # Closing Connection
    db.commit()
    db.close()


# Function to Mark Attendance
def mark_attendance():

    global mark_attendance_date
    global mark_attendance_window

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')

    # Creating New Window
    mark_attendance_window = Tk()
    mark_attendance_window.title("Mark Attendance")
    mark_attendance_window.iconbitmap(r"#Location of theimage of icon")
    mark_attendance_window.geometry("200x100")

    Label(mark_attendance_window, text="ENTER DATE").grid(row=0, column=0)
    mark_attendance_date = Entry(mark_attendance_window)
    mark_attendance_date.grid(row=0, column=1)
    mark_attendance_date.insert(0, "YYYY_MM_DD")

    Button(mark_attendance_window, text="Continue",
           command=adding_date_column).grid(row=1, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Function to Check Attendance
def check_attendance():
    global check_attendance_date
    global check_attendance_reg_no
    global check_attendance_window

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')

    # Creating New Window
    check_attendance_window = Tk()
    check_attendance_window.title("Check Attendance")
    check_attendance_window.iconbitmap(r"#Location of theimage of icon")
    check_attendance_window.geometry("200x125")

    Label(check_attendance_window, text="Reg. No").grid(row=0, column=0)
    Label(check_attendance_window, text="Date").grid(row=1, column=0)
    check_attendance_date = Entry(check_attendance_window)
    check_attendance_reg_no = Entry(check_attendance_window)
    check_attendance_date.grid(row=1, column=1)
    check_attendance_reg_no.grid(row=0, column=1)
    check_attendance_date.insert(0, "YYYY_MM_DD")

    Button(check_attendance_window, text="Continue",
           command=check_attendance_from_database).grid(row=2, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Function to Check Profile
def check_profile():
    global check_profile_reg_no
    global check_student_window

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')

    # Creating New Window
    check_student_window = Tk()
    check_student_window.title("Check Profile")
    check_student_window.iconbitmap(r"#Location of theimage of icon")
    check_student_window.geometry("225x270")

    check_profile_reg_no = Entry(check_student_window)
    check_profile_reg_no.grid(row=0, column=1)
    Label(check_student_window, text="Enter ID").grid(row=0, column=0)

    Button(check_student_window, text="Check Record",
           command=check_profile_from_database).grid(row=1, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Function to Edit Profile
def edit_proflie():

    global edit_student_window
    global edit_profile_reg_no

    # Connection with database
    db = mysql.connector.connect(
        host="localhost", user="root", password="********", database="project")
    if db.is_connected() == False:
        print('error connecting to MYSQL database')

    # Creating New Window
    edit_student_window = Tk()
    edit_student_window.title("Edit Profile")
    edit_student_window.iconbitmap(r"#Location of theimage of icon")
    edit_student_window.geometry("225x270")

    edit_profile_reg_no = Entry(edit_student_window)
    edit_profile_reg_no.grid(row=0, column=1)
    Label(edit_student_window, text="Enter ID").grid(row=0, column=0)

    Button(edit_student_window, text="Show Record",
           command=show_profile_from_database).grid(row=1, column=0, columnspan=2)

    # Closing Connection
    db.commit()
    db.close()


# Creating and Placing the Welcome Text

Label(root, text="😎ACHIEVER'S CLUB😎", font=('Garamond', 20, 'bold')).pack()
Label(root, text="😎The Place Where You Start Achieving Your Goals😎", pady=10).pack()


# Creating Button on Main Screen
Button(root, text="Add Student", pady=5, width=25, command=add_student,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()
Button(root, text="Remove Student", pady=5, width=25, command=remove_student,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()
Button(root, text="Pay Fee", pady=5, width=25, command=pay_fee,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()
Button(root, text="Check Fee Structure", pady=5, width=25, command=check_fee_structure,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()
Button(root, text="Mark Attendance", pady=5, width=25, command=mark_attendance,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()
Button(root, text="Check Attendance", pady=5, width=25, command=check_attendance,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()
Button(root, text="Check Profile", pady=5, width=25, command=check_profile,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()
Button(root, text="Edit Profile", pady=5, width=25, command=edit_proflie,
       fg='pink', bg='blue', font=('Rockwell', 15, 'bold')).pack()


# Welcome Sound
speak("  Welcome to Achiever's Club")


# Closing Connection
db.commit()
db.close()
root.mainloop()
