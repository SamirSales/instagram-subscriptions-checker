from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.should_append = False
        self.users = []

    def handle_starttag(self, tag, attrs):
        self.should_append = tag == 'a'

    def handle_data(self, data):
        if self.should_append:
            self.users.append(data)

    def get_users(self):
        return self.users


# getting followers
followersFile = open("followers_file.html", "r")
parser = MyHTMLParser()
parser.feed(followersFile.read())
followers = parser.get_users()

# getting subscriptions
subscriptionsFile = open("subscriptions_file.html", "r")
parser2 = MyHTMLParser()
parser2.feed(subscriptionsFile.read())
subscriptions = parser2.get_users()

print("Subscriptions who do not follow you back...\n")

for subs in subscriptions:
    if subs not in followers:
        print(subs)
