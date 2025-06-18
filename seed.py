from app import create_app
from app.models import db, Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Domino's", address="123 Pizza Street")
    r2 = Restaurant(name="Papa John's", address="456 Dough Blvd")

    p1 = Pizza(name="Pepperoni", ingredients="Cheese, Tomato, Pepperoni")
    p2 = Pizza(name="Margherita", ingredients="Cheese, Tomato, Basil")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
