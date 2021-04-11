import mysql.connector
global active_mail
global active_id
global log_in
def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325"
    )
    database="no"
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for i in mycursor:
        if i[0]=="maindatabase":
            database="yes"
            break
        else:
            pass
    if database == "no":
        create_database()
    else:
        pass
def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE maindatabase")
def table(t_n):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="project2325",
            database="maindatabase",
        )
    table="no"
    check_table=t_n
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for i in mycursor:
        if i[0] == check_table:
            table = "yes"
            break
        else:
            pass
    if table == "no":
        create_table(check_table)
    else:
        pass
def create_table(table):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    if table =="student":
        mycursor.execute("CREATE TABLE student (name varchar(150),id varChar(30),department varChar(100),gender varchar(10),section varchar(10),password varchar(100),que1 varchar(100),que2 varchar(100),mail varchar(100),PRIMARY KEY(id))")
    elif table=="teacher":
        mycursor.execute("CREATE TABLE teacher(name varchar(150),id varChar(30),designation varChar(30),department varChar(100),faculty varChar(100),gender varchar(10),password varchar(100),que1 varchar(100),que2 varchar(100),phone varChar(20),cellphone varChar(20),mail varchar(100),status varChar(10),PRIMARY KEY(id))")
    elif table=="course":
        mycursor.execute(
            "CREATE TABLE course (stdid varChar(30),coursename varchar(50),coursecode varchar(50),teachername varchar(150),advisorid varchar(30))")
    elif table=="admin":
        mycursor.execute(
            "CREATE TABLE admin (name varchar(150),mail varChar(100),password varchar(100),que1 varchar(100),que2 varchar(100),status varChar(10),role varChar(10),PRIMARY KEY(mail))")
def main_function():
    database()
    global active_mail
    global active_id
    global log_in
    active_mail=""
    active_id=""
    log_in = False
    table("admin")
    table("student")
    table("teacher")
    table("course")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT mail FROM admin")
    re_su_lt = mycursor.fetchall()
    if re_su_lt:
        print("")
    else:
        print("Create Admin Account")
        admin_create_account()
    while True:
        print(""" 
          1. SIGN IN
          2. SIGN UP
          3. Forget Password ?
          4. EXIT

          Enter Your Choose : 
        """)
        choice = input()
        if choice == "1":
            login_mail = input("Enter Mail : ")
            login_passwd = input("Enter Password : ")
            login(login_mail,login_passwd)
        elif choice == "2":
            create()
        elif choice == "3":
            forget_password(log_in)
        elif choice == "4":
            exit()
        else:
            main_function()
def create():
    print("""
        1. Student
        2. Teacher
        3. Admin
        4. Back
        5. Exit
        """)
    cre = input()
    if cre=='1':
        student_create_account()
        main_function()
    elif cre=='2':
        teacher_create_account()
    elif cre == '3':
        admin_create_account()
    elif cre == '4':
        main_function()
    elif cre=='5':
        exit()
def student_create_account():
    name= input("Enter Full Name :  ")
    while True:
        if len(name)>2:
            break
        else:
            name = input("Enter Full Name :  ")
    mail= input("Enter Mail (Length (8-100) ) : ")
    while True:
        ma_il = check_mail(mail)
        if len(mail) >= 8 and len(mail) <= 100 and ma_il == 0:
            break
        else:
            mail= input("Enter Mail (Length (8-100) ) : ")
    password=input("Enter Password (length (5-100)):  ")
    while True:
        if len(password) >=5 and len(password) <= 100:
            break
        else:
            password = input("Wrong ! Enter Password (length (5-100)):  ")

    id= input("Enter ID (length (8-30)) : ")
    while True:
        i_d = check_id(id)
        if len(id) >= 8 and len(id) <= 30 and i_d==0 :
            break
        else:
            id= input("Enter ID (length (8-30)) : ")
    department = input("Enter Department (length (2-100)):  ")
    if len(department) < 2 and len(department) <= 100:
        while True:
            department = input("Wrong ! Enter Department (length (2-100)):  ")
            if len(department) < 3 and len(department) <= 100:
                break
    else:
        pass
    print("Answer those Question ? ")
    ans1 = input("Primary School name ?")
    if ans1=="":
        while True:
            ans1 = input("Primary School name ?")
            if ans1 == "":
                continue
            else:
                break
    else:
        pass

    ans2 = input("Favourite Teacher name ?")
    if ans2=="":
        while True:
            ans2 = input("Favourite Teacher name ?")
            if ans2 == "":
                continue
            else:
                break
    else:
        pass
    gender=str(input("""
    Enter Gender :
    M. Male
    F. Female
    """))
    if gender=="M" or gender=="m":
        gender="Male"
    elif gender=="F" or gender=="f":
        gender="Female"
    else:
        gender=""
    section = input("Enter Section : ")

    # Insert Data
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    query = "INSERT INTO student (name,id ,department,gender,section ,password ,que1 ,que2,mail )VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    s = (name,id,department,gender,section,password,ans1,ans2,mail)
    mycursor.execute(query,s)
    mydb.commit()
    print("-------------------------*****-------------------------")
    print("|                  Create Successfully !                 |")
    print("-------------------------*****-------------------------")
def teacher_create_account():
    name= input("Enter Full Name :  ")
    while True:
        if len(name)>2:
            break
        else:
            name = input("Enter Full Name :  ")
    mail= input("Enter Mail (Length (8-10) ) : ")
    while True:
        ma_il = check_mail(mail)
        if len(mail) >= 8 and len(mail) <= 100 and ma_il==0 :
            break
        else:
            mail= input("Enter Mail (Length (8-100) ) : ")
    password=input("Enter Password (length (5-100)):  ")

    while True:
        password = input(" Enter Password (length (5-100)):  ")
        if len(password)>5 and len(password)<=100:
            break

    id= input("Enter ID (length (8-30)) : ")
    while True:
        i_d = check_id(id)
        if len(id) >= 8 and len(id) <= 30 and i_d==0:
            break
        else:
            id= input("Enter ID (length (8-30)) : ")
    designation = input("Enter Designation (length (5-100)):  ")
    if len(designation) < 5 or len(designation) > 100:
        while True:
            designation = input("Wrong ! Enter Designation (length (5-100)):  ")
            if len(designation) < 5 or len(designation) > 100:
                break
    else:
        pass
    department = input("Enter Department (length (2-100)):  ")
    while True:
        if len(department) >= 2 and len(department) <= 100:
            break
        department = input("Wrong ! Enter Department (length (2-100)):  ")

    faculty = input("Enter Faculty (length (3-100)):  ")
    if len(faculty) < 3 or len(faculty) > 100:
        while True:
            faculty = input("Wrong ! Enter Department (length (3-100)):  ")
            if len(faculty) < 3 or len(faculty) > 100:
                break
    else:
        pass
    phone = input("Enter Phone Number :  ")
    cellphone = input("Enter Cell Phone Number :  ")
    print("Answer those Question ? ")
    ans1 = input("Primary School name ?")
    if ans1=="":
        while True:
            ans1 = input("Primary School name ?")
            if ans1 == "":
                continue
            else:
                break
    else:
        pass

    ans2 = input("Favourite Teacher name ?")
    if ans2=="":
        while True:
            ans2 = input("Favourite Teacher name ?")
            if ans2 == "":
                continue
            else:
                break
    else:
        pass
    gender=str(input("""
    Enter Gender :
    M. Male
    F. Female
    """))
    if gender=="M" or gender=="m":
        gender="Male"
    elif gender=="F" or gender=="f":
        gender="Female"
    else:
        gender=""
    status="pending"
    # Insert Data
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    query = "INSERT INTO teacher (name,id,designation,department,faculty,gender,password,que1,que2,phone,cellphone,mail,status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    s = (name,id,designation,department,faculty,gender,password,ans1,ans2,phone,cellphone,mail,status)
    mycursor.execute(query,s)
    mydb.commit()
    print("-------------------------*****-------------------------")
    print("|                  Create Successfully !                 |")
    print("-------------------------*****-------------------------")
def admin_create_account():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    name = input("Enter Full Name :  ")
    while True:
        if len(name) >=2:
            break
        else:
            name = input("Enter Full Name :  ")
    mail = input("Enter Mail (Length (8-10) ) : ")
    while True:
        ma_il = check_mail(mail)
        if len(mail) >= 8 and len(mail) <= 100 and ma_il == 0:
            break
        else:
            mail = input("Enter Mail (Length (8-100) ) : ")
    password = input("Enter Password (length (5-100)):  ")
    if len(password) >= 5 and len(password) <= 100:
        pass
    else:
        while True:
            password = input("Wrong ! Enter Password (length (5-100)):  ")
            if len(password) >=5 and len(password) <= 100:
                break
    print("Answer those Question ? ")
    ans1 = input("Primary School name ?")
    if ans1 == "":
        while True:
            ans1 = input("Primary School name ?")
            if ans1 == "":
                continue
            else:
                break
    else:
        pass

    ans2 = input("Favourite Teacher name ?")
    if ans2 == "":
        while True:
            ans2 = input("Favourite Teacher name ?")
            if ans2 == "":
                continue
            else:
                break
    else:
        pass
    status="pending"
    role="parent"
    query = "SELECT * from admin"
    mycursor.execute(query)
    result = mycursor.fetchall()
    if result:
        status="pending"
        role = "child"
    else:
        status = "approved"
        role = "parent"
    query = "INSERT INTO admin (name,mail,password,que1,que2,status,role)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    s = (name,mail, password, ans1, ans2,status,role)
    mycursor.execute(query, s)
    mydb.commit()
    print("-------------------------*****-------------------------")
    print("|                  Create Successfully !                 |")
    print("-------------------------*****-------------------------")
def check_mail(m_ail):
    global  active_mail
    global active_id
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    count=0
    edit_query=("SELECT mail FROM student WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result =mycursor.fetchall()
    for db in result:
        if db[0]==m_ail:
            count+=1
            return count
    edit_query=("SELECT mail FROM teacher WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result = mycursor.fetchall()
    for db in result:
        if db[0]==m_ail:
            count += 1
            return count
    edit_query = ("SELECT mail FROM admin WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result = mycursor.fetchall()
    for db in result:
        if db[0] == m_ail:
            count += 1
            return count
    return count
def check_id(id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    found=0
    mycursor.execute("SELECT id FROM student")
    for db in mycursor:
        if db[0] == id:
            found+=1
            return found
    mycursor.execute("SELECT id FROM teacher")
    for db in mycursor:
        if db[0] == id:
            found += 1
            return found
    return found
def login(input_mail,input_pass):
    global log_in
    global active_mail
    global active_id
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT mail,password,id FROM student")
    for i in mycursor:
        if i[0] == input_mail :
            if i[1]==input_pass:
                active_mail = input_mail
                active_id=i[2]
                log_in = True
                student()
            else:
                print("Wrong Password!")
                main_function()

        else:
            pass
    tcursor = mydb.cursor()
    tcursor.execute("SELECT mail,password,id,status FROM teacher")
    for i in tcursor:
        if i[0] == input_mail  :
            if i[1] == input_pass:
                if i[3]=="approved":
                    active_mail = input_mail
                    active_id = i[2]
                    log_in = True
                    teacher()
                else:
                    print("This account haven't approved by admin.")
                    main_function()
            else:
                print("Wrong Password!")
                main_function()
        else:
            pass
    mycursor.execute("SELECT mail,password,status FROM admin")
    for i in mycursor:
        if i[0] == input_mail:
            if i[1] == input_pass:
                if i[2]=="approved":
                    active_mail = input_mail
                    active_id = ""
                    log_in = True
                    admin()
                else:
                    print("This account haven't approved by admin.")
                    main_function()
            else:
                print("Wrong Password!")
                main_function()

        else:
            pass
    if log_in!=True:
        print("No account in this mail !")
def student():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    global active_mail
    global active_id
    global log_in
    e_name = ""
    e_id = ""
    e_department = ""
    e_mail = ""
    e_ans1 = ""
    e_ans2 = ""
    e_gender = ""
    e_section=""
    while True:
        p_s = input("1. Profile\n2. Profile Edit\n3. Course List\n4. Course Search\n5. Change Password\n6. Logout\n")
        if p_s=='1':
            query=("SELECT * from student WHERE mail=%s and id=%s")
            s = (active_mail,active_id)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ",row[0])
                print("ID : ", row[1])
                print("Department : ",row[2])
                print("Gender : ", row[3])
                print("Section : ", row[4])
                print("Ans : ", row[6])
                print("Ans : ", row[7])
                print("Mail : ", row[8])
            query = "SELECT coursename,coursecode,teachername,advisorid from course WHERE stdid=%s"
            s = (active_id,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            if result:
                print("\nCourse List : \n")
                for q in result:
                    print("Course Name : (", q[0],") "," Course Code : (", q[1],")"," Teacher Name : (", q[2],")"," Advisor Id : (", q[3],")")
            else:
                print("Havn't take any course.")
        elif p_s=='2':
            query = ("SELECT * FROM student WHERE mail=%s and id=%s")
            s = (active_mail, active_id)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_name = input("Enter Full Name :  ")
                    while True:
                        if len(e_name) > 2:
                            break
                        else:
                            e_name = input("Enter Full Name :  ")
                else:
                    e_name = row[0]
                print("ID : ", row[1])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_id = input("Enter ID (length (8-30)) : ")
                    while True:
                        i_d = check_id(e_id)
                        if len(e_id) >= 8 and len(e_id) <= 30 and i_d == 0:
                            break
                        else:
                            e_id = input("Enter ID (length (8-30)) : ")
                else:
                    e_id = row[1]
                print("Department : ", row[2])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_department = input("Enter Department (length (3-100)):  ")
                    if len(e_department) < 3 or len(e_department) > 100:
                        while True:
                            e_department = input("Wrong ! Enter Department (length (3-100)):  ")
                            if len(e_department) < 3 or len(e_department) > 100:
                                break
                    else:
                        pass
                else:
                    e_department = row[2]
                print("Gender : ", row[3])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_gender = str(input("""
                                    Enter Gender :
                                    M. Male
                                    F. Female
                                    """))
                    if e_gender == "M" or e_gender == "m":
                        e_gender = "Male"
                    elif e_gender == "F" or e_gender == "f":
                        e_gender = "Female"
                    else:
                        e_gender = ""
                else:
                    e_gender = row[3]
                print("Section : ", row[4])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_section= input("Enter Gender : ")
                else:
                    e_section = row[4]
                print("Primary School name ?")
                print("Ans : ", row[6])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_ans1 = input("Primary School name ?")
                    if e_ans1 == "":
                        while True:
                            e_ans1 = input("Primary School name ?")
                            if e_ans1 == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_ans1 = row[6]
                print("Favourite Teacher name ?")
                print("Ans : ", row[7])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_ans2 = input("Favourite Teacher name ?")
                    if e_ans2 == "":
                        while True:
                            e_ans2 = input("Favourite Teacher name ?")
                            if e_ans2 == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_ans2 = row[7]
                print("Mail : ", row[8])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_mail = input("Enter Mail (Length (11-10) ) : ")
                    while True:
                        ma_il = check_mail(e_mail)
                        if len(e_mail) >= 11 and len(e_mail) <= 100 and ma_il == 0:
                            break
                        else:
                            e_mail = input("Enter Mail (Length (11-100) ) : ")
                else:
                    e_mail = row[8]
            mycur = mydb.cursor()
            edit_query = ("UPDATE student SET name=%s,id=%s,department=%s,gender=%s,section=%s,que1=%s,que2=%s,mail=%s WHERE mail=%s and id=%s")
            edit = (e_name, e_id,  e_department,   e_gender,e_section, e_ans1, e_ans2,e_mail, active_mail, active_id,)
            mycur.execute(edit_query, edit)
            mydb.commit()
            active_mail = e_mail
            active_id = e_id
        elif p_s=='3':
            query = "SELECT coursename,coursecode,teachername,advisorid from course WHERE stdid=%s"
            s = (active_id,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            loop=1
            if result :
                for q in result:
                    print("Course Name : (", q[0], ") ", " Course Code : (", q[1], ")", " Teacher Name : (", q[2], ")"," Advisor Id : (", q[3], ")")
                    loop+=1
            else:
                print("Havn't take any course.")
        elif p_s=='4':
            code_name=input("Enter course name or code : ")
            query = "SELECT coursename,coursecode,teachername,advisorid from course WHERE stdid=%s and (coursename=%s or coursecode=%s)"
            s = (active_id,code_name,code_name,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            if result :
                for q in result:
                    print("Course Name : (", q[0],") "," Course Code : (", q[1],")"," Teacher Name : (", q[2],")"," Advisor Id : (", q[3],")")
            else:
                print("No result.")
        elif p_s=='5':
            forget_password(log_in)
        elif p_s=='6':
            active_mail = ""
            active_id = ""
            log_in = False
            main_function()
def teacher():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    global active_mail
    global active_id
    global log_in
    e_name=""
    e_id=""
    e_designation=""
    e_department=""
    e_faculty=""
    e_mail=""
    e_ans1=""
    e_ans2=""
    e_gender=""
    e_phone=""
    e_cellphone = ""
    mycursor = mydb.cursor()
    while True:
        p_s = input("1. Profile\n2. Profile Edit\n3. View / Search\n4. Course Add\n5. Course Delete\n6. Change Password\n7. Logout\n")
        if p_s == '1':
            query = ("SELECT * FROM teacher WHERE mail=%s and id=%s")
            s = (active_mail, active_id)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                print("ID : ", row[1])
                print("Designation : ", row[2])
                print("Department : ",row[3])
                print("Faculty : ", row[4])
                print("Gender : ", row[5])
                print("Primary School name ?")
                print("Ans : ", row[7])
                print("Favourite Teacher name ?")
                print("Ans : ", row[8])
                print("Phone : ",row[9])
                print("Cellphone : ", row[10])
                print("Mail : ", row[11])
        elif p_s == '2':
            query = ("SELECT * FROM teacher WHERE mail=%s and id=%s")
            s = (active_mail, active_id)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                a=input("1. Edit\n2. Skip")
                if a=='1':
                    e_name = input("Enter Full Name :  ")
                    while True:
                        if len(e_name) > 2:
                            break
                        else:
                            e_name = input("Enter Full Name :  ")
                else:
                    e_name=row[0]
                print("ID : ", row[2])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_id = input("Enter ID (length (8-30)) : ")
                    while True:
                        i_d = check_id(e_id)
                        if len(e_id) >= 8 and len(e_id) <= 30 and i_d == 0:
                            break
                        else:
                            e_id = input("Enter ID (length (8-30)) : ")
                else:
                    e_id=row[2]
                print("Department : ",row[4])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_department = input("Enter Department (length (3-100)):  ")
                    if len(e_department) < 3 or len(e_department) > 100:
                        while True:
                            e_department = input("Wrong ! Enter Department (length (3-100)):  ")
                            if len(e_department) < 3 or len(e_department) > 100:
                                break
                    else:
                        pass
                else:
                    e_department=row[4]
                print("Designation : ", row[3])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_designation = input("Enter Designation (length (5-100)):  ")
                    if len(e_designation) < 5 or len(e_designation) > 100:
                        while True:
                            e_designation = input("Wrong ! Enter Designation (length (5-100)):  ")
                            if len(e_designation) < 5 or len(e_designation) > 100:
                                break
                    else:
                        pass
                else:
                    e_designation=row[3]
                print("Faculty : ", row[5])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_faculty = input("Enter Faculty (length (3-100)):  ")
                    if len(e_faculty) < 3 or len(e_faculty) > 100:
                        while True:
                            e_faculty = input("Wrong ! Enter Department (length (3-100)):  ")
                            if len(e_faculty) < 3 or len(e_faculty) > 100:
                                break
                    else:
                        pass
                else:
                    e_faculty=row[5]

                print("Gender : ", row[12])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_gender = str(input("""
                        Enter Gender :
                        M. Male
                        F. Female
                        """))
                    if e_gender == "M" or e_gender == "m":
                        e_gender = "Male"
                    elif e_gender == "F" or e_gender == "f":
                        e_gender = "Female"
                    else:
                        e_gender = ""
                else:
                    e_gender=row[12]
                print("Primary School name ?")
                print("Ans : ", row[10])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_ans1 = input("Primary School name ?")
                    if e_ans1 == "":
                        while True:
                            e_ans1 = input("Primary School name ?")
                            if e_ans1 == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_ans1=row[10]
                print("Favourite Teacher name ?")
                print("Ans : ", row[11])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_ans2 = input("Favourite Teacher name ?")
                    if e_ans2 == "":
                        while True:
                            e_ans2 = input("Favourite Teacher name ?")
                            if e_ans2 == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_ans2=row[11]
                print("Phone : ",row[6])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_phone = input("Enter Phone Number :  ")
                else:
                    e_phone=row[6]
                print("Cellphone : ", row[7])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_cellphone = input("Enter Cell Phone Number :  ")
                else:
                    e_cellphone=row[7]
                print("Mail : ", row[8])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_mail = input("Enter Mail (Length (11-10) ) : ")
                    while True:
                        ma_il = check_mail(e_mail)
                        if len(e_mail) >= 11 and len(e_mail) <= 100 and ma_il ==0:
                            break
                        else:
                            e_mail = input("Enter Mail (Length (11-100) ) : ")
                else:
                    e_mail=row[8]
            mycur = mydb.cursor()
            edit_query = ("UPDATE teacher SET name=%s,id=%s,designation=%s,department=%s,faculty=%s,mail=%s,que1=%s,que2=%s,gender=%s,phone=%s,cellphone=%s WHERE mail=%s and id=%s")
            edit = (e_name,e_id,e_designation,e_department,e_faculty,e_mail,e_ans1,e_ans2,e_gender,e_phone,e_cellphone,active_mail,active_id)
            mycur.execute(edit_query,edit)
            mydb.commit()
            active_mail=e_mail
            active_id=e_id
        elif p_s=='3':
            student_id=input("Enter student id : ")
            query = "SELECT * from student WHERE id=%s"
            s = (student_id,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                print("ID : ", row[1])
                print("Department : ", row[2])
                print("Gender : ", row[3])
                print("Section : ", row[4])
                print("Mail : ", row[8])
            query = "SELECT coursename,coursecode,teachername from course WHERE stdid=%s"
            s = (student_id,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            if result:
                print("\nCourse List : \n")
                for q in result:
                    print("Course Name : (", q[0], ") ", " Course Code : (", q[1], ")", " Teacher Name : (", q[2],")" )
            else:
                print("Havn't take any course.")
        elif p_s == '4':
            student_id=input("Enter student id : ")
            mycursor.execute("SELECT id FROM student")
            for i in mycursor:
                if i[0] ==  student_id:
                    print("Student found!")
                    q_u="SELECT coursename,coursecode,teachername FROM course WHERE stdid = %s "
                    sp=(i[0],)
                    mycursor.execute(q_u,sp)
                    result = mycursor.fetchall()
                    if result:
                        print("\nCourse List : \n")
                        for q in result:
                            print("Course Name : (", q[0], ") ", " Course Code : (", q[1], ")", " Teacher Name : (",
                                  q[2], ")")
                    else:
                        print("Havn't take any course.")
                else:
                    pass
            course_name=input("Enter course name : ")
            while True:
                c_name_count = check_course_name(course_name,student_id)
                if len(course_name) >= 1 and len(course_name) <= 100 and c_name_count==0:
                    break
                else:
                    print("Don't maintain all required!")
                    qwe=input("1. Try again\n2. Back")
                    if qwe=='1':
                        course_name = input("Enter course name : ")
                    else:
                        teacher()
            #course code
            course_code=input("Enter course code : ")
            while True:
                c_code_count=check_course_code(course_code, student_id)
                if len(course_code) >= 1 and len(course_code) <= 100 and c_code_count==0:
                    break
                else:
                    print("Don't maintain all required!")
                    qwe = input("1. Try again\n2. Back")
                    if qwe == '1':
                        course_code = input("Enter course code : ")
                    else:
                        teacher()
            course_teacher_name=input("Enter course teacher name : ")
            while True:
                if len(course_teacher_name) >= 1 and len(course_teacher_name) <= 100 :
                    break
                else:
                    print("Don't maintain all required!")
                    qwe = input("1. Try again\n2. Back")
                    if qwe == '1':
                        course_teacher_name = input("Enter course teacher name : ")
                    else:
                        teacher()
            mycursor = mydb.cursor()
            query = "INSERT INTO course (stdid,coursename,coursecode,teachername,advisorid)VALUES(%s,%s,%s,%s,%s)"
            s = (student_id,course_name,course_code,course_teacher_name,active_id)
            mycursor.execute(query, s)
            mydb.commit()
            print("-------------------------*****-------------------------")
            print("|                  Add Successfully !                 |")
            print("-------------------------*****-------------------------")
            q_u2 = "SELECT  coursename,coursecode,teachername  FROM course WHERE stdid = %s"
            sp2 = (student_id,)
            mycursor.execute(q_u2, sp2)
            re_sult2 = mycursor.fetchall()
            for q in re_sult2:
                print("Course Name : (", q[0], ") ", " Course Code : (", q[1], ")", " Teacher Name : (",
                      q[2], ")")
        elif p_s == '5':
            student_id = input("Enter student id : ")
            count = 0
            mycursor.execute("SELECT id FROM student")
            sult = mycursor.fetchall()
            for i in sult:
                if i[0] == student_id:
                    print("Student found!")
                    q_u = "SELECT coursename,coursecode,teachername FROM course WHERE stdid = %s "
                    sp = (i[0],)
                    mycursor.execute(q_u, sp)
                    result = mycursor.fetchall()
                    if result:
                        print("\nCourse List : \n")
                        for q in result:
                            count+=1
                            print("Course Name : (", q[0], ") ", " Course Code : (", q[1], ")", " Teacher Name : (",
                                  q[2], ")")
                    else:
                        print("Havn't take any course.")
                    break
                else:
                    pass
            if count>0:
                name_code = input("Enter course name or code : ")
                q_u = "SELECT coursename,coursecode FROM course WHERE stdid = %s "
                s = (student_id,)
                mycursor.execute(q_u, s)
                res_ult = mycursor.fetchall()
                for i in res_ult:
                    if i[0]==name_code or i[1]==name_code:
                        q_o = "DELETE FROM course WHERE stdid = %s and (coursename=%s or coursecode=%s) and advisorid=%s"
                        sp21 = (student_id,name_code,name_code,active_id,)
                        mycursor.execute(q_o, sp21)
                        mydb.commit()
                        print("-------------------------*****-------------------------")
                        print("|                  Delete Successfully !                 |")
                        print("-------------------------*****-------------------------")
                        break
        elif p_s=='6':
            forget_password(log_in)
        elif p_s == '7':
            active_mail = ""
            active_id = ""
            log_in = False
            main_function()
def admin():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    global active_mail
    global active_id
    global log_in
    e_name=""
    e_mail=""
    e_ans1=""
    e_ans2=""
    mycursor = mydb.cursor()
    while True:
        in_put = input("1. Profile\n2. Edit Profile\n3. Approve Account\n4. Delete Account\n5. Change Password\n6. Logout\n")
        if in_put=='1':
            query = ("SELECT * from admin WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                print("Mail : ", row[1])
                print("Password : ", row[2])
                print("Primary School name : ", row[3])
                print("Favourite Teacher Name : ", row[4])
        elif in_put=="2":
            query = ("SELECT name,mail,que1,que2 from admin WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_name = input("Enter Full Name :  ")
                    while True:
                        if len(e_name) > 2:
                            break
                        else:
                            e_name = input("Enter Full Name :  ")
                else:
                    e_name = row[0]
                print("Mail : ", row[1])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_mail = input("Enter Mail (Length (11-10) ) : ")
                    while True:
                        ma_il = check_mail(e_mail)
                        if len(e_mail) >= 11 and len(e_mail) <= 100 and ma_il == 0:
                            break
                        else:
                            e_mail = input("Enter Mail (Length (11-100) ) : ")
                else:
                    e_mail = row[1]
                print("Primary School name ?")
                print("Ans : ", row[2])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_ans1 = input("Primary School name ?")
                    if e_ans1 == "":
                        while True:
                            e_ans1 = input("Primary School name ?")
                            if e_ans1 == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_ans1 = row[2]
                print("Favourite Teacher name ?")
                print("Ans : ", row[3])
                a = input("1. Edit\n2. Skip\n")
                if a == '1':
                    e_ans2 = input("Favourite Teacher name ?")
                    if e_ans2 == "":
                        while True:
                            e_ans2 = input("Favourite Teacher name ?")
                            if e_ans2 == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_ans2 = row[3]
            edit_query = (
                "UPDATE admin SET name=%s ,mail=%s,que1=%s,que2=%s WHERE mail=%s")
            edit = (e_name, e_mail, e_ans1, e_ans2,active_mail,)
            mycursor.execute(edit_query, edit)
            mydb.commit()
            active_mail = e_mail
            active_id = ""
            print("Update Complete!")
        elif in_put=='3':
            x=input("1. Admin\n2. Teacher\n")
            if x=='1':
                a=input("Enter mail : ")
                query = ("SELECT mail from admin WHERE mail=%s")
                s = (a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                status="approved"
                if result :
                    print("Account Found!")
                    edit_query = (
                        "UPDATE admin SET status=%s WHERE mail=%s")
                    edit = (status,a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Approved Complete!")
                else:
                    print("No Account Found!")
            elif x=='2':
                a = input("Enter mail or id : ")
                query = ("SELECT mail,id from teacher WHERE mail=%s or id =%s")
                s = (a,a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                status = "approved"
                if result:
                    print("Account Found!")
                    edit_query = (
                        "UPDATE teacher SET status=%s WHERE mail=%s or id = %s")
                    edit = (status,a,a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Approved Complete!")
                else:
                    print("No Account Found!")
        elif in_put=='4':
            x = input("1. Admin\n2. Teacher\n3. Student\n")
            if x == '1':
                a = input("Enter mail : ")
                query = ("SELECT mail,role from admin WHERE mail=%s")
                s = (a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    print("Account Found!")
                    for i in result:
                        if i[1]=="parent":
                            print("You haven't permission!")
                        else:
                            edit_query = (
                                "DELETE FROM admin WHERE mail=%s")
                            edit = (a,)
                            mycursor.execute(edit_query, edit)
                            mydb.commit()
                            print("Account Delete Complete!")
                else:
                    print("No Account Found!")
            elif x == '2':
                a = input("Enter mail or id : ")
                query = ("SELECT mail from teacher WHERE mail=%s or id=%s")
                s = (a,a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    print("Account Found!")
                    edit_query = (
                        "DELETE FROM teacher WHERE mail=%s or id=%s")
                    edit = (a,a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Delete Complete!")
                else:
                    print("No Account Found!")
            elif x=='3':
                a = input("Enter mail or id : ")
                query = ("SELECT mail from student WHERE mail=%s or id=%s")
                s = (a, a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    print("Account Found!")
                    #Delete student account
                    edit_query = (
                        "DELETE FROM student WHERE mail=%s or id=%s")
                    edit = (a, a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    # Delete course
                    edit_query = (
                        "DELETE FROM course WHERE stdid=%s")
                    edit = ( a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Delete Complete!")
                else:
                    print("No Account Found!")
        elif in_put=='5':
            forget_password(log_in)
        elif in_put=='6':
            active_mail = ""
            active_id = ""
            log_in = False
            main_function()
def check_course_name(course_name,student_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    q_uery = "SELECT coursename FROM course where stdid=%s"
    data=(student_id,)
    count=0
    mycursor.execute(q_uery,data)
    c_re_sult = mycursor.fetchall()
    for i in c_re_sult:
        if i[0]==course_name:
            count+=1
            break
    return count
def check_course_code(course_code,student_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    mycursor = mydb.cursor()
    q_u = "SELECT coursecode FROM course WHERE stdid =%s"
    sp = (student_id,)
    mycursor.execute(q_u, sp)
    re_sult = mycursor.fetchall()
    count=0
    for i in re_sult:
        if i[0]==course_code:
            count+=1
            break
    return count
def forget_password(log_in_status):
    global login
    global active_mail
    global active_id
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="project2325",
        database="maindatabase",
    )
    print(log_in_status)
    mycursor = mydb.cursor()
    if log_in_status == True:
        p_s_q=input("1. Password \n2. Security Question : \n")
        if p_s_q=="1":
            mycursor.execute("SELECT id,password FROM student")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_id:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            pass_ = input("Enter previous password : ")
                            if pass_ == i[1]:
                                print("Correct !")
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE student SET password=%s WHERE id=%s")
                                        s = (password,active_id)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                print("Wrong Answer !")
                        else:
                            main_function()
            mycursor.execute("SELECT id,password FROM teacher")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_id:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            pass_ = input("Enter previous password : ")
                            if pass_ == i[1]:
                                print("Correct !")
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE teacher SET password=%s WHERE id=%s")
                                        s = (password, active_id,)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()

                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                print("Wrong Answer !")
                        else:
                            main_function()
            mycursor.execute("SELECT mail,password FROM admin")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_mail:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            pass_ = input("Enter previous password : ")
                            if pass_ == i[1]:
                                print("Correct !")
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE admin SET password=%s WHERE mail=%s")
                                        s = (password, active_mail,)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()

                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                print("Wrong Answer !")
                        else:
                            main_function()
        elif p_s_q=='2':
            mycursor.execute("SELECT id,que1,que2 FROM student")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_id :
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement=='1':
                            first_q = input("Primary School name ?")
                            if first_q == i[1]:
                                print("Correct !")
                                second_q = input("Favourite Teacher name ?")
                                if second_q == i[2]:
                                    print("Correct !")
                                    password = input("Enter Password (length (5-100)):  ")
                                    while True:
                                        if len(password) >= 5 and len(password) <= 100:
                                            query=("UPDATE student SET password=%s WHERE id=%s")
                                            s=(password,active_id,)
                                            mycursor.execute(query,s)
                                            mydb.commit()
                                            main_function()
                                        else:
                                            password = input("Wrong ! Enter Password (length (5-100)):  ")
                                else:
                                    print("Wrong Answer !")

                            else:
                                print("Wrong Answer !")
                        else:
                            main_function()
            mycursor.execute("SELECT id,que1,que2 FROM teacher")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_id:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            first_q = input("Primary School name ?")
                            if first_q == i[1]:
                                print("Correct !")
                                second_q = input("Favourite Teacher name ?")
                                if second_q == i[2]:
                                    print("Correct !")
                                    password = input("Enter Password (length (5-100)):  ")
                                    while True:
                                        if len(password) >= 5 and len(password) <= 100:
                                            query = ("UPDATE teacher SET password=%s WHERE id=%s")
                                            s = (password, active_id,)
                                            mycursor.execute(query, s)
                                            mydb.commit()
                                            main_function()
                                        else:
                                            password = input("Wrong ! Enter Password (length (5-100)):  ")
                                else:
                                    print("Wrong Answer !")

                            else:
                                print("Wrong Answer !")
                        else:
                            main_function()
            mycursor.execute("SELECT mail,que1,que2 FROM admin")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_mail:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            first_q = input("Primary School name ?")
                            if first_q == i[1]:
                                print("Correct !")
                                second_q = input("Favourite Teacher name ?")
                                if second_q == i[2]:
                                    print("Correct !")
                                    password = input("Enter Password (length (5-100)):  ")
                                    while True:
                                        if len(password) >= 5 and len(password) <= 100:
                                            query = ("UPDATE admin SET password=%s WHERE mail=%s")
                                            s = (password, active_mail,)
                                            mycursor.execute(query, s)
                                            mydb.commit()
                                            main_function()
                                        else:
                                            password = input("Wrong ! Enter Password (length (5-100)):  ")
                                else:
                                    print("Wrong Answer !")

                            else:
                                print("Wrong Answer !")
                        else:
                            main_function()
    elif log_in_status==False:
        f_mail=input("Enter Mail : ")
        mycursor.execute("SELECT mail,password,que1,que2 FROM student")
        result = mycursor.fetchall()
        for w in result:
            if w[0]==f_mail:
                print("Account Found !")
                p_s_q = input("1. Password \n2. Security Question : \n")
                if p_s_q == "1":
                    f_pass=input("Enter previous password : ")
                    if f_pass==w[1]:
                        while True:
                            print("Correct !")
                            statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                            if statement == '1':
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE student SET password=%s WHERE mail=%s")
                                        s = (password, f_mail)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                main_function()
                    else:
                        print("Wrong!")
                elif p_s_q == "2":
                    first_q = input("Primary School name ?")
                    if first_q == w[2]:
                        print("Correct !")
                        second_q = input("Favourite Teacher name ?")
                        if second_q == w[3]:
                            print("Correct !")
                            statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                            if statement == '1':
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE student SET password=%s WHERE mail=%s")
                                        s = (password, f_mail)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                main_function()
                        else:
                            print("Wrong!")
                    else:
                        print("Wrong!")
        mycursor.execute("SELECT mail,password,que1,que2 FROM teacher")
        result = mycursor.fetchall()
        for w in result:
            if w[0] == f_mail:
                print("Account Found !")
                p_s_q = input("1. Password \n2. Security Question : \n")
                if p_s_q == "1":
                    f_pass = input("Enter previous password : ")
                    if f_pass == w[1]:
                        while True:
                            print("Correct !")
                            statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                            if statement == '1':
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE teacher SET password=%s WHERE mail=%s")
                                        s = (password, f_mail)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                main_function()
                    else:
                        print("Wrong!")
                elif p_s_q == "2":
                    first_q = input("Primary School name ?")
                    if first_q == w[2]:
                        print("Correct !")
                        second_q = input("Favourite Teacher name ?")
                        if second_q == w[3]:
                            print("Correct !")
                            statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                            if statement == '1':
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE teacher SET password=%s WHERE mail=%s")
                                        s = (password, f_mail)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                main_function()
                        else:
                            print("Wrong!")
                    else:
                        print("Wrong!")
        mycursor.execute("SELECT mail,password,que1,que2 FROM admin")
        result = mycursor.fetchall()
        for w in result:
            if w[0] == f_mail:
                print("Account Found !")
                p_s_q = input("1. Password \n2. Security Question : \n")
                if p_s_q == "1":
                    f_pass = input("Enter previous password : ")
                    if f_pass == w[1]:
                        while True:
                            print("Correct !")
                            statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                            if statement == '1':
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE admin SET password=%s WHERE mail=%s")
                                        s = (password, f_mail,)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                main_function()
                    else:
                        print("Wrong!")
                elif p_s_q == "2":
                    first_q = input("Primary School name ?")
                    if first_q == w[2]:
                        print("Correct !")
                        second_q = input("Favourite Teacher name ?")
                        if second_q == w[3]:
                            print("Correct !")
                            statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                            if statement == '1':
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE admin SET password=%s WHERE mail=%s")
                                        s = (password, f_mail,)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        main_function()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                main_function()
                        else:
                            print("Wrong!")
                    else:
                        print("Wrong!")
main_function()