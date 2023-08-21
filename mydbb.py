import pymysql

emp_name =" mike white"
hire_date ="2022-2-11"
salary = 580000
dept_id = 32

# post
def mydbpost():
    connection =pymysql.connect(host='localhost', user='root', password='',
                                                database='simba')
                            
    sql = "insert into employees(emp_name, hire_date, salary, dept_id) values(%s, %s, %s, %s)"
        

    cursor = connection.cursor()

    cursor.execute(sql, (emp_name, hire_date, salary, dept_id))

    connection.commit()


#get
def mydbview():

    connection =pymysql.connect(host='localhost', user='root', password='',
                                                database='simba')
                            
    sql = "select * from employees where emp_id = 1"
        

    cursor = connection.cursor()

    cursor.execute(sql)

    output = cursor.fetchall()
    print(output)

    connection.commit()

#update
def mydbupdate():
    
    connection =pymysql.connect(host='localhost', user='root', password='',
                                                database='simba')
                            
    sql = "UPDATE Employees SET salary = 230000 WHERE emp_name = 'Ken Mumba'"
        

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()

# delete
def mydbdelete():
    
    connection =pymysql.connect(host='localhost', user='root', password='',
                                                database='simba')
                            
    sql = "DELETE FROM Employees WHERE emp_name = 'Tom Mboya'"
        

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()

if __name__ == "__main__" :
    mydbdelete()