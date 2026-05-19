from werkzeug.security import generate_password_hash
from database import get_db

def init_database():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT,
        is_active INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS role_permissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role_name TEXT,
        module TEXT,
        can_view INTEGER DEFAULT 0,
        can_create INTEGER DEFAULT 0,
        can_edit INTEGER DEFAULT 0,
        can_delete INTEGER DEFAULT 0,
        can_assign INTEGER DEFAULT 0
    )
    """)

    admin_password = generate_password_hash("admin123")

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (id, name, email, password_hash, role)
    VALUES
    (1, 'Super Admin', 'admin@example.com', ?, 'SuperAdmin')
    """, (admin_password,))

    conn.commit()

    print("Database initialized successfully")


if __name__ == "__main__":
    init_database()
