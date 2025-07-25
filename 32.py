import sqlite3
import hashlib
import getpass
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    is_logged_in INTEGER NOT NULL DEFAULT 0
)
""")
conn.commit()
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists. Please choose a different username.")
        return

    password = getpass.getpass("Enter a password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    hashed_pw = hash_password(password)
    cursor.execute(
        "INSERT INTO users (username, password, is_logged_in) VALUES (?, ?, 0)",
        (username, hashed_pw)
    )
    conn.commit()
    print(f"User '{username}' registered successfully.")

def login():
    username = input("Enter your username: ").strip()
    password = getpass.getpass("Enter your password: ").strip()
    hashed_pw = hash_password(password)

    cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if not result:
        print("Username does not exist.")
        return

    stored_pw, is_logged_in = result
    if is_logged_in:
        print(f"User '{username}' is already logged in.")
        return

    if hashed_pw == stored_pw:
        cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
        conn.commit()
        print(f"User '{username}' logged in successfully.")
    else:
        print("Incorrect password.")

def logout():
    username = input("Enter your username: ").strip()
    cursor.execute("SELECT is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if not result:
        print("Username does not exist.")
        return

    is_logged_in = result[0]
    if not is_logged_in:
        print(f"User '{username}' is not logged in.")
        return

    cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
    conn.commit()
    print(f"User '{username}' logged out successfully.")

def change_password():
    username = input("Enter your username: ").strip()
    cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if not result:
        print("Username does not exist.")
        return

    stored_pw, is_logged_in = result
    if not is_logged_in:
        print(f"User '{username}' is not logged in. Please login first.")
        return

    current_password = getpass.getpass("Enter your current password: ").strip()
    if hash_password(current_password) != stored_pw:
        print("Current password is incorrect.")
        return

    new_password = getpass.getpass("Enter your new password: ").strip()
    if not new_password:
        print("New password cannot be empty.")
        return

    hashed_new_pw = hash_password(new_password)
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_new_pw, username))
    conn.commit()
    print(f"Password for user '{username}' changed successfully.")

def main():
    while True:
        print("\n=== User Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            logout()
        elif choice == '4':
            change_password()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    conn.close()
