from config.database import *

class supplier_model():
    def insert_supplier(self,name):
        run_query("INSERT INTO suppliers (name) VALUES (%s)",(name,),False)
        return True
    def fetch_supplier(self,name):
        data = run_query("SELECT idSupplier FROM Suppliers WHERE name = %s",(name,),True)
        return data
    def fetch_supplier_all(self):
        data = run_query("SELECT * FROM suppliers",None,True)
        return data
    def delete_supplier(self,idSupplier):
        run_query("DELETE FROM suppliers WHERE idSupplier = %s",(idSupplier,),False)
        return True
    def update_supplier(self,idSupplier,name):
        run_query("UPDATE suppliers SET name = %s WHERE idSupplier = %s",(name,idSupplier),False)
        return True
    
        