# mood_responses.py
from mood_list import responses

def mood_response(mood):
    if mood in responses:
        print(responses[mood])
    else:
        print("Sorry, I don't recognize that mood. Could you try another?")