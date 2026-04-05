# test_integration_with_fake.py

from order_service import create_order
from database import SessionLocal
from models import Order

# ---- Fake usado también en la APP ----
class FakeUserRepository:
    def get_user_email(self, user_id):
        return f"user{user_id}@fake.local"


class DummyLogger:
    def log(self, msg):
        pass


class NullNotifier:
    def send(self, to, message):
        pass


def test_create_order_integration_with_fake_repository():
    """
    Test de integración:
    - BD real
    - Lógica real
    - Fake en lugar de API externa
    """

    db = SessionLocal()

    order = create_order(
        user_id=5,
        amount=75,
        notifier=NullNotifier(),
        logger=DummyLogger(),
        db=db,
        user_repository=FakeUserRepository()
    )

    assert order.status == "CREATED"
    assert order.user_email == "user5@fake.local"

    db.query(Order).delete()
    db.commit()
    db.close()