from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.orm import  relationship
from SaleApp.saleapp import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

class Category (BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    products = relationship('Product', backref ='category', lazy =True) #backref ='category', thì tự động trong đối tượng
    # của product sẽ thêm 1 category và thuộc tính này đại diện cho đối tượng category mà sản phẩm nó đang trực thuộc vào
    def __str__(self):
        return self.name




class Product (BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default = 0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default = datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    def __str__(self):
        return self.name

if __name__ == '__main__':
    db.create_all()
