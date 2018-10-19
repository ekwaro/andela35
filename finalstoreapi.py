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
