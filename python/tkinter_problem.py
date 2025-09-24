import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import csv
from tkinter import filedialog

# pip install mysql-connector-python

"""
import mysql.connector
from mysql.connector import Error
# ...existing code...

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',         # default XAMPP/WAMP user
        password='',         # default is empty for XAMPP/WAMP
        database='admin'     # make sure this DB exists in phpMyAdmin
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            phone VARCHAR(20)
        )
    ''')
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)
# ...existing code...
"""

conn = sqlite3.connect('admin.db')
cursor = conn.cursor()  #  its for allow to execute the query
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        phone TEXT
    )
''')

root = tk.Tk()
root.title("Login/Register Example")
root.geometry("450x500")
root.configure(bg="#CF1E1E")

def clear_window():
    for i in root.winfo_children():  #it is used for remove the old condent and come new content in the same window
        i.destroy()

def show_login():
    clear_window()
    frame = tk.Frame(root, bg="#555c62", bd=5, relief="sunken")  # bd was frame border width relief was related to bd it is the select the style of border
    frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=250)  #relx,rely was used for padding of r , l, t, b
    
    tk.Label(frame, text="Login", font=("Arial", 18, "bold"), bg="#e3eaf2", fg="#2c3e50").pack(pady=10)
    tk.Label(frame, text="Username", bg="#e3eaf2", fg="#2c3e50").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=2)

    tk.Label(frame, text="Password", bg="#e3eaf2", fg="#2c3e50").pack()
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=2)

    def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "admin123":
            show_admin_dashboard()
        
        elif  cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)):
            user = cursor.fetchone()
            if user:
                show_dashboard(user)
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    tk.Button(frame, text="Login", bg="#2980b9", font=("Arial", 10, "bold"), command=handle_login).pack(pady=10)
    tk.Button(frame, text="Go to Register", command=show_register, bg="#bdc3c7").pack()

def show_register():
    clear_window()
    frame = tk.Frame(root, bg="#e3eaf2", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=370)
    
    tk.Label(frame, text="Register", font=("Arial", 18, "bold"), bg="#e3eaf2", fg="#16a085").pack(pady=10)

    tk.Label(frame, text="Username", bg="#e3eaf2", fg="#2c3e50").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=2)

    tk.Label(frame, text="Password", bg="#e3eaf2", fg="#2c3e50").pack()
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=2)

    tk.Label(frame, text="Email", bg="#e3eaf2", fg="#2c3e50").pack()
    email_entry = tk.Entry(frame)
    email_entry.pack(pady=2)

    tk.Label(frame, text="Phone", bg="#e3eaf2", fg="#2c3e50").pack()
    phone_entry = tk.Entry(frame)
    phone_entry.pack(pady=2)

    def handle_register():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        if not username or not password or not email or not phone:
            messagebox.showerror("Error", "All fields are required.")
        elif username == "admin":
            messagebox.showerror("Error", "Cannot register with reserved username 'admin'.")
        else:
            try:
                cursor.execute(
                    "INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)",
                    (username, password, email, phone)
                )
                conn.commit()
                messagebox.showinfo("Success", "Registration successful!")
                show_login()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists.")

    tk.Button(frame, text="Register", bg="#27ae60", font=("Arial", 10, "bold"), command=handle_register).pack(pady=10)
    tk.Button(frame, text="Go to Login", command=show_login, bg="#bdc3c7").pack()

def show_dashboard(user):
    clear_window()
    frame = tk.Frame(root, bg="#e3eaf2", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=250)

    user_id, username, _, email, phone = user # here use _ for avoiding password feild 

    tk.Label(frame, text=f"Welcome, {username}!", font=("Arial", 16, "bold"), bg="#e3eaf2", fg="#8e44ad").pack(pady=10)
    tk.Label(frame, text=f"Email: {email}", bg="#e3eaf2", fg="#2c3e50", font=("Arial", 12)).pack(pady=2)
    tk.Label(frame, text=f"Phone: {phone}", bg="#e3eaf2", fg="#2c3e50", font=("Arial", 12)).pack(pady=2)
    
    tk.Button(frame, text="Logout", command=show_login, bg="#c0392b").pack(pady=20)

def show_admin_dashboard():
    clear_window()
    frame = tk.Frame(root, bg="#e3eaf2", bd=2, relief="groove")
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    tk.Label(frame, text="Admin Dashboard", font=("Arial", 18, "bold"), bg="#e3eaf2", fg="#c0392b").pack(pady=10)
    
    tree = ttk.Treeview(frame, columns=("ID", "Username", "Email", "Phone"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Username", text="Username")
    tree.heading("Email", text="Email")
    tree.heading("Phone", text="Phone")
    tree.column("ID", width=50)
    tree.column("Username", width=100)
    tree.column("Email", width=150,anchor='center')
    tree.column("Phone", width=100)
    tree.pack(pady=10, padx=10, fill="both", expand=True)

    cursor.execute("SELECT id, username, email, phone FROM users")
    users = cursor.fetchall()
    for user in users:
        tree.insert("", "end", values=user)

    btn_frame = tk.Frame(frame, bg="#e3eaf2")
    btn_frame.pack(pady=10)

    def view_user_details():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a user first.")
        else:
            user_data = tree.item(selected_item)['values']
            user_id = user_data[0]
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            user = cursor.fetchone()
            show_user_details(user)

    def delete_user():
        selected_item = tree.focus()
        user_data = tree.item(selected_item)['values']

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a user first.")
            return
        elif user_data[1] == "admin":
            messagebox.showerror("Error", "Cannot delete admin account.")   
            return   
        else:
            if messagebox.askyesno("Confirm", f"Are you sure you want to delete user {user_data[1]}?"):

                cursor.execute("DELETE FROM users WHERE id=?", (user_data[0],))
                conn.commit()
                tree.delete(selected_item)
                messagebox.showinfo("Success", "User deleted successfully.")

    def export_to_csv():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save user data as",
            initialfile="users"
        )
        if file_path:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Username", "Password", "Email", "Phone"])
                writer.writerows(users)
            messagebox.showinfo("Success", f"User data exported to {file_path}")

    tk.Button(btn_frame, text="View Details", command=view_user_details, bg="#3498db").grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Delete User", command=delete_user, bg="#e74c3c").grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Export to CSV", command=export_to_csv, bg="#2ecc71").grid(row=0, column=2, padx=5)
    tk.Button(frame, text="Logout", command=show_login, bg="#c0392b").pack(pady=10)

def show_user_details(user):
    top = tk.Toplevel(root)
    top.title("User Details")
    top.geometry("300x250")
    top.configure(bg="#e3eaf2")

    user_id, username, _, email, phone = user

    tk.Label(top, text="User Details", font=("Arial", 16, "bold"), bg="#e3eaf2", fg="#16a085").pack(pady=10)
    tk.Label(top, text=f"ID: {user_id}", bg="#e3eaf2", fg="#2c3e50", font=("Arial", 12)).pack(pady=2)
    tk.Label(top, text=f"Username: {username}", bg="#e3eaf2", fg="#2c3e50", font=("Arial", 12)).pack(pady=2)
    tk.Label(top, text=f"Email: {email}", bg="#e3eaf2", fg="#2c3e50", font=("Arial", 12)).pack(pady=2)
    tk.Label(top, text=f"Phone: {phone}", bg="#e3eaf2", fg="#2c3e50", font=("Arial", 12)).pack(pady=2)

    tk.Button(top, text="Close", command=top.destroy, bg="#c0392b").pack(pady=10)

if __name__ == "__main__":
    show_login()
    root.mainloop()
    conn.close()