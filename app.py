import time

from flask import Flask, request, jsonify
from products import products

app = Flask(__name__)

def getProductByName(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        return productFound[0]
    return {}

@app.route('/products')
def getProducts():
    return jsonify({'message': "Product's List", 'products': products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = getProductByName(product_name)
    if(productFound):
        return jsonify({'message': 'Product found', 'product': productFound})
    return jsonify({'message': 'Product not found'})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
       "name": request.json['name'],
       "price": request.json['price'],
       "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'message': 'Product Added Succesfully', 'products': products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = getProductByName(product_name)
    if (productFound):
        productFound['name'] = request.json['name']
        productFound['price'] = request.json['price']
        productFound['quantity'] = request.json['quantity']
       
        return jsonify({'message': 'Product Updated', 'products': products})
    return jsonify({'message': 'Product not found'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = getProductByName(product_name)
    if(productFound): 
        products.remove(productFound)
        return jsonify({'message': 'Product deleted', 'products': products})
    return jsonify({'message': 'Product not found'})
