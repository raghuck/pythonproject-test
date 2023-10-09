import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="online_medicines_store"
)

# Create a cursor object
cursor = db.cursor()

# Define the SQL query to insert the data into the database
sql = "INSERT INTO customers (full_name, mobile_no, age, address, prescription) VALUES (%s, %s, %s, %s, %s)"

# Get the form data from the request
full_name = request.form.get("full_name")
mobile_no = request.form.get("mobile_no")
age = request.form.get("age")
address = request.form.get("address")
prescription = request.files.get("prescription")

# Convert the prescription file to a binary object
prescription_file = prescription.read()

# Execute the SQL query to insert the data into the database
cursor.execute(sql, (full_name, mobile_no, age, address, prescription_file))

# Commit the changes to the database
db.commit()

# Close the cursor object
cursor.close()

# Close the database connection
db.close()

# Return a JSON response to the client
return jsonify({"success": True})
