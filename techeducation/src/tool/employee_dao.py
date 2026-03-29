import mysql.connector
class EmployeeDAO:
    def __init__(self):
        pass

    def get_employee_salary(self, name):

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="onlineedu"
        )

        cursor = conn.cursor()

        query = "SELECT salary FROM employees WHERE name = %s"

        cursor.execute(query, (name,))

        result = cursor.fetchone()

        conn.close()

        if result:
            return f"{name}'s salary is {result[0]}"
        else:
            return "Employee not found"
    
    def execute_query(self, query):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="onlineedu"
            )

        cursor = conn.cursor()

        cursor.execute(query)

        results = cursor.fetchall()

        conn.close()

        return str(results)