# Inventory Management API
This is a FastAPI-based Inventory Management System that allows you to manage products and stock transactions.

# Features

Product CRUD (Create, Read, Update, Delete)
Stock management (IN/OUT transactions)
PostgreSQL/SQLite with SQLAlchemy & Alembic
Dockerized app for easy deployment
Auto-generated OpenAPI docs

# Setup Instructions

1. Clone the repository
git clone https://github.com/Gouravkar123/CoreZen-assignment.git
cd inventory_crud_api
2. Build and start the API using Docker
Make sure Docker is installed and running on your machine.

docker-compose up --build
This will start the API server at:

http://localhost:8000

3. Run migrations manually
If you want to run migrations outside Docker:

alembic upgrade head

# Testing the API with Postman

http://localhost:8000

#Sample API Requests

Method	Endpoint	
● POST /products/ – Add a new product
● GET /products/ – List all products
● GET /products/{id} – Get product details
● PUT /products/{id} – Update product
● DELETE /products/{id} – Delete a product
● POST /stock/ – Record a stock transaction
● GET /stock/ – List all stock transactions
● GET /stock/product/{product_id} – Transactions for a specific product

How to test in Postman
Create a new request in Postman.

Set the HTTP method (GET, POST, PUT, DELETE) and enter the URL combining base URL + endpoint.


Body:
For POST and PUT requests, select Body → raw → JSON and enter the JSON payload.

Send the request and verify the response status and data.

Example POST request in Postman to create a new item
# Method: POST

URL: http://localhost:8000/products/

Body (raw JSON):

{
  "name": "Laptop",
  "description": "High-end gaming laptop",
  "price": 1499.99,
  "available_quantity": 5
}
# GET request to list all items
Method: GET
URL: http://localhost:8000/products/

# Update Product
Method: PUT
URL: http://localhost:8000/products/product_id

# GET request to list specific item
Method: GET
URL: http://localhost:8000/products/product_id

# Delete product
Method: delete
URL: http://localhost:8000/products/product_id

# Stock APIs
Add Stock Transaction
Method: POST
url: http://localhost:8000/stock/stock
Body (raw JSON):

{
  "product_id": 1,
  "quantity": 3,
  "transaction_type": "IN"
}

# GET request to list all items
Method: GET
url: http://localhost:8000/stock/stock

# GET request to list specific item
Method: GET
URL: http://localhost:8000/stock/stock/products/product_id

