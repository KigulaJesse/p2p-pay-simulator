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
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    balance = Column(Float, default=0.0)

    def verify_password(self, password:str) -> str:
        """Verify a plain text password against the stored hash."""
        return pwd_context.verify(password, self.hashed_password)
    
    def hash_password(cls, password: str) -> str:
        """Hash a password before storing it."""
        return pwd_context.hash(password)
    
    def __repr__(self):
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
