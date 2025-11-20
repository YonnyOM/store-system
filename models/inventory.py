from config.database import *
class inventory_model():
    def insert_inventory(self,idProduct,purchase,sale,stock):
        run_query("INSERT INTO inventory (idProduct,purchase,sale,stock) VALUES (%s,%s,%s,%s)",(idProduct,purchase,sale,stock),False)
        return True
    def delete_inventory(self):
        pass
    def update_inventory(self,idProduct,purchase,sale,stock):
        run_query("UPDATE inventory SET purchase = %s, sale = %s, stock = %s WHERE idProduct = %s",(purchase,sale,stock,idProduct),False)
        return True
    def fetch_inventory(self,idProduct):
        data = run_query("SELECT * FROM inventory WHERE idProduct = %s",(idProduct,),True)
        return data
    def fetch_inventory_all(self):
        data = run_query("SELECT *FROM inventory",None,True)
        return data
    