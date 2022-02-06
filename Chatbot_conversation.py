import Chatbot_word_cleanup as cleanup
import re, random

##each pair is an array of [x,y] where 
##x is an array of keywords to trigger action,
##y is an array of responses
##r for regular expression
pairs =[
    [
        r".*subtask.*",
        ["What number task should this new subtask fall under?",
        "This new subtask should go under what task number?"]
    ],
    [
        r".*add.*",
        ["What task should I add to your TODO list?",
        "I'm ready! Let's add a task to your TODO list.",
        "What task am I adding?"]
    ],
    [
        r".*search.*until.*|.*get.*until.*",
        ["Get tasks until what date and time?"]
    ],
    [
        r".*search.*|.*get.*",
        ["What would you like to search today?",
        "I can help with that! What would you like to search?",
        "Let me help you find what you're looking for!",
        "Type some key words so I know what to search!"]  
    ],
    [
        r".*count.*|.*stats.*|.*statistics.*",
        ["Sure! Let's see some statistics about your tasks."]
    ],
    [
        r".*list.*|.*due.*|.*TODO list.*",
        ["Here's your TODO list!",
        "What's due on your list?"]
    ],
    [
        r".*tasks?.*|.*options?.*|.*choices?.*|.*help.*",
        ["You can:\nadd task\t\tadd subtask\nsearch task by name\tsearch task by date\nview stats\t\tlist tasks"]
    ]
]

def arrToString(arr):
    ret_string = ""
    for a in arr:
        ret_string += a
    return ret_string

#override respond function in nltk to take in array of keywords
def reply(str):
        # check each pattern
        for (pattern, response) in pairs:
            match = re.match(pattern, str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                return resp

#override converse function in nltk to get user input and convert to array of cleaned words
def conversation(quit="quit"):
    user_input = input("Type quit to exit ")
    if(user_input != quit) :
        arr = cleanup.askCleanString(user_input)
        s = arrToString(arr)
        print(reply(s))
        conversation()

#execute bot
conversation()