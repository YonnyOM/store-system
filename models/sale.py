from config.database import *

class sale_model():
    def insert_sale(self,idProduct,date,amount,idUser):
        run_query("INSERT INTO sales (idProduct,date,amount,idUser) VALUES(%s,%s,%s,%s)",(idProduct,date,amount,idUser),False)
        return True
    def delete_sale(self,idSale):
        run_query("DELETE FROM sales WHERE idSale = %s",(idSale,),False)
        return True
    def update_sale(self,idProduct,date,amount,idUser,idSale):
        date = run_query("UPDATE sales SET idProduct = %s,date = %s,amount = %s,idUser = %s WHERE idSale = %s",(idProduct,date,amount,idUser,idSale),False)
        return True
    def fetch_sale(self,idSale):
        data = run_query("SELECT *FROM sales WHERE idSale = %s",(idSale,),True)
        return data
    def fetch_sale_all(self,idSale):
        data = run_query("SELECT *FROM sales",None,True)
        return data