from instaloader import Instaloader, Profile
import pandas as pd

# create an instance of Instaloader class
loader = Instaloader()

# login to Instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
loader.context.log("Logging in...")
loader.context.login(username, password)

# get the username of the account whose followers and following you want to export
target_username = input("Enter the username of the Instagram account: ")

# get the profile of the target account
profile = Profile.from_username(loader.context, target_username)

# get the list of followers and following of the target account
followers_list = []
following_list = []

for follower in profile.get_followers():
    followers_list.append(follower.username)
for followee in profile.get_followees():
    following_list.append(followee.username)

# Load follower and following data into dataframes
followers_df = pd.DataFrame(followers_list, columns=["Followers"])
following_df = pd.DataFrame(following_list, columns=["Following"])

# Export dataframes to Excel file
file_name = target_username + ".xlsx"
with pd.ExcelWriter(file_name) as writer:
    followers_df.to_excel(writer, sheet_name="Followers", index=False)
    following_df.to_excel(writer, sheet_name="Following", index=False)

print("Data exported successfully to " + file_name)
