from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server import db

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({'errors': ['Missing required fields']}), 400
    
    
    restaurant = Restaurant.query.get(data['restaurant_id'])
    pizza = Pizza.query.get(data['pizza_id'])
    
    if not restaurant or not pizza:
        return jsonify({'errors': ['Restaurant or Pizza not found']}), 404
    
    # Create new RestaurantPizza
    try:
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400