import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet = True)
nltk.download('wordnet', quiet = True)

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random


store_products = {
    "rice": 60,
    "sugar": 45,
    "milk": 30,
    "bread": 25,
    "eggs": 6,
    "oil": 120,
    "salt": 20
}


training_data = [
    ("hi", "greeting"),
    ("hello", "greeting"),
    ("hey", "greeting"),
    ("store timing", "timing"),
    ("when do you open", "timing"),
    ("bye", "bye"),
    ("thank you", "thanks")
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


def rule_based_response(user_input):
    tokens = preprocess(user_input)

    # Discount
    if "discount" in tokens or "offer" in tokens:
        return "We have 10% discount on rice and oil."

    # Recommendation
    if "recommend" in tokens or "suggest" in tokens:
        return "You can try milk and eggs for a healthy choice."

    # Product + Quantity
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

    return None   # Important → tells ML to handle fallback
    
    
"""def hybrid_chatbot(user_input):

    # Step 1 → ML Intent Detection
    features = extract_features(user_input)
    intent = classifier.classify(features)

    # Step 2 → ML Responses
    if intent == "greeting":
        return "Hello! Welcome to Smart Store 😊"

    elif intent == "timing":
        return "We are open from 9 AM to 9 PM."

    elif intent == "thanks":
        return "You're welcome!"

    elif intent == "bye":
        return "Thank you for visiting!"

    # Step 3 → Rule-Based Fallback
    rule_response = rule_based_response(user_input)

    if rule_response:
        return rule_response

    return "Sorry, I didn’t understand. Please ask about store products."
    
    
print("🛒 Hybrid Store Bot Started")"""


def hybrid_chatbot(user_input):

    # Step 1 → Rule-Based First
    rule_response = rule_based_response(user_input)

    if rule_response:
        return rule_response

    # Step 2 → ML Intent Detection
    features = extract_features(user_input)
    intent = classifier.classify(features)

    if intent == "greeting":
        return "Hello! Welcome to Smart Store 😊"

    elif intent == "timing":
        return "We are open from 9 AM to 9 PM."

    elif intent == "thanks":
        return "You're welcome!"

    elif intent == "bye":
        return "Thank you for visiting!"

    return "Sorry, I didn’t understand. Please ask about store products."


while True:
    user = input("You: ")

    response = hybrid_chatbot(user)
    print("Bot:", response)

    if user.lower() in ["bye", "exit", "quit"]:
        break



