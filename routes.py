from flask import request, jsonify
from app import app
import sqlite3


@app.route('/submit_bug', methods=['POST'])
def submit_bug():
    bug_description = request.form.get('bug-description')

    conn = sqlite3.connect('bug_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bugs (description) VALUES (?)',
                   (bug_description,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Bug submitted successfully!"})


if __name__ == '__main__':
    app.run(debug=True)
