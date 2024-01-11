"""
steps input/listen
process/decide 
output talkback

"""



greet_words =['hi','hello','yo']
bye_words= ['bye','tata','hasta la vista']
bad_words= ['naughty','bullshit','fuck','dog','pocha']


def listen():
    return input('say something: ')

def decide(command):
    command = command.lower()
    break_words = command.split(" ")
    print(break_words)
    for words in break_words:
        if words in greet_words:
            talkback('greeting say words')
            return False
        elif words in bye_words:
            talkback('bye words he/she ')
            return True
        elif words in bad_words:
            talkback('the bot does not provide bad words')
            return True
        return False
        

def talkback(response):
    print(response)
while True:
    command = listen()
    if decide(command):
         break
   