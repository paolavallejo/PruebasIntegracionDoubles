# test_integration.py
from order_service import create_order

class SpyNotifier:
    def __init__(self):
        self.sent = []

    def send(self, to, message):
        self.sent.append((to, message))

class DummyLogger:
    def log(self, msg):
        pass


def test_create_order_with_real_api():
    notifier = SpyNotifier()
    logger = DummyLogger()

    result = create_order(
        user_id=1,
        amount=50,
        notifier=notifier,
        logger=logger
    )

    assert result["status"] == "CREATED"
    assert notifier.sent
