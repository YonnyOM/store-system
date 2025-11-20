from config.database import *
class user_model():
    def insert_user(self,name,password,position,state):
        run_query("insert INTO users (name,password,position,satate) VALUES (%s,%s,%s,%s)",(name,password,position,state,False))
        return True
    def delete_user(self,idUser):
        run_query("DELETE FROM users WHERE idUser = %s",(idUser,),False)
        return True
    def update_user(self,idUser,name,password,position,state):
        run_query("UPDATE  users SET name=%s, password =%s ,position =%s,state =%s WHERE idUser = %s",(name,password,position,state,idUser),False)
        return True
    def fetch_user (self,idUser):
        data = run_query("SELECT * FROM users WHERE idUser = %s",(idUser,),True)
        return data
    def fetch_user_all(self,idUser):
        data = run_query("SELECT *FROM users",None,True)
        return data