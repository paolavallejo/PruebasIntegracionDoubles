# test_unit.py
from unittest.mock import Mock
from faker import Faker
import order_service
from order_service import create_order

# Faker para datos realistas
fake = Faker()


# ---------- Dummy ----------
class DummyLogger:
    def log(self, msg):
        pass


# ---------- Stub de requests.get ----------
class FakeResponse:
    """
    Imita al objeto requests.Response,
    pero solo implementa lo que necesitamos: .json()
    """
    def __init__(self, email):
        self._email = email

    def json(self):
        return {"email": self._email}


def fake_get(url):
    """
    Stub de requests.get(url) que evita
    ir a la red y retorna datos controlados
    """
    return FakeResponse(fake.email())


def test_create_order_uses_notifier():
    """
    Prueba unitaria:
    - NO usa la API real
    - NO envía correos reales
    - Verifica que notifier.send() se llame correctamente
    """

    # Arrange
    notifier = Mock()           # Mock: registra interacciones
    logger = DummyLogger()      # Dummy: evita AttributeError

    # Reemplazamos requests.get por nuestro stub
    order_service.requests.get = fake_get

    # Act
    result = create_order(
        user_id=1,
        amount=100,
        notifier=notifier,
        logger=logger
    )

    # Assert
    assert result["status"] == "CREATED"
    notifier.send.assert_called_once()

    # Verificamos con qué argumentos se llamó
    called_email, message = notifier.send.call_args[0]
    assert message == "Order created"
    assert "@" in called_email   # email realista gracias a Faker


def test_create_order_invalid_amount():
    """
    Prueba de lógica propia:
    - No depende de mocks externos
    - Verifica que se lance una excepción
    """

    notifier = Mock()
    logger = DummyLogger()

    order_service.requests.get = fake_get

    try:
        create_order(
            user_id=1,
            amount=-10,   # inválido
            notifier=notifier,
            logger=logger
        )
        assert False, "Se esperaba ValueError por monto inválido"
    except ValueError:
        pass

class StubUserRepository:
    def get_user_email(self, user_id):
        return "test@stub.com"