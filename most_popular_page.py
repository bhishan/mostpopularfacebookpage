import facebook #sudo pip install facebook-sdk 
from collections import Counter 
import itertools 
# the access token should be stored as a string 
access_token = "CAACEdEose0cBAHmnWcPlAY8YiEdQgK5tPPFZClzZCeLmYpw2z3AH8aZAHZB8rZAJ0JySvQpIQltZCuYeIrA46f0M4rizbaJadYP6wfTOqFCZAVSlJNpZBCP1RGZANy9TNdhS02lf9GKnTWR2ZBTUFbg7Di5hHtePIFBHQzIsZBjIwIuxdDkbwvMTwH9gQwKM2s5KXjL4QeGWrTUnARESA7S7Cbt"

g = facebook.GraphAPI(access_token) #creating connection to the Facebook Graph API through facebook-sdk 

friends = g.get_connections("me", "friends")['data'] #getting the name and id of friends 

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] for friend in friends } #a dictionary comprehension to store 

#frined's name as key and liked page information as it's value 

friends_likes = Counter([like['name'] for friend in likes for like in likes[friend] if like.get('name')]) #counting the repetition of pages 
#and getting name of the page 

friends_likes_id = Counter ([like['id'] for friend in likes for like in likes[friend] if like.get('id')]) 
#getting id for the pages with 
#repetitions 
for i in friends_likes.most_common(10): #getting the 10 most repeated pages amongst friends, returns a tupple with page name and no. of likes 
    print i[0],i[1] 

for i,j in itertools.izip(friends_likes.most_common(10),friends_likes_id.most_common(10)): #using itertools to iterate through two items and printing the page name with the global likes 
    print i[0],g.get_object(j[0])['likes']


