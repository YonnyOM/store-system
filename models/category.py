from config.database import *
class category_model():
    def insert_category(self,name):
        run_query("INSERT INTO category (name) VALUES (%s)",(name,),False)
        return True
    def delete_category(self,idCategory):
        run_query("DELETE FROM category WHERE idCategory = %s",(idCategory,),False)
        return True
    def update_category(self,idCategory,name):
        run_query ("UPDATE category SET name = %s WHERE idCategory = %s",(name,idCategory),False)
        return True
    def fetch_category (self,name):
        data = run_query ("SELECT idCategory FROM category WHERE name = %s",(name,),True)
        return data
    def fetch_category_all(self):
        data = run_query("SELECT * FROM category",None,True)
        return data
    