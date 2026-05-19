import sqlite3
import threading

from config import Config

thread_local = threading.local()

def get_db():
    if not hasattr(thread_local, "connection"):
        conn = sqlite3.connect(
            Config.DATABASE_PATH,
            check_same_thread=False
        )

        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL;")

        thread_local.connection = conn

    return thread_local.connection


def close_db():
    conn = getattr(thread_local, "connection", None)

    if conn:
        conn.close()
        del thread_local.connection
