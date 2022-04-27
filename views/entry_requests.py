import sqlite3
import json
from models import Entry
  
def get_all_entries():
    """Gets all entries"""
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id 
        FROM entries e
        """)

        # Initialize an empty list to hold all entries representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            entry = Entry(row['id'], row['concept'], row['entry'],
                            row['date'], row['mood_id'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)

# def get_single_entry(id):
#     """Gets single entry"""
    
#     with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()
        
#         db_cursor.execute("""
#         SELECT
#             e.id,
#             e.concept,
#             e.entry,
#             e.date,
#             e.mood_id
#         FROM entries e
#         WHERE e.id = ?
#         """, ( id, ))
        
#         data = db_cursor.fetchone()
        
#         entry = Entry(data['id'], data['concept'], data['entry'], 
#                         data['e.date'], data ['mood_id'])
        
#         return json.dumps(entry.__dict__)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        entry = Entry(data['id'], data['concept'], data['entry'],
                            data['date'], data['mood_id'])

        return json.dumps(entry.__dict__)
    
def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))
        
def search_entries(value):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM Entries e
        WHERE e.entry LIKE ?
        """, (f"%{value}%", ))

        # Initialize an empty list to hold all entries representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            entry = Entry(row['id'], row['concept'], row['entry'],
                            row['date'], row['mood_id'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)