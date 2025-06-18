from flask import Blueprint, jsonify, request, abort
from app.models import db, Restaurant, Pizza, RestaurantPizza

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        abort(404, description="Restaurant not found")
    
    pizzas = [
        {"id": rp.pizza.id, "name": rp.pizza.name, "ingredients": rp.pizza.ingredients}
        for rp in restaurant.restaurant_pizzas
    ]
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    })

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        abort(404, description="Restaurant not found")

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
