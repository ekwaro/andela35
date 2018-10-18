from flask import Flask, jsonify, request
#An id is inbuilt object so we use it in our list object instead of creating a key such as productId, salesid
#In the routes, if you want to querry and get results, endeavour to add the type of the variable ,for example int:saleId, other wise you will get an error
#when returning the results for the post, you should return the dictionary you have defined not the name of the list of dictionaries.

app = Flask(__name__)
#Defining alist of dictionaries to hold sample data for the "productId" and products routes

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
#defining a list of dictionaries to hold my sample data for the "sales/ salesId" and the sales routes

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

#defining a default route


@app.route('/')
def hello():
    return 'Hello World'

#will return all the items in the products list


@app.route('/storemanager/v1/products/', methods=['GET'])
def products_all():
    return jsonify({'goods': goods})

#will return a single product querried by the user


@app.route('/storemanager/v1/products/<int:productId>/', methods=['GET'])
def productgood(productId):
    item = [product for product in goods if product['id'] == productId]
    return jsonify({'item': item[0]})

##will return all the items in the sale_made list


@app.route('/storemanager/v1/sales/', methods=['GET'])
def sales():
    return jsonify({'sale_made': sales_made}), 200

#will return a single sale_querried querried by the user


@app.route('/storemanager/v1/sales/<int:sales_Id>/', methods=['GET'])
def sale(sales_Id):
    sell = [sell for sell in sales_made if sell['id'] == sales_Id]
    return jsonify({'item': sell[0]})

## Is used to add a product in the product list


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

# is used to add a sale to a sale list


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


if __name__ == '__main__':

    app.run(debug=True)