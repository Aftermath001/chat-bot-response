import re
import long_responses as long

def message_probabilty(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Counts words present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    #Calculates the percent of recognised word in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list [bot_response] = message_probabilty(message, list_of_words, single_response, required_words)
    #Responses-------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'sup','heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you','doing'], required_words=['how'])
    response('Thank you!', ['i','love', 'code', 'palace'], required_words=['code','palace'])

    response (long.R_ATING, ['how', 'old', 'you'], required_words=['old','you'])
    response (long.R_DESC, ['who', 'describe', 'alvin', 'adams'], required_words=['describe','alvin','adams'])
    response (long.R_ADVC, ['advice', 'me', 'life'], required_words=['advice','me'])
    response (long.R_KENYA, ['about', 'kenya', 'tell'], required_words=['about','kenya'])
    response (long.R_MORINGA, ['where', 'moringa', 'school', 'about'], required_words=['moringa','school','about'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

#Create a function get_reponse
def get_response(user_input):
    #Split the message to analyse each individually
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))