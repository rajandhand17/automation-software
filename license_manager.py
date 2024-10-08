import sqlite3
from datetime import datetime, timedelta

class LicenseManager:
    def __init__(self, db_file="database.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS licenses (
                    id INTEGER PRIMARY KEY,
                    license_key TEXT UNIQUE,
                    is_active INTEGER,
                    user_email TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS trials (
                    id INTEGER PRIMARY KEY,
                    user_email TEXT UNIQUE,
                    trial_start TIMESTAMP,
                    trial_end TIMESTAMP
                )
            """)

    def start_trial(self, email):
        trial_start = datetime.now()
        trial_end = trial_start + timedelta(days=10)
        with self.conn:
            self.conn.execute("""
                INSERT INTO trials (user_email, trial_start, trial_end)
                VALUES (?, ?, ?)
            """, (email, trial_start, trial_end))

    def check_trial(self, email):
        with self.conn:
            trial = self.conn.execute("""
                SELECT trial_end FROM trials WHERE user_email = ?
            """, (email,)).fetchone()
            if trial:
                trial_end = datetime.strptime(trial[0], '%Y-%m-%d %H:%M:%S')
                return datetime.now() < trial_end
            return False

    def activate_license(self, license_key, email):
        with self.conn:
            self.conn.execute("""
                UPDATE licenses SET is_active = 1, user_email = ? WHERE license_key = ?
            """, (email, license_key))

    def check_license(self, email):
        with self.conn:
            license = self.conn.execute("""
                SELECT is_active FROM licenses WHERE user_email = ?
            """, (email,)).fetchone()
            return license[0] if license else False
