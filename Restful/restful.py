from flask import Flask
from flask_restful import Api, Resource, fields, marshal, reqparse, abort

app = Flask(__name__)
api = Api(app)


#defining the attributes of a product

goods = []

#method to catch empty product id
def abort_if_productid_does_not_exist(product_id):
    if product_id not in Product:
        abort(404, message="Product {} does not exist".format(product_id))

#Use regparse to accept user input arguments
product_parser = reqparse.RequestParser()
product_parser.add_argument('Category', type = str, location = 'json', required = True,help = 'Category can'+'t be empty')
product_parser.add_argument('Product Name', type = str, location = 'json', required = True,help = 'Product Name can'+'t be empty')
product_parser.add_argument('Price', type = str, location = 'json', required = True,help = 'Price'+'t be empty')
product_parser.add_argument('Quantity Available', type = int, location = 'json', required = True,help = 'Please fill in the quantity')
product_parser.add_argument('Description', type = str, location = 'json', required = True,help = 'Add a description')


#defining a list of sales
sales = []

#defining not to accept empty sales_Id
def abort_if_sales_id_does_not_exist(sales_id):
    if sales_id not in sales:
        abort(404, message = "sales {} does not exist".format(sales_id))


#defining  arguments for the post method in sales
sale_parser = reqparse.RequestParser()
sale_parser.add_argument('Sales Attendant', type=str, location='json', required=True, help='Category can'+'t be empty')
sale_parser.add_argument('Product Name', type=str, location='json', required=True, help='Product Name can'+'t be empty')
sale_parser.add_argument('Unit Price', type=str, location='json', required=True, help='Price'+'t be empty')
sale_parser.add_argument('Quantity', type=int, location='json', required=True, help='Please fill in the quantity')
sale_parser.add_argument('Total', type=str, location='json', required=True, help='Add a description')

#defining the input field type of sales
sale_fields = {
    'Sales Attendant': fields.String,
    'Product Name': fields.String,
    'Unit Price': fields.Integer,
    'Quantity': fields.Integer,
    'Total': fields.String

}

#defining the input fields type of product fields
product_fields = {
    'Category': fields.String,
    'Product Name': fields.String,
    'Price':fields.Integer,
    'Quantity Available':fields.Integer,
    'Description': fields.String
}


class Products(Resource):
    #method to get all items from the product list
    def get(self):
        return goods
#methost to post a product to the product list

    def post(self):
        args = product_parser.parse_args()
        good = {
            'product_id': goods[-1]['product_id'] + 1,
            'Category':args['Category'],
            'Product Name':args['Product Name'],
            'Price':args['Price'],
            'Quantity Available': args['Quantity available'],
            'Description': args['Description']

        }
        goods.append(good)
        return {'Product': marshal(good, product_fields)}, 201


class Product(Resource):
    #querrying for a single product from the product list
    def get(self, product_id):
        abort_if_productid_does_not_exist(product_id)
        return goods[product_id]


class Sales(Resource):
    #querrying all items from the sales list
    def get(self):
        return sales

   #Adding an item to the sales list
    def post(self):
        argument = product_parser.parse_args()
        transaction = {
            'sale_id': goods[-1]['sale_id'] + 1,
            'Sale Attendant': argument['Sale Attendant'],
            'Product Name': argument['Product Name'],
            'Unit Price': argument['Unit Price'],
            'Quantity': argument['Quantity'],
            'Total': argument['Total']

        }
        goods.append(transaction)
        return {'Product': marshal(transaction, product_fields)}, 201


class Sale(Resource):
    #querrying a single item from the sales list
    def get(self, sale_id):
        abort_if_sales_id_does_not_exist(sale_id)
        return sales[sale_id]

#defining the routes to our end points


api.add_resource(Products, '/storemanager/v1/products', endpoint='products')
api.add_resource(Product, '/storemanager/v1/products/<product_id>', endpoint='product')
api.add_resource(Sales, '/storemanager/v1/sales', endpoint='sales')
api.add_resource(Sale, '/storemanager/v1/sales/<sale_id>', endpoint='sale_id')
api.add_resource(Products, '/storemanager/v1/post', endpoint='post')

if __name__ == '__main__':
    app.run(debug=True)