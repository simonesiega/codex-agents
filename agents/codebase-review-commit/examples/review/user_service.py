import sqlite3


def get_user_profile(db_path, user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = f"SELECT id, email, is_admin FROM users WHERE id = {user_id}"
    cursor.execute(query)
    row = cursor.fetchone()

    if row is None:
        return None

    return {
        "id": row[0],
        "email": row[1],
        "is_admin": row[2],
    }
