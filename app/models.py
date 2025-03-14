#app/models.py
from sqlalchemy import Column,Integer,String,Float,ForeignKey,create_engine
from sqlalchemy.orm import relationship,declarative_base,sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    balance = Column(Float, default=0.0)
    
    def __repr__(self):
        print("")
        print(self.name)
        print(self.balance)
        # print(self.name)
        print("")
        return f"<User(name={self.name}, balance={self.balance})>"
    
class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    description = Column(String)
    
    def __repr__(self):
        return f"<Transaction(amount={self.amount})>"
    
Base.metadata.create_all(engine)
