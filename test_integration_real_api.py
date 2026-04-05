# test_integration_real_api.py

from order_service import create_order
from database import SessionLocal, Base, engine
from user_repository import JsonPlaceholderUserRepository

# Aseguramos que las tablas existan antes del test
Base.metadata.create_all(bind=engine)


class DummyLogger:
    def log(self, msg):
        # Logger que no hace nada (implementación mínima)
        pass


class NullNotifier:
    def send(self, to, message):
        # Notifier que no hace nada (evita efectos reales)
        pass


def test_create_order_integration_real_api():
    """
    Test de integración con:
    - API real (JSONPlaceholder)
    - Base de datos real (SQLite)
    - Lógica real (create_order)
    """

    db = SessionLocal()

    order = create_order(
        user_id=1,
        amount=50,
        notifier=NullNotifier(),
        logger=DummyLogger(),
        db=db,
        user_repository=JsonPlaceholderUserRepository()
    )

    assert order.status == "CREATED"

    db.close()