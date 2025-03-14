from app.models import User, Transaction, session

def send_money(sender_name, receiver_name, amount):
    sender = session.query(User).filter_by(name=sender_name).first()
    receiver = session.query(User).filter_by(name=receiver_name).first()

    if not sender or not receiver:
        return "User not found"
    if sender.balance < amount:
        return "Insufficient funds."
    
    sender.balance -= amount
    receiver.balance += amount
    transaction = Transaction(sender_id=sender.id, receiver_id=receiver.id, amount=amount, description="Transfer")
    session.add(transaction)
    session.commit()

    return f"Transfer successful: {sender_name} sent {amount} to {receiver_name}"