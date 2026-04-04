# test_integration.py
from order_service import create_order
from database import SessionLocal, Base, engine
from user_repository import JsonPlaceholderUserRepository
from models import Order

# Aseguramos que las tablas existan
Base.metadata.create_all(bind=engine)


class SpyNotifier:
    def __init__(self):
        self.sent = []

    def send(self, to, message):
        self.sent.append((to, message))


class DummyLogger:
    def log(self, msg):
        pass


def test_create_order_with_real_api():
    # Arrange
    db = SessionLocal()
    notifier = SpyNotifier()
    logger = DummyLogger()
    user_repo = JsonPlaceholderUserRepository()  # ✅ API real

    # Act
    result = create_order(
        user_id=1,
        amount=50,
        notifier=notifier,
        logger=logger,
        db=db,                         # ✅ BD real
        user_repository=user_repo     # ✅ repositorio real
    )

    # Assert
    assert result.status == "CREATED"
    assert notifier.sent

    # Limpieza (buena práctica en integración)
    db.query(Order).delete()
    db.commit()
    db.close()