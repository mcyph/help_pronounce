import sqlite3
import json

conn = sqlite3.connect('wiktionary.db')
c = conn.cursor()
c.execute('CREATE TABLE wiktionary (k TEXT PRIMARY KEY, v TEXT);')

D = json.loads(open('wiktionary.json', 'rb').read().decode('utf-8'))

for k, i_D in D.items():
    c.execute(
        'INSERT INTO wiktionary VALUES (?,?)',
        [k, json.dumps(i_D, ensure_ascii=False)]
    )

conn.commit()
