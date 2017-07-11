import requests, urllib
import matplotlib.pyplot as plt
from paralleldots import set_api_key, get_api_key, sentiment


ACCESS_TOKEN = "1595866987.0d51ae1.ecb2290bd5f74b1584894260fc8cfd64"
BASE_URL= "https://api.instagram.com/v1/"
a=[]

KEY= "6nkFU0DD6Ixi1KS7AVqE4ioyLUeG3vRLyFflDW15Oig"
set_api_key("6nkFU0DD6Ixi1KS7AVqE4ioyLUeG3vRLyFflDW15Oig")
get_api_key()

Positive_sentiments = 0
Negative_sentiments = 0
Neutral_sentiments = 0


# Function to show our own information
def apni_jaankari():
    print "GET request url :" + ((BASE_URL + "users/self/?access_token=%s") % (ACCESS_TOKEN))
    upyogkarta_jankaari = requests.get((BASE_URL + "users/self/?access_token=%s") % (ACCESS_TOKEN)).json()
    if upyogkarta_jankaari["meta"]["code"] == 200:
        if len(upyogkarta_jankaari["data"]):
            print "Username: %s" % (upyogkarta_jankaari["data"]["username"])
            print "Followers: %s" % (upyogkarta_jankaari["data"]["counts"]["followed_by"])
            print "Following: %s" % (upyogkarta_jankaari["data"]["counts"]["follows"])
            print "Posts: %s" % (upyogkarta_jankaari["data"]["counts"]["media"])
        else:
            print "USER DOES NOT EXIST"
    elif upyogkarta_jankaari["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print "Error"


# Function to search any user's id
def get_user_id(instagram_username):
    print 'GET request url :' + (BASE_URL + 'users/search?q=%s&access_token=%s') % (instagram_username, ACCESS_TOKEN)
    upyogkarta_jankaari = requests.get((BASE_URL + 'users/search?q=%s&access_token=%s') % (instagram_username, ACCESS_TOKEN)).json()
    if upyogkarta_jankaari["meta"]["code"] == 200:
        if len(upyogkarta_jankaari["data"]):
            return upyogkarta_jankaari["data"][0]["id"]
        else:
            return None
    elif upyogkarta_jankaari["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print "Error"
        exit()


# Function to show the basic information of any user like username, followers, posts etc.
def get_user_information(instagram_username):
    user_id = get_user_id(instagram_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    print 'GET request url :' + (BASE_URL + 'users/%s?access_token=%s') % (user_id, ACCESS_TOKEN)
    upyogkarta_jankaari = requests.get((BASE_URL + 'users/%s?access_token=%s') % (user_id, ACCESS_TOKEN)).json()
    if upyogkarta_jankaari["meta"]["code"] == 200:
        if len(upyogkarta_jankaari["data"]):
            print "Username: %s" % (upyogkarta_jankaari["data"]["username"])
            print "Followers: %s" % (upyogkarta_jankaari["data"]["counts"]["followed_by"])
            print "Following: %s" % (upyogkarta_jankaari["data"]["counts"]["follows"])
            print "Posts: %s" % (upyogkarta_jankaari["data"]["counts"]["media"])
        else:
            print "There is no data for this user"
    elif upyogkarta_jankaari["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print "Error"


# Function to show our own recent posts
def khudki_post():
    print "GET request url :" + (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    apni_post = requests.get((BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)).json()
    if apni_post["meta"]["code"] == 200:
        if len(apni_post["data"]):
            print apni_post["data"][0]["id"]
            tasveer_ka_naam = apni_post["data"][0]["id"] + ".jpeg"
            link = apni_post["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(link, tasveer_ka_naam)
            print "Aapki tasveer download ho chuki hai"
        else:
          print "Media does not exist"
    elif apni_post["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print "Error"


# Function to get any post's id
def get_post_id(instagram_username):
    user_id = get_user_id(instagram_username)
    if user_id == None:
        print "User does not exist!"
        exit()
    print "GET request url :" + (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)
    user_media = requests.get((BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)).json()
    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            return user_media["data"][0]["id"]
        else:
            print "Iss user ne koi post nahi ki huyi"
            exit()
    elif user_media["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print "Error"
        exit()


# Function to download recent post of any user
def get_users_post(instagram_username):
    user_id = get_user_id(instagram_username)
    if user_id == None:
        print "User does not exist!"
        exit()
    print "GET request url :" + (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)
    user_media = requests.get((BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)).json()
    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            link = user_media["data"][0]["images"]["standard_resolution"]["url"]
            tasveer_ka_naam = user_media["data"][0]["id"] + ".jpeg"
            urllib.urlretrieve(link, tasveer_ka_naam)
            print"Aapke dost ki tasveer download hp chuki hai"
            return user_media["data"][0]["id"]
        else:
          print "There is no recent post!"
    elif user_media["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print "Error"

# Function to show the recent posts liked by the owner of Access token
def liked_by_user():
    print "Get request URL:" + ((BASE_URL + "users/self/media/liked?access_token=%s") % (ACCESS_TOKEN))
    liked = requests.get((BASE_URL + "users/self/media/liked?access_token=%s") % (ACCESS_TOKEN)).json()
    print liked["data"][0]["id"]


# Function to get the list of comments on any post
def get_the_comments(instagram_username):
    post_id = get_post_id(instagram_username)
    print "Get request URL:" + ((BASE_URL + "media/%s/comments?access_token=%s") % (post_id, ACCESS_TOKEN))
    comments = requests.get((BASE_URL + "media/%s/comments?access_token=%s") % (post_id, ACCESS_TOKEN)).json()
    for i, d in enumerate(comments["data"]):
        print d["text"]
        a.append(d["text"])
    return a


# Function to like any post of any user
def post_a_like(instagram_username):
    media_id = get_post_id(instagram_username)
    request = (BASE_URL + "media/%s/likes") % (media_id)
    data = {"access_token": ACCESS_TOKEN}
    print "POST request URL : %s" % (request)
    post_a_like = requests.post(request, data).json()
    if post_a_like['meta']['code'] == 200:
        print "Like was successful!"
    elif post_a_like["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print "Your like was unsuccessful. Try again!"


# Function to posy comment using username
def post_a_comment(instagram_username):
    media_id = get_post_id(instagram_username)
    request = (BASE_URL + "media/%s/comments") % (media_id)
    comment = raw_input("Comment?:")
    data = {"access_token": ACCESS_TOKEN, "text": comment}
    print "POST request URL: %s" % (request)
    comment_on_post = requests.post(request, data).json()
    if comment_on_post["meta"]["code"] == 200:
        print "comment done"
    elif comment_on_post["meta"]["code"] == 503:
        print "The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
    else:
        print"comment was unsuccessful"



# Function to perform the sentimental analysis on comments
def pie_chart():
    insta_username = raw_input("Enter the username: \n")
    give_comments = get_the_comments(insta_username)
    for i in give_comments:
        sentiments = sentiment(str(i))
        print sentiments["sentiment"]
        if (sentiments["sentiment"] > 0.75):
            print "Positive sentiments"
            global Positive_sentiments
            Positive_sentiments = Positive_sentiments + 1
        elif (0.25 < sentiments["sentiment"] <= 0.75):
            print "Neutral Sentiments"
            global Neutral_sentiments
            Neutral_sentiments = Neutral_sentiments + 1
        else:
            print "Negative Sentiments"
            global Negative_sentiments
            Negative_sentiments = Negative_sentiments + 1

    labels = 'Positive Sentiments', 'Negative Sentiments', 'Neutral Sentiments'
    sizes = [Positive_sentiments,Neutral_sentiments ,Negative_sentiments ]
    explode = (0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()



# Function to show the main menu of the instaBot
def bot_main():
    while True:
        print "\nHey! Welcome to instaBot!\n\nHere are your menu options:\n" \
              "a.Get your own details\nb.Get details of a user by username\n" \
              "c.Get your own recent post\nd.Get the recent post of a user by username\n" \
              "e.Show the images liked by user\nf.Get the comments using media ID\ng.Like a post\n" \
              "h.Comment on a post\ni.Plot a pie chart of sentimental analysis data"
        choose_option = raw_input("Choose any option from tha given menu:")
        if choose_option == "a":
            apni_jaankari()
        elif choose_option == "b":
            instagram_username= raw_input("Enter the username of user")
            get_user_information(instagram_username)
        elif choose_option == "c":
            khudki_post()
        elif choose_option == "d":
            instagram_username = raw_input("Enter the username of user")
            get_users_post(instagram_username)
        elif choose_option == "e":
            liked_by_user()
        elif choose_option == "f":
            instagram_username = raw_input("Enter the username of user")
            get_the_comments(instagram_username)
        elif choose_option == "g":
            instagram_username = raw_input("Enter the username of user")
            post_a_like(instagram_username)
        elif choose_option == "h":
            instagram_username = raw_input("Enter the username of user")
            post_a_comment(instagram_username)
        elif choose_option == "i":
            pie_chart()

bot_main()