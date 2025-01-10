import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
from datetime import date, datetime
from decimal import Decimal

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "empdb"
}

def get_db_connection():
    """
    Creates and returns a new database connection.
    """
    return mysql.connector.connect(**DB_CONFIG)

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle non-serializable types."""
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()  # Convert to ISO 8601 string
        if isinstance(obj, Decimal):
            return float(obj)  # Convert Decimal to float
        return super().default(obj)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests to fetch employees."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            
            # Check if specific employee_id is requested
            if self.path.startswith("/employees/"):
                employee_id = self.path.split("/")[-1]
                cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
                result = cursor.fetchone()
                if not result:
                    self.send_error(404, "Employee not found.")
                    return
            else:
                cursor.execute("SELECT * FROM employees")
                result = cursor.fetchall()
            
            # Respond with the fetched data
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result, cls=CustomJSONEncoder).encode())
        except Exception as e:
            self.send_error(500, f"Internal server error: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    def do_POST(self):
        """Handle POST requests to add a new employee."""
        try:
            length = int(self.headers["Content-Length"])
            data = json.loads(self.rfile.read(length))

            conn = get_db_connection()
            cursor = conn.cursor()
            
            sql = """INSERT INTO employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                data["first_name"], data["last_name"], data["email"], data["phone_number"],
                data["hire_date"], data["job_id"], data["salary"], data.get("manager_id"), data["department_id"]
            ))
            conn.commit()

            self.send_response(201)
            self.end_headers()
            self.wfile.write(b"Employee added successfully.")
        except Exception as e:
            self.send_error(500, f"Internal server error: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    def do_PUT(self):
        """Handle PUT requests to update an employee."""
        try:
            if not self.path.startswith("/employees/"):
                self.send_error(400, "Invalid endpoint")
                return
            
            employee_id = self.path.split("/")[-1]
            length = int(self.headers["Content-Length"])
            data = json.loads(self.rfile.read(length))

            conn = get_db_connection()
            cursor = conn.cursor()
            
            sql = """UPDATE employees SET first_name = %s, last_name = %s, email = %s, phone_number = %s,
                     hire_date = %s, job_id = %s, salary = %s, manager_id = %s, department_id = %s
                     WHERE employee_id = %s"""
            cursor.execute(sql, (
                data["first_name"], data["last_name"], data["email"], data["phone_number"],
                data["hire_date"], data["job_id"], data["salary"], data.get("manager_id"), data["department_id"],
                employee_id
            ))
            conn.commit()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Employee updated successfully.")
        except Exception as e:
            self.send_error(500, f"Internal server error: {str(e)}")
        finally:
            cursor.close()
            conn.close()

def do_DELETE(self):
    """Handle DELETE requests to remove an employee."""
    try:
        if not self.path.startswith("/employees/"):
            self.send_error(400, "Invalid endpoint")
            return

        employee_id = self.path.split("/")[-1]

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check for dependent records
        cursor.execute("SELECT COUNT(*) FROM employees WHERE manager_id = %s", (employee_id,))
        dependent_count = cursor.fetchone()[0]

        if dependent_count > 0:
            self.send_error(400, f"Cannot delete employee {employee_id} because they are a manager of {dependent_count} employees.")
            return

        # Proceed to delete the employee
        sql = "DELETE FROM employees WHERE employee_id = %s"
        cursor.execute(sql, (employee_id,))
        conn.commit()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Employee deleted successfully.")
    except Exception as e:
        self.send_error(500, f"Internal server error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    """Run the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

"""
Testing with Postman
GET All Employees:
Method: GET
URL: http://localhost:8080/employees

GET Employee by ID:
Method: GET
URL: http://localhost:8080/employees/<employee_id>

POST (Add Employee):
Method: POST
URL: http://localhost:8080/employees
Body (JSON):
{
  "first_name": "Anirudha",
  "last_name": "Gaikwad",
  "email": "anirudha.gaikwad@example.com",
  "phone_number": "1234567890",
  "hire_date": "2020-01-01",
  "job_id": 1,
  "salary": 50000.00,
  "manager_id": null,
  "department_id": 1
}

PUT (Update Employee):
Method: PUT
URL: http://localhost:8080/employees/<employee_id>
Body (JSON): Same as above, with updated fields.

DELETE (Remove Employee):
Method: DELETE
URL: http://localhost:8080/employees/<employee_id>

"""