class OrderInfo1:
    def __init__(self, goods, count1):
        self.goods = goods
        self.count1 = count1
    def order_info1(self):
        if  goods == 1:
            c.execute("INSERT INTO orders VALUES(1, '스마트폰', ?)", (count1,),self.goods, self.count1)
        elif goods == 2:
            c.execute("INSERT INTO orders VALUES(2, '컴퓨터', ?)", (count1,),self.goods, self.count1)
        elif goods == 3:
            c.execute("INSERT INTO orders VALUES(3, '노트북', ?)", (count1,),self.goods, self.count1)
        elif goods == 4:
            c.execute("INSERT INTO orders VALUES(4, '파이썬 책', ?)", (count1,),self.goods, self.count1)
        elif goods == 5:
            c.execute("INSERT INTO orders VALUES(5, 'TV', ?)", (count1,),self.goods, self.count1)
        elif goods == 6:
            c.execute("INSERT INTO orders VALUES(6, '자전거', ?)", (count1,),self.goods, self.count1)
        elif goods == 7:
            c.execute("INSERT INTO orders VALUES(7, '헤드셋', ?)", (count1,),self.goods, self.count1)
        elif goods == 8:
            c.execute("INSERT INTO orders VALUES(8, '시계', ?)", (count1,),self.goods, self.count1)
        elif goods == 9:
            c.execute("INSERT INTO orders VALUES(9, '맥북', ?)", (count1,),self.goods, self.count1)
        elif goods == 10:
            c.execute("INSERT INTO orders VALUES(10, '마우스', ?)", (count1,),self.goods, self.count1)
        else:
            pass