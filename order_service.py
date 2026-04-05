# order_service.py
from models import Order

def create_order(user_id, amount, notifier, logger, db, user_repository):

    # TODO 1: obtener el email desde el repositorio



    logger.log(f"Creating order for {email}")

    # TODO 2: validar que amount sea positivo



    order = Order(
        user_email=email,
        amount=amount,
        status="CREATED"
    )

    # TODO 3: persistir la orden



    notifier.send(email, "Order created")
    return order