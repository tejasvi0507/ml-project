# Creating a dictionary
product = {
    "id": 101,
    "name": "Laptop",
    "price": 50000,
    "brand": "Dell"
}

# Display dictionary
print("Product Details:")
print(product)

# Access a value
print("Product Name:", product["name"])

# Add a new key-value pair
product["stock"] = 15

# Update price
product["price"] = 48000

# Remove a key
product.pop("brand")

# Print updated dictionary
print("\nUpdated Product Details:")
for key in product:
    print(key, ":", product[key])