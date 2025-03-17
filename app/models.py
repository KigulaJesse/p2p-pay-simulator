#app/models.py
from sqlalchemy import Column,Integer,String,Float,ForeignKey,create_engine
from sqlalchemy.orm import relationship,declarative_base,sessionmaker
from passlib.context import CryptContext

Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    "Users model"
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    balance = Column(Float, default=0.0)

    def __repr__(self):
        return f"<User(name={self.name}, balance={self.balance})>"

class Transaction(Base):
    "Transactions model"
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    description = Column(String)

    def __repr__(self):
        return f"<Transaction(amount={self.amount})>"

Base.metadata.create_all(engine)
