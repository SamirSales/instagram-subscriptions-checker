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


def get_items_array1_absent_array2(array1, array2):
    for item_arr_1 in array1:
        if item_arr_1 not in array2:
            print(item_arr_1)


followersFile = open("followers_file.html", "r")
followersHtmlParser = MyHTMLParser()
followersHtmlParser.feed(followersFile.read())
followersArray = followersHtmlParser.get_users()

subscriptionsFile = open("subscriptions_file.html", "r")
subscriptionsHtmlParser = MyHTMLParser()
subscriptionsHtmlParser.feed(subscriptionsFile.read())
subscriptionsArray = subscriptionsHtmlParser.get_users()

print("Users who do not follow you back...\n")
get_items_array1_absent_array2(subscriptionsArray, followersArray)

print("\n\n")
print("Followers who you do not follow back...\n")
get_items_array1_absent_array2(followersArray, subscriptionsArray)
