# test_unit_with_stub.py

from order_service import create_order
from database import SessionLocal
from models import Order

# ---- Test Double: STUB ----
class StubUserRepository:
    def get_user_email(self, user_id):
        return "stub@test.com"


# ---- Doubles auxiliares ----
class DummyLogger:
    def log(self, msg):
        pass


class NullNotifier:
    def send(self, to, message):
        pass


def test_create_order_with_stub_user_repository():
    """
    Test unitario REAL:
    - No usa red
    - No usa API externa
    - No depende del mundo
    """

    db = SessionLocal()

    order = create_order(
        user_id=123,
        amount=200,
        notifier=NullNotifier(),
        logger=DummyLogger(),
        db=db,
        user_repository=StubUserRepository()  # AQUÍ se usa el Stub
    )

    assert order.status == "CREATED"
    assert order.user_email == "stub@test.com"

    db.query(Order).delete()
    db.commit()
    db.close()
