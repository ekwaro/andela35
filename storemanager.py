from flask import Flask, jsonify, request, abort

app = Flask(__name__)

goods = [
    {
        'id': 1,
        'name': 'jeans',
        'category': 'clothes',
        'description': 'German-made'
      },
    {
        'id': 2,
        'name': 'samsung',
        'category': 'smart phones',
        'description': 'newest model',

      },

    {
         'id': 3,
         'name': 'iphone',
         'category': 'smart-phone',
         'description': 'iphone-6x'

      }
]


@app.route('/api/v1/products/', methods=['GET'])
def get_all_products():
    return jsonify({'goods': goods})


@app.route('/api/v1/products/<int:productId>/', methods=['GET'])
def productgood(productId):
    item = [product for product in goods if product['id'] == productId]
    return jsonify({'item': item[0]})


"""Admin should be able to add a product"""
@app.route('/api/v1/products/', methods=['POST'])
def create_product():
    product = {
             'id': goods[-1]['id'] + 1,
             'category': request.json['category'],
             'name': request.json['name'],
             'description': request.json['description']
               }
    goods.append(product)
    return jsonify({'goods': product}), 201

if __name__ == "__main__":
    app.run(debug=True)