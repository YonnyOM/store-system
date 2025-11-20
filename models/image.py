from config.database import *
class image_model():
    def insert_image(self,idProduct,route):
        run_query("INSERT INTO images (idProduct,route) VALUES (%s,%s)",(idProduct,route),False)
        return True
    def delete_image(self):
        pass
    def update_image(self,idProduct,route):
        run_query("UPDATE images SET route = %s WHERE idProduct = %s",(route,idProduct),False)
        return True
    def fetch_image(self):
        pass
    def fetch_image_all(self):
        pass