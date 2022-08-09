import sqlite3
 
def sql_commit(sql_command):
    conn=sqlite3.connect("moviedb.db")
    cur=conn.cursor()
    cur.execute(sql_command)
    conn.commit()
    conn.close()
 
def sql_fetch(sql_command):
    conn=sqlite3.connect("moviedb.db")
    cur=conn.cursor()
    cur.execute(sql_command)
    rows = cur.fetchall()
    conn.close()
    return rows
 
def connect():
    sql_com = "CREATE TABLE IF NOT EXISTS moviedb (id INTEGER PRIMARY KEY, title text, director text, genre text, year integer, rating integer)"
    sql_commit(sql_com)

def drop():
    sql_com = "DROP TABLE moviedb"
    sql_commit(sql_com)
 
def insert(title,director,genre,year,rating):
    sql_com = "INSERT INTO moviedb VALUES(NULL,'%s','%s','%s',%s,%s)"%(title,director,genre,year,rating)
    sql_commit(sql_com)
 
def view():
    sql_com = "SELECT * FROM moviedb"
    return sql_fetch(sql_com)
 
def search(title="",director="",genre="",year="",rating=""):
    sql_com = "SELECT * FROM moviedb WHERE title='%s' OR director='%s' or genre='%s' or year='%s' or rating='%s'"%(title,director,genre,year,rating)
    print(sql_com)
    return sql_fetch(sql_com)
 
def delete(id):
    sql_com = "DELETE FROM moviedb WHERE id=%s"%(id)
    sql_commit(sql_com)


def update(id,title,director,genre,year,rating):
    sql_com = "UPDATE moviedb SET title='%s', director='%s', genre='%s', year='%s', rating='%s' WHERE id='%s'"%(title,director,genre,year,rating, id)
    sql_commit(sql_com)

#drop()
connect()
# insert("Prey", "Dan Trachtenber", "Sci-fi/Action",2022, 5)
# print(view())
#print(search(director="Dan Trachtenber"))