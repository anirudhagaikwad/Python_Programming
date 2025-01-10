import json
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import date, datetime
from decimal import Decimal

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "empdb",
}

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()  # Convert to ISO 8601 string
        if isinstance(obj, Decimal):
            return float(obj)  # Convert Decimal to float
        return super().default(obj)

def connect_to_database():
    """Establish a connection to the MySQL database."""
    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
    )

class EmployeeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests to fetch employee(s)."""
        try:
            # Extract the employee ID from the URL if provided
            employee_id = self.path.split("/")[-1] if self.path != "/" else None

            # Connect to the database
            connection = connect_to_database()
            cursor = connection.cursor(dictionary=True)  # Return results as a dictionary

            if employee_id and employee_id.isdigit():
                # Fetch specific employee by ID
                query = "SELECT * FROM employees WHERE id = %s"
                cursor.execute(query, (employee_id,))
                result = cursor.fetchone()
                if not result:
                    self.send_error(404, "Employee not found.")
                    return
            else:
                # Fetch all employees
                query = "SELECT * FROM employees"
                cursor.execute(query)
                result = cursor.fetchall()

            # Serialize the result to JSON
            response_body = json.dumps(result,cls=CustomJSONEncoder) 
            # response_body = json.dumps(result)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response_body.encode())

        except Exception as e:
            self.send_error(500, f"Internal server error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def do_POST(self):
        """Handle POST requests to add a new employee."""
        try:
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length).decode()
            data = json.loads(body)

            # Validate input
            required_fields = ["name", "designation", "salary"]
            if not all(field in data for field in required_fields):
                self.send_error(400, "Missing required fields.")
                return

            # Insert the new employee
            connection = connect_to_database()
            cursor = connection.cursor()
            query = "INSERT INTO employees (name, designation, salary) VALUES (%s, %s, %s)"
            cursor.execute(query, (data["name"], data["designation"], data["salary"]))
            connection.commit()

            # Send response
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Employee added successfully."}).encode())

        except Exception as e:
            self.send_error(500, f"Internal server error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def do_PUT(self):
        """Handle PUT requests to update an existing employee."""
        try:
            # Extract employee ID
            employee_id = self.path.split("/")[-1]
            if not employee_id.isdigit():
                self.send_error(400, "Invalid employee ID.")
                return

            # Read request body
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length).decode()
            data = json.loads(body)

            # Validate input
            allowed_fields = ["name", "designation", "salary"]
            update_fields = {k: v for k, v in data.items() if k in allowed_fields}
            if not update_fields:
                self.send_error(400, "No valid fields to update.")
                return

            # Update employee
            connection = connect_to_database()
            cursor = connection.cursor()
            set_clause = ", ".join(f"{key} = %s" for key in update_fields.keys())
            query = f"UPDATE employees SET {set_clause} WHERE id = %s"
            cursor.execute(query, (*update_fields.values(), employee_id))
            connection.commit()

            if cursor.rowcount == 0:
                self.send_error(404, "Employee not found.")
                return

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Employee updated successfully."}).encode())

        except Exception as e:
            self.send_error(500, f"Internal server error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def do_DELETE(self):
        """Handle DELETE requests to remove an employee."""
        try:
            # Extract employee ID
            employee_id = self.path.split("/")[-1]
            if not employee_id.isdigit():
                self.send_error(400, "Invalid employee ID.")
                return

            # Delete employee
            connection = connect_to_database()
            cursor = connection.cursor()
            query = "DELETE FROM employees WHERE id = %s"
            cursor.execute(query, (employee_id,))
            connection.commit()

            if cursor.rowcount == 0:
                self.send_error(404, "Employee not found.")
                return

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Employee deleted successfully."}).encode())

        except Exception as e:
            self.send_error(500, f"Internal server error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

def run(server_class=HTTPServer, handler_class=EmployeeHandler, port=8088):
    """Run the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()


"""

### Instructions to Test Using Postman:

1. GET All Employees:
   - Method: `GET`
   - URL: `http://localhost:8088/`

2. GET Employee by ID:
   - Method: `GET`
   - URL: `http://localhost:8088/{id}`

3. POST Add Employee:
   - Method: `POST`
   - URL: `http://localhost:8088/`
   - Body (JSON):
     
     {
         "name": "Alice",
         "designation": "HR Manager",
         "salary": 60000
     }
     

4. PUT Update Employee:
   - Method: `PUT`
   - URL: `http://localhost:8088/{id}`
   - Body (JSON):
     
     {
         "name": "Alice Smith",
         "salary": 65000
     }
     

5. DELETE Remove Employee:
   - Method: `DELETE`
   - URL: `http://localhost:8088/{id}`

"""


