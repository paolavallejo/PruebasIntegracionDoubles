# run_app.py
from order_service import create_order

class ConsoleNotifier:
    def send(self, to, message):
        print(f"[EMAIL] To: {to} | Message: {message}")

class ConsoleLogger:
    def log(self, msg):
        print(f"[LOG] {msg}")


if __name__ == "__main__":
    result = create_order(
        user_id=1,
        amount=150,
        notifier=ConsoleNotifier(),
        logger=ConsoleLogger()
    )

    print("\n✅ ORDER RESULT")
    print(result)