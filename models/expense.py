from config.database import *
class expense_model():
    def insert_expense(self,idProduct,date,bill,amount,idUser):
        run_query ("INSERT INTO expense (idProduct,date,bill,amount,idUser) VALUES(%s,%s,%s,%s)",(idProduct,date,bill,amount,idUser),False)
        return True
    def delete_expense(self,idExpense):
        run_query("DELETE FROM expense WHERE idExpense = %s",(idExpense,),False)
        return True
    def update_expense(self,idExpense,idProduct,date,bill,amount,idUser):
        run_query ("UPDATE expense SET idProduct = %s,date = %s,bill = %s,amount = %s,idUser =%s WHERE idExpense = %s ",(idProduct,date,bill,amount,idUser,idExpense),False)
        return True
    def fetch_expense(self,idExpense):
        data = run_query("SELECT * FROM expense WHERE idExpense = %s",(idExpense),True)
        return data
    def fetch_expense_all(self):
        data = run_query("SELECT * FROM expense",None,True)
        return data
    