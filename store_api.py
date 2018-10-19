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
sales_made = [{
         'id': 1,
         'customer': 'Stanley',
         'category': 'smart phones',
         'quantity': 2,
         'price': 2000,
         'total': 4000
     },
    {
     'id': 2,
     'customer': 'Dominic',
     'category': 'smart phones',
     'quantity': 1,
     'price': 2000,
     'total': 2000
    },
    {
     'id': 3,
     'customer': 'Brian',
     'category': 'mercedes',
     'quantity': 2,
     'price': 300000,
     'total': 600000
     }]


@app.route('/storemanager/v1/products/', methods=['GET'])
def get_all_products():
    return jsonify({'goods': goods})


@app.route('/storemanager/v1/products/<int:productId>/', methods=['GET'])
def get_product(productId):
    item = [product for product in goods if product['id'] == productId]
    return jsonify({'item': item[0]})


@app.route('/storemanager/v1/products/', methods=['POST'])
def create_product():
    product = {
             'id': goods[-1]['id'] + 1,
             'category': request.json['category'],
             'name': request.json['name'],
             'description': request.json['description']
               }
    goods.append(product)
    return jsonify({'goods': product}), 201


@app.route('/storemanager/v1/sales/', methods=['POST'])
def create_sales():
    record = {
         'id': sales_made[-1]['id'] + 1,
         'customer': request.json['customer'],
         'category': request.json['category'],
         'quantity': request.json['quantity'],
         'price': request.json['price'],
         'total': request.json['total']
         }
    sales_made.append(record)
    return jsonify({'sales_made': record}), 201

@app.route('/api/v1/sales/', methods=['GET'])
def sales():
    return jsonify({'sale_made': sales_made}), 200


if __name__ == '__main__':
    app.run(debug=True)