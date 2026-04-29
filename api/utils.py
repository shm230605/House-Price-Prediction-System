def format_response(price):
    return {
        "predicted_price": round(price, 2),
        "currency": "INR"
    }