import instaloader

ig = instaloader.Instaloader()
dp = input("enter insta username: ")
print(ig.download_profile(dp, profile_pic=True))
