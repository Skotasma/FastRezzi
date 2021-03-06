from fastapi import FastAPI
#uvicorn main:app --reload
app = FastAPI()
import sqlite3
con = sqlite3.connect('DB/SQLite1.db')

@app.get("/")
async def root():
    cur = con.cursor()
    t = ('Schnitzel',)
   # cur.execute('SELECT * FROM Rezepte WHERE Titel=?', t)
    cur.execute('SELECT * FROM Rezepte')
    return {"message": cur.fetchall()}