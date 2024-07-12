import mysql.connector


def get_data():
    mydb = mysql.connector.connect(host = "localhost", user="root", password="root",database="testdb")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchall()
    mydb.close()
    return result