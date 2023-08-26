import qrcode
import json

data = {
    "store": {
        "name": "McDonalds",
        "address": "123 Sample Street, Sample City, SC 12345",
        "phone": "(123) 456-7890",
        "website": "www.mcdonalds.com"
    },
    "cashier": "John Doe",
    "transactionId": "T123456789",
    "date": "2023-06-11T15:30:00Z",
    "items": [
        {
            "name": "Fries",
            "quantity": 2,
            "price": 4.99
        },
        {
            "name": "Ham Burger",
            "quantity": 1,
            "price": 9.99
        },
        {
            "name": "Coca Cola",
            "quantity": 2,
            "price": 4.99
        },
        {
            "name": "Dessert",
            "quantity": 1,
            "price": 9.99
        },
        {
            "name": "Nuggets",
            "quantity": 2,
            "price": 4.99
        },
        {
            "name": "Chicken Burger",
            "quantity": 1,
            "price": 9.99
        },
    ],
    "subTotal": 19.97,
    "tax": 1.20,
    "total": 21.17,
    "paymentMethod": "Visa Ending in 1234"
}

# Convert the data to a string
data_str = json.dumps(data)

# Generate the QR code
img = qrcode.make(data_str)

# Save the QR code to a file
img.save("receipt_qr_code_9.png")