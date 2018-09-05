from html.parser import HTMLParser


followersFile = open("followers_file.html", "r")
subscriptionsFile = open("subscriptions_file.html", "r")


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
parser = MyHTMLParser()
parser.feed(followersFile.read())
followers = parser.get_users()

# getting subscriptions
parser2 = MyHTMLParser()
parser2.feed(subscriptionsFile.read())
subscriptions = parser2.get_users()

print("Subscriptions who do not follow you back...\n")

for subs in subscriptions:
    follow_you = False

    for follower in followers:
        if subs == follower:
            follow_you = True
            break

    if not follow_you:
        print(subs)