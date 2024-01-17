import sqlite3 
from datetime import*


'''
con = sqlite3.connect("storage.db")
cur = con.cursor()
cur.execute ("CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, user VARCHAR, mdp VARCHAR, date_cr DATE, res_pari INT)")
con.commit()
con.close()
'''

def inscri_donne (u : str,m : str, p = 0, d = datetime.today().strftime('%d-%m-%Y'), r = 0):
    '''u est l'identifient, m est le mdp, d est la date et p est sont nb de point/ argent on vera'''
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    a = cur.execute ("SELECT user FROM user WHERE user= ? ", (u,))
    a = a.fetchone()
    if a == None :
        val = (None, u, m, d, p, r)
        cur.execute ("INSERT INTO user VALUES(?,?,?,?,?,?)", val)
        con.commit()
        con.close()
        return True
    else :
        con.commit()
        con.close()
        return False


def connect (m : str, u : str):
    '''m est le mdp de l'utilisateur et u sont identifient
    en plus j'ai rajouté une id qui s'auto incrémente comme ça une fois l'utilisateur connecter ou pourra directement 
    récupérer ces info avec l'id que l'on aura stocke quelque part
    La fonction retourne : acces ou pas/ l'id de l'utilisateur / 1 si admin et 0 si utilisateur'''
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    val = (u,)
    a = cur.execute ("SELECT mdp FROM user WHERE user= ? ", val)
    a = a.fetchone()
    if a == None:
        return False
    else :
        if a[0] == m :
            b = cur.execute("SELECT id, admin FROM user WHERE user= ? AND mdp= ?", (u, m))
            b = b.fetchone()
            con.commit()
            con.close() 
            return True, b[0], b[1]

        else :
            con.commit()
            con.close()
            return False
    

def modife_donne (i : str,v : str,ch):
    '''modifie les donner choisie:
    i : id utilisateur
    v : nouvelle valeur
    ch : valeur à modifier '''
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    val = (i,v)
    if ch=="mdp":
        cur.execute ("UPDATE user SET mdp=? WHERE id= ?", val)
    elif ch=="mail":
        cur.execute ("UPDATE user SET user=? WHERE id= ?", val)
    elif ch=="pts":
        cur.execute ("UPDATE user SET res_pari=? WHERE id= ?", val)
    con.commit()
    con.close()

def suprime_donne(i:int):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    val = (i,)
    cur.execute ("DELETE FROM user WHERE id=?", val)
    con.commit()
    con.close()


'''
a = connect("admin", "Lucas")
print(a)
'''
con = sqlite3.connect("storage.db")
cur = con.cursor()


a = cur.execute("SELECT * FROM user")
a = a.fetchall()
print(a)
con.commit()
con.close()
