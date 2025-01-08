import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    
    friends = open(file_name).read().splitlines()  # It provided line to read file
    network = []  # It initializes the network list

    # Total users (first line in the file)
    num_users = int(friends[0].strip())
    
    # Dictionary to map users and to their friends
    user_friend_map = {}

    # It processes each friendship entry
    for line in friends[1:]:
        user_u, user_v = map(int, line.strip().split())

        # It adds user_v to user_u's friends list
        if user_u not in user_friend_map:
            user_friend_map[user_u] = []
        user_friend_map[user_u].append(user_v)

        # It adds user_u to user_v's friends list
        if user_v not in user_friend_map:
            user_friend_map[user_v] = []
        user_friend_map[user_v].append(user_u)

    # It constructs the network list sorted by user ID and friends
    network = [(user, sorted(friends)) for user, friends in sorted(user_friend_map.items())]

    return network


def getCommonFriends(user1, user2, network):
    '''
    (int, int, 2D list) -> list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common = []  # It initializes the list for common friends

    # It gets the friends lists for user1 and user2 from the network
    friends1 = next(friends for user, friends in network if user == user1)
    friends2 = next(friends for user, friends in network if user == user2)

    # It finds the intersection using two-pointer technique
    i, j = 0, 0
    while i < len(friends1) and j < len(friends2):
        if friends1[i] == friends2[j]:
            common.append(friends1[i])
            i += 1
            j += 1
        elif friends1[i] < friends2[j]:
            i += 1
        else:
            j += 1

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''
    
    # It finds the user's friends
    user_friends = []
    for u, friends in network:
        if u == user:
            user_friends = friends
            break

    # It initializes recommendation variables
    max_common_friends = 0
    recommended_user = None

    # It iterates over the network
    for other_user, other_friends in network:
        # It skips the given user and their current friends
        if other_user == user or other_user in user_friends:
            continue

        # It finds mutual friends
        mutual_friends = set(user_friends).intersection(other_friends)

        # It updates recommendation based on maximum mutual friends
        if len(mutual_friends) > max_common_friends:
            max_common_friends = len(mutual_friends)
            recommended_user = other_user
        elif len(mutual_friends) == max_common_friends:
            # It breaks ties by selecting the smallest ID
            if recommended_user is None or other_user < recommended_user:
                recommended_user = other_user

    return recommended_user


    


def k_or_more_friends(network, k):
    '''(2Dlist, int) -> int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    
    # It initializes a counter for users with at least k friends
    count = 0
    
    # It iterates through the network
    for user, friends in network:
        if len(friends) >= k:
            count += 1  # It increments the count if user has at least k friends
    
    return count

 

def maximum_num_friends(network):
    '''(2Dlist) -> int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.'''
    
    # It initializes a variable to keep track of the maximum number of friends
    max_friends = 0
    
    # It iterates through the network
    for user, friends in network:
        # It updates max_friends if the current user has more friends
        max_friends = max(max_friends, len(friends))
    
    return max_friends


def people_with_most_friends(network):
    '''(2Dlist) -> 1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in the network.'''
    
    max_friends = 0
    most_friends_users = []
    
    # It iterates through the network to find the maximum number of friends
    for user, friends in network:
        num_friends = len(friends)
        
        # It updates max_friends and reset the most_friends_users list
        if num_friends > max_friends:
            max_friends = num_friends
            most_friends_users = [user]
        # If current user has the same number of friends as max_friends, add them to the list
        elif num_friends == max_friends:
            most_friends_users.append(user)
    
    return most_friends_users



def average_num_friends(network):
    '''(2Dlist) -> number
    Returns an average number of friends over all users in the network'''
    
    total_friends = 0
    total_users = len(network)
    
    # It sums up the number of friends for each user
    for user, friends in network:
        total_friends += len(friends)
    
    # It calculates and return the average
    average = total_friends / total_users if total_users > 0 else 0
    return average

    

def knows_everyone(network):
    '''(2Dlist) -> bool
    Given a 2D-list for friendship network, returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    total_users = len(network)
    
    # It iterates over each user in the network
    for user, friends in network:
        # It checks if the user knows everyone else
        if len(friends) == total_users - 1:
            return True
    
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist) -> int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    while True:
        # It asks for the user ID
        user_input = input("Enter an integer for a user ID: ").strip()

        # It checks if the input is an integer
        if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
            print("That was not an integer. Please try again.")
            continue
        
        user_id = int(user_input)
        
        # It checks if the user ID exists in the network
        ids_in_network = [user[0] for user in network]  # Extract the user IDs from the network
        if user_id not in ids_in_network:
            print("That user ID does not exist. Try again.")
        else:
            return user_id

    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
