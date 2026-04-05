def test_create_order_with_real_api():
    db = SessionLocal()

    order = create_order(
        user_id=1,
        amount=100,
        notifier=SpyNotifier(),
        logger=DummyLogger(),
        db=db,
        user_repository=JsonPlaceholderUserRepository()
    )

    assert order.status == "CREATED"
    db.close()