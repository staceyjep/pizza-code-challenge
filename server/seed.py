from server import create_app, db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create sample pizzas
    cheese = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pepperoni = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
    veggie = Pizza(name='Veggie', ingredients='Dough, Tomato Sauce, Cheese, Vegetables')
    
    # Create sample restaurants
    dominos = Restaurant(name='Dominos', address='123 Main St')
    pizza_hut = Restaurant(name='Pizza Hut', address='456 Oak Ave')
    little_caesars = Restaurant(name='Little Caesars', address='789 Pine Rd')
    
    # Add to session
    db.session.add_all([cheese, pepperoni, veggie, dominos, pizza_hut, little_caesars])
    db.session.commit()
    
    # Create restaurant pizzas
    rp1 = RestaurantPizza(price=10, pizza_id=cheese.id, restaurant_id=dominos.id)
    rp2 = RestaurantPizza(price=12, pizza_id=pepperoni.id, restaurant_id=dominos.id)
    rp3 = RestaurantPizza(price=15, pizza_id=veggie.id, restaurant_id=pizza_hut.id)
    
    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()
    
    print("Database seeded successfully!")