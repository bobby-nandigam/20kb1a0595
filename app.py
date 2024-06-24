from flask import Flask, request, jsonify
import requests
import uuid
import functools

app = Flask(__name__)

# Define the URLs for registration and authentication
REGISTRATION_URL = "http://20.244.56.144/test/register"
AUTH_URL = "http://20.244.56.144/test/auth"

# E-commerce API endpoints (mock examples, replace with actual endpoints)
ECOMMERCE_API_URLS = [
    "http://ecommerce1.example.com/api/products",
    "http://ecommerce2.example.com/api/products",
    # Add more as needed
]

# Placeholder for credentials (normally you'd secure this better)
credentials = {
    "companyName": "Fullstack",
    "ownerName": "Bobby Nandigam",
    "rollNo": "20kb1a0595",
    "ownerEmail": "bobbynandigam.official@gmail.com",
    "accessCode": "nbYNBp",
    "clientID": "",
    "clientSecret": ""
}

# In-memory cache to minimize cost (this can be a more sophisticated cache like Redis)
cache = {}

# Function to register and authenticate with the test server
def register_and_authenticate():
    global credentials
    # Register
    response = requests.post(REGISTRATION_URL, json=credentials)
    registration_data = response.json()
    
    # Update credentials with clientID and clientSecret
    credentials['clientID'] = registration_data['clientID']
    credentials['clientSecret'] = registration_data['clientSecret']
    
    # Authenticate
    auth_data = {
        "companyName": credentials['companyName'],
        "clientID": credentials['clientID'],
        "clientSecret": credentials['clientSecret'],
        "ownerName": credentials['ownerName'],
        "ownerEmail": credentials['ownerEmail'],
        "rollNo": credentials['rollNo']
    }
    response = requests.post(AUTH_URL, json=auth_data)
    return response.json()

# Register and authenticate on startup
auth_response = register_and_authenticate()

# Function to fetch products from e-commerce APIs
def fetch_products_from_apis(category):
    products = []
    for url in ECOMMERCE_API_URLS:
        response = requests.get(url, params={"category": category})
        if response.status_code == 200:
            products.extend(response.json())
    return products

# Generate a unique identifier for each product
def generate_unique_id():
    return str(uuid.uuid4())

# Helper function for caching
def cache_results(key, results, ttl=300):
    cache[key] = {
        "results": results,
        "expiry": time.time() + ttl
    }

def get_cached_results(key):
    if key in cache and cache[key]['expiry'] > time.time():
        return cache[key]['results']
    return None

# Route to get top N products within a category
@app.route("/categories/<string:category>/products", methods=["GET"])
def get_top_products(category):
    n = int(request.args.get("n", 10))
    page = int(request.args.get("page", 1))
    sort_by = request.args.get("sort_by", "rating")
    sort_order = request.args.get("sort_order", "desc")
    
    # Fetch products from cache or APIs
    cache_key = f"{category}_{page}_{n}_{sort_by}_{sort_order}"
    products = get_cached_results(cache_key)
    
    if not products:
        products = fetch_products_from_apis(category)
        
        # Generate unique IDs for products
        for product in products:
            product['id'] = generate_unique_id()
        
        # Sort products
        reverse = True if sort_order == "desc" else False
        products.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        
        # Paginate results
        start = (page - 1) * n
        end = start + n
        products = products[start:end]
        
        # Cache results
        cache_results(cache_key, products)
    
    return jsonify(products)

# Route to get product details by product ID
@app.route("/categories/<string:category>/products/<string:product_id>", methods=["GET"])
def get_product_details(category, product_id):
    # Iterate through cached products to find the product details
    for key, value in cache.items():
        for product in value['results']:
            if product['id'] == product_id:
                return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
