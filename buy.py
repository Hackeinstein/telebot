from transact import Transact as tx
import database as db
class Cc:
    def __init__(self,chat_id):
        self.user=chat_id
        self.price=""
        self.tx=""
    def query (self,bin):
        self.query=f"SELECT * FROM cc WHERE cc_bin={bin}"
        db.prop.execute(self.query)
        self.result=db.prop.fetchall()
        if len(self.result) >0:
            self.price=self.result
            return  f"THERE ARE {len(self.result)} CC's"
        else:
            return f"CC's WITH {bin} NOT FOUND"
    def price (self):
        return self.result
    def dist(self,no):
        for x in range(no):
            return self.product[3]


new_cc=Cc(12345)
new_cc.query(601100)
print(new_cc.price())
