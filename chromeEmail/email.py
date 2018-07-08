
class Email:
    def __init__(self, body, subject, to):
        if type(body) is str:
            self.body = body
        else:
            print('ERROR: [body] should be of type string')

        if type(subject) is str:
            self.subject = subject
        else:
            print('ERROR: [subject] should be of type string')

        if type(to) is str:
            self.to = to
        else:
            print('ERROR: [to] should be of type string')