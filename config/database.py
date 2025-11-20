#connection databese
import mysql.connector

def getConnection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="luna"  # cámbialo por el nombre de tu base
        ) 
    except Exception as e:
        print("Error:", e)
        return None

def run_query(query, params=None, fetch=False): 
    cnn = getConnection()
    cursor = cnn.cursor()
    cursor.execute(query, params) if params else cursor.execute(query)
    data = cursor.fetchall() if fetch else None
    cnn.commit()
    cursor.close()
    cnn.close()
    return data


