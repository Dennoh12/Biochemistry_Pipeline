import sqlite3

def create_table():
    conn = sqlite3.connect('biochemistry_db.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hhsearch_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_id TEXT,
            best_hit TEXT,
            best_evalue TEXT,
            best_score TEXT,
            score_mean TEXT,
            score_std TEXT,
            score_gmean TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
