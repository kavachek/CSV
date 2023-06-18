import sqlite3 as sql

conn = sql.connect("database.db")


def set_sqlite_pragma(conn):
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    print("PRAGMA foreign_keys=ON")
    conn.commit()
    return True


def create_t_students(conn):
    cursor = conn.cursor()
    sql_create_table_query = '''CREATE TABLE students (
                                id_student INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL);'''
    cursor.execute(sql_create_table_query)
    print("Таблица students создана")
    conn.commit()
    return True


def create_t_documents(conn):
    cursor = conn.cursor()
    sql_create_table_query = '''CREATE TABLE documents (
                                id_student INTEGER PRIMARY KEY,
                                number INTEGER DEFAULT NULL,
                                series INTEGER DEFAULT NULL,
                                FOREIGN KEY (id_student) REFERENCES students(id_student)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE);'''
    cursor.execute(sql_create_table_query)
    print("Таблица documents создана")
    conn.commit()
    return True


def create_t_users(conn):
    cursor = conn.cursor()
    sql_create_table_query = '''CREATE TABLE users (
                                id_user INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email TEXT NOT NULL,
                                avatar_path TEXT);'''
    cursor.execute(sql_create_table_query)
    print("Таблица users создана")
    conn.commit()
    return True


def create_t_sections(conn):
    cursor = conn.cursor()
    sql_create_table_query = '''CREATE TABLE sections (
                                id_section INTEGER PRIMARY KEY,
                                section_name TEXT NOT NULL,
                                date DATE,
                                id_moderator INTEGER,
                                FOREIGN KEY (id_moderator) REFERENCES users(id_user)
                                    ON DELETE SET NULL
                                    ON UPDATE CASCADE);'''
    cursor.execute(sql_create_table_query)
    print("Таблица sections создана")
    conn.commit()
    return True


def create_t_posts(conn):
    cursor = conn.cursor()
    sql_create_table_query = '''CREATE TABLE posts (
                                id_post INTEGER PRIMARY KEY,
                                id_section INTEGER,
                                id_author INTEGER,
                                post_name TEXT NOT NULL,
                                text TEXT NOT NULL,
                                date DATE,
                                FOREIGN KEY (id_section) REFERENCES sections(id_section)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE,
                                FOREIGN KEY (id_author) REFERENCES users(id_user)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE);'''
    cursor.execute(sql_create_table_query)
    print("Таблица posts создана")
    conn.commit()
    return True


def create_t_messages(conn):
    cursor = conn.cursor()
    sql_create_table_query = '''CREATE TABLE messages (
                                id_message INTEGER PRIMARY KEY,
                                id_post INTEGER,
                                id_user_sender INTEGER,
                                id_user_recipient INTEGER,
                                text TEXT NOT NULL,
                                date DATE,
                                FOREIGN KEY (id_post) REFERENCES posts(id_post)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE,
                                FOREIGN KEY (id_user_sender) REFERENCES users(id_user)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE,
                                FOREIGN KEY (id_user_recipient) REFERENCES users(id_user)
                                    ON DELETE SET NULL
                                    ON UPDATE CASCADE);'''
    cursor.execute(sql_create_table_query)
    print("Таблица messages создана")
    conn.commit()
    return True


# set_sqlite_pragma(conn)
# create_t_students(conn)
# create_t_documents(conn)
# create_t_users(conn)
# create_t_sections(conn)
# create_t_posts(conn)
# create_t_messages(conn)
