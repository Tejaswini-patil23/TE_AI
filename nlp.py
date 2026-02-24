import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random


# ----------------------------
# Knowledge Base (Products)
# ----------------------------

store_products = {
    "rice": 60,
    "sugar": 45,
    "milk": 30,
    "bread": 25,
    "eggs": 6,
    "oil": 120,
    "salt": 20
}


# ----------------------------
# ML Training Data
# ----------------------------

training_data = [
    ("hi", "greeting"),
    ("hello", "greeting"),
    ("bye", "bye"),
    ("thank you", "thanks"),
    ("store timing", "timing"),
    ("when do you open", "timing"),
    ("home delivery", "delivery"),
    ("deliver items", "delivery"),
    ("book order", "booking"),
    ("online order", "booking")
]


def extract_features(text):
    words = word_tokenize(text.lower())
    return {word: True for word in words}


training_set = [(extract_features(text), label) for (text, label) in training_data]
classifier = nltk.NaiveBayesClassifier.train(training_set)


lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens


# ----------------------------
# Rule-Based Expert Logic
# ----------------------------

def rule_based_response(user_input):
    tokens = preprocess(user_input)

    # Discount
    if "discount" in tokens or "offer" in tokens:
        return "We have 10% discount on rice and oil today."

    # Recommendation
    if "recommend" in tokens or "suggest" in tokens:
        return "We recommend milk and eggs for a healthy diet."

    # Product + Quantity Handling
    for product in store_products:
        if product in tokens:
            price = store_products[product]

            numbers = [int(word) for word in tokens if word.isdigit()]

            if numbers:
                quantity = numbers[0]
                total = quantity * price
                return f"{quantity} {product} will cost ₹{total}."
            else:
                return f"{product} is available at ₹{price} per unit."

    return None


# ----------------------------
# Step Guidance Functions
# ----------------------------

def delivery_steps():
    return (
        "🏠 Home Delivery Process:\n"
        "1. Select products and quantity.\n"
        "2. Provide delivery address.\n"
        "3. Choose payment method (Online/COD).\n"
        "4. Confirm order.\n"
        "5. Delivery within 24 hours."
    )


def booking_steps():
    return (
        "🛒 Online Order Booking Steps:\n"
        "1. Visit store website/app.\n"
        "2. Add products to cart.\n"
        "3. Review cart items.\n"
        "4. Proceed to checkout.\n"
        "5. Make payment.\n"
        "6. Receive order confirmation SMS."
    )


# ----------------------------
# Hybrid Expert System
# ----------------------------

def store_expert_system(user_input):

    # Step 1 → Rule-based logic first
    rule_response = rule_based_response(user_input)
    if rule_response:
        return rule_response

    # Step 2 → ML Intent Detection
    features = extract_features(user_input)
    intent = classifier.classify(features)

    if intent == "greeting":
        return "Welcome to Smart General Store 🛒"

    elif intent == "timing":
        return "Store is open from 9 AM to 9 PM."

    elif intent == "thanks":
        return "Thank you for visiting our store!"

    elif intent == "bye":
        return "Goodbye! Visit again."

    elif intent == "delivery":
        return delivery_steps()

    elif intent == "booking":
        return booking_steps()

    return "Sorry, please ask about products, delivery, or booking."


# ----------------------------
# Main Loop
# ----------------------------

print("🛒 General Store Expert System Started")

while True:
    user = input("You: ")
    response = store_expert_system(user)
    print("System:", response)

    if user.lower() in ["bye", "exit", "quit"]:
        break
