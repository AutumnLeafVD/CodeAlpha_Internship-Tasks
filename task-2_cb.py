import nltk
from nltk.chat.util import reflections

# Download necessary NLTK packages
nltk.download('punkt')
nltk.download('wordnet')

# Define a list of common greetings the user might use
greetings = ["hi", "hello", "hey", "what's up?"]

# Define a dictionary of FAQs with questions and answers
faq_list = {
    "What is your purpose?": "I am a simple FAQ chatbot designed to answer your questions about [Topic Name].",
    "Can you [action]?" : "Unfortunately, I cannot perform actions in the real world yet. I can answer your questions about [Topic Name].",
    "How does [Topic Name] work?": "[Detailed explanation of how the topic works]",
    "What are the benefits of [Topic Name]?" : "[List of benefits]",
    "What are the limitations of [Topic Name]?" : "[List of limitations]"
}

# Define a function to preprocess user input
def preprocess(text):
  tokens = nltk.word_tokenize(text.lower())  # Tokenize and lowercase the text
  return tokens

# Define a function to find the most similar question in the FAQ list
def find_best_match(user_input):
  processed_input = preprocess(user_input)
  scores = {faq: nltk.edit_distance(processed_input, preprocess(q)) for faq, q in faq_list.items()}
  return max(scores, key=scores.get)

# Define a function to respond to the user
def respond(user_input):
  if user_input in greetings:
    return "Hi! How can I help you today?"
  else:
    best_match = find_best_match(user_input)
    return faq_list.get(best_match, "Sorry, I don't understand your question. Can you rephrase it?")

# Start the chatbot interaction
while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break
  print("Chatbot: " + respond(user_input))
