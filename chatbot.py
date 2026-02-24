import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmer = WordNetLemmatizer()

# Sample customer support knowledge base
faq_data = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Welcome! How may I assist you?"
    ],
    "hours": [
        "Our store is open from 9 AM to 9 PM, Monday to Saturday."
    ],
    "order_status": [
        "You can check your order status in the 'My Orders' section.",
        "Please provide your order ID to track your order."
    ],
    "returns": [
        "You can return a product within 7 days of delivery.",
        "Refunds are processed within 3–5 business days."
    ],
    "goodbye": [
        "Thank you for contacting us. Have a great day!",
        "Goodbye! Feel free to reach out anytime."
    ]
}

# Combine all responses into a corpus
sentences = []
responses = []

for key in faq_data:
    for reply in faq_data[key]:
        sentences.append(key.replace("_", " "))
        responses.append(reply)

# Text preprocessing
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Greeting check
def greeting(user_input):
    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    for word in user_input.lower().split():
        if word in greetings:
            return random.choice(faq_data["greeting"])
    return None

# Chatbot response
def chatbot_response(user_input):
    greet = greeting(user_input)
    if greet:
        return greet

    sentences.append(user_input)

    vectorizer = TfidfVectorizer(tokenizer=preprocess)
    tfidf = vectorizer.fit_transform(sentences)

    similarity = cosine_similarity(tfidf[-1], tfidf)
    idx = similarity.argsort()[0][-2]

    sentences.pop()

    if similarity[0][idx] < 0.2:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
    else:
        return responses[idx]

# Chat loop
print("Customer Support Bot 🤖 (type 'bye' to exit)")
while True:
    user = input("You: ")
    if user.lower() in ["bye", "exit", "quit"]:
        print("Bot:", random.choice(faq_data["goodbye"]))
        break
    print("Bot:", chatbot_response(user))

