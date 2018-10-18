from rasa_nlu.model import Metadata, Interpreter

# loading the interpreter
interpreter = Interpreter.load('./models/nlu/default/chat')

# define function to ask question
def ask_question(text):
    print(interpreter.parse(text))

# asking question
ask_question("I want to know the price Mercedes Benz 2010")
ask_question("Hello Kim")

# ask_question("How many days in January")
# ask_question("How many days in March")
