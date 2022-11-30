from shop_app import product


def test_prod():
    assert isinstance(product.get_error_message(), str)
