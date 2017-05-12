def secret_message(msg):
    return ''.join([c for c in msg if c.isupper()])


secret_message('Jasleen is Here and Saying HeLLO')
