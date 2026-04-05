# app.py
from flask import Flask, render_template, request
from database import Base, engine, SessionLocal
from order_service import create_order
from models import Order
from user_repository import JsonPlaceholderUserRepository
#from user_repository import FakeUserRepository

app = Flask(__name__)
Base.metadata.create_all(bind=engine)

class WebNotifier:
    def send(self, to, message):
        print(f"[EMAIL] {to}: {message}")

class WebLogger:
    def log(self, msg):
        print(f"[LOG] {msg}")

@app.route("/", methods=["GET", "POST"])
def index():
    db = SessionLocal()
    repo = JsonPlaceholderUserRepository()
    #repo = FakeUserRepository()
    result = None
    error = None

    if request.method == "POST":
        try:
            result = create_order(
                user_id=int(request.form["user_id"]),
                amount=int(request.form["amount"]),
                notifier=WebNotifier(),
                logger=WebLogger(),
                db=db,
                user_repository=repo
            )
        except Exception as e:
            error = str(e)

    orders = db.query(Order).all()
    db.close()

    return render_template(
        "index.html",
        result=result,
        orders=orders,
        error=error
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)