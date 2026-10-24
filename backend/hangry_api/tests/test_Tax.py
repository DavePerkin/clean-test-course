from api.controllers import Tax


def test_SimpleTax():
  subtotal = 15
  deliveryFee = 3.50

  tax = Tax.calculate(subtotal, deliveryFee)

  assert tax == 1.53
