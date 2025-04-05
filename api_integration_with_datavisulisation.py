from flask import Flask, request, jsonify
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('contact_book.db')
c = conn.cursor()

# Creating table
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (name text, phone_number text)''')
conn.commit()

# API endpoint to add contact
@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data['name']
    phone_number = data['phone_number']
    c.execute("INSERT INTO contacts VALUES (?,?)", (name, phone_number))
    conn.commit()
    return jsonify({'message': 'Contact added successfully'}), 200

# API endpoint to get all contacts
@app.route('/get_contacts', methods=['GET'])
def get_contacts():
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    return jsonify(contacts), 200

# API endpoint to update contact
@app.route('/update_contact', methods=['PUT'])
def update_contact():
    data = request.get_json()
    name = data['name']
    phone_number = data['phone_number']
    c.execute("UPDATE contacts SET phone_number=? WHERE name=?", (phone_number, name))
    conn.commit()
    return jsonify({'message': 'Contact updated successfully'}), 200

# API endpoint to delete contact
@app.route('/delete_contact', methods=['DELETE'])
def delete_contact():
    data = request.get_json()
    name = data['name']
    c.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()
    return jsonify({'message': 'Contact deleted successfully'}), 200

# Data visualization:
def visualize_contacts():
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    names = [contact[0] for contact in contacts]
    phone_numbers = [contact[1] for contact in contacts]
    plt.figure(figsize=(10, 5))
    sns.barplot(x=names, y=phone_numbers)
    plt.title('Contacts')
    plt.xlabel('Name')
    plt.ylabel('Phone Number')
    plt.show()

if __name__ == '__main__':
    app.run(debug=True)
