# coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, Date, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:1234@localhost:3306/baobab?charset=utf8", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


session = Session()


# 货物详情
class StockDetail(Base):
    __tablename__ = 'stock_detail'
    # 操作id
    id = Column(Integer, primary_key=True)
    # 组图地址
    combo_pic_address = Column(String(500))
    # 图片地址
    pic_address = Column(String(500))
    # 商品编号
    stock_number = Column(String(500))
    # 商品名称
    name = Column(String(500))
    # 材质
    texture = Column(String(500))
    # 尺寸
    size = Column(String(500))
    # 单位
    unit = Column(String(500))
    # 备注
    remark = Column(String(500))
    # 原价
    orin_price = Column(String(500))
    # 单价
    price = Column(Integer)


# 订单详情
class OrderDetail(Base):
    __tablename__ = 'order_detail'
    # 订单详情id
    id = Column(Integer, primary_key=True)
    # 订单id
    order_id = Column(Integer, index=True)
    # 货物id
    stock_id = Column(Integer, index=True)
    # 数量
    count = Column(Integer)
    # 总价格
    total_price = Column(Integer)


# 订单
class Order(Base):
    __tablename__ = 'order'
    # 订单id
    id = Column(Integer, primary_key=True)
    # 联系人id
    contact_id = Column(Integer,index=True)
    # 项目名称
    project_name = Column(String(500))
    # 总价格
    total_price = Column(Integer)
    # 实际价格
    actual_price = Column(Integer)
    # 是否发货
    has_deliveried = Column(SmallInteger)
    # 是否开发票
    is_need_invoice = Column(SmallInteger)
    # 是否已经开发票
    has_made_invoice = Column(SmallInteger)
    # 是否付款
    is_paid = Column(SmallInteger)
    # 已付款
    paid_num = Column(Integer)
    # 订单建立日期
    start_time = Column(DateTime)
    # 订单结算日期
    end_time = Column(DateTime)


# 联系人
class Contact(Base):
    __tablename__ = 'contact'
    # 联系人id
    id = Column(Integer, primary_key=True)
    # 联系人名称
    name = Column(String(500))
    # 联系方式
    phone_number = Column(String(500))
    # 公司
    company = Column(String(500))


# 操作记录
class OperationLog(Base):
    __tablename__ = 'operation_log'
    # 操作id
    id = Column(Integer, primary_key=True)
    # 操作内容
    content = Column(String(500))
    # 操作时间
    operate_time = Column(DateTime)

def init_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
    session.add(StockDetail(pic_address=r"d:\web", name="陶瓷艺术", texture="牛皮", price=5))
    session.commit()
