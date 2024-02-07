class item:
    discount =0.08
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def total_price(self):
        return self.price*self.quantity
    def final_price(self):
        self.price=self.price*item.discount
    
shoe=item("nike",2000,6)

cloth=item("Versache",3452,32)
shoe.final_price()
print("the",shoe.name,"is",shoe.price,"remaining",shoe.quantity,"pieces","total price is:",shoe.total_price())


   
    
