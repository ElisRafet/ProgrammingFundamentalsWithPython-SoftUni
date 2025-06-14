# class Email:
#     def __init__(self, sender_, receiver_, content_):
#         self.sender_ = sender_
#         self.receiver_ = receiver_
#         self.content_ = content_
#         self.is_sent = False
#
#         def send(self):
#             self.is_sent =True
#
#         def get_info(self):
#             return f"{self.sender_} says to {self.receiver_}: {self.content_}. Sent: {self.is_sent}"
#
# emails = []
# line = input()
#
# while line != 'Stop':
#     tokens = line.split()
#     sender = tokens[0]
#     receiver = tokens[1]
#     content = tokens[2]
#     email = Email(tokens[0], tokens[1], tokens[2])
#     emails.append(email)
#     line = input()
#
# send_emails = [int(x) for x in input().split(', ')]
#
# for x in send_emails:
#     emails[x].send()
#
# for email in emails:
#     print(email.get_info())
#



class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
            self.is_sent = True

    def get_info(self):
            return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails =[]

while True:
    data = input().split()
    if data[0] == 'Stop':
        break
    sender, receiver, content = data
    email = Email(sender, receiver, content)
    emails.append(email)

indices = [int(i) for i in input().split(', ')]

for index in indices:
    emails[index].send()

for email in emails:
    print(email.get_info())