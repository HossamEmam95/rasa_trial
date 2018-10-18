from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

    rasaNLU = RasaNLUInterpreter("models/nlu/default/chat")
agent = Agent.load("models/dialogue", interpreter= rasaNLU)

# asking question
print(agent.handle_message('Hi Willson'))
# >>> [{'recipient_id': 'default', 'text': 'Hey'}]

# once more
print(agent.handle_message('I want to know the price Toyota Corolla 2010'))
# >>> [{'recipient_id': 'default', 'text': 'There are 31 days in the mentioned month.'}]


# once more
agent.handle_message('Bye')
# >>> [{'recipient_id': 'default', 'text': 'Goodbye'}]
