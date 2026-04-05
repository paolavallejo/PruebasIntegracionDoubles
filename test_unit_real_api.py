from order_service import create_order
from database import SessionLocal, Base, engine
from user_repository import JsonPlaceholderUserRepository

Base.metadata.create_all(bind=engine)

class DummyLogger:
    def log(self, msg):
        # TODO: implementar un logger que no haga nada
        __________

class NullNotifier:
    def send(self, to, message):
        # TODO: implementar un notifier que no haga nada
        __________

def test_create_order_with_real_api():
    db = SessionLocal()

    order = create_order(
        user_id=1,
        amount=100,
        notifier=NullNotifier(),
        logger=DummyLogger(),
        db=db,
        user_repository=JsonPlaceholderUserRepository()
    )

    # TODO: completar el estado esperado
    assert order.status == "________"

    db.close()