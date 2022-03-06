from datetime import date, datetime
import database as db
class Report:
    def __init__(self,invoice_id,chat_id) :
        self.invoice=invoice_id
        self.user=chat_id
    def validate(self):
        query=f"SELECT * FROM report WHERE invoice_id={self.invoice} AND chat_id={self.user}"
        db.prop.execute(query)
        result=db.prop.fetchall()
        if len(result) >0:
            return f"THERE ARE {len(result)} FOUND"
        else:
            return "invoice NOT FOUND"
    def status(self):
        query=f"SELECT * FROM report WHERE invoice_id={self.invoice} AND chat_id={self.user}"
        db.prop.execute(query)
        result=db.prop.fetchall() 
        return result['status']   
    def new (self,item,price,rep_status):
        date=datetime.now().strftime('%b-%Y-%d')
        query=f"INSERT INTO report chat_id,invoice_id,item,price,rep_date,rep_status VALUES ({self.user},{self.invoice},{item},{price},{rep_status},{date})"
        db.prop.execute(query)
        return "REPORT SENT ✅"
    def list (self):
        query=f"SELECT * FROM report WHERE  chat_id={self.user}"
        db.prop.execute(query)
        result=db.prop.fetchall()
        return result
