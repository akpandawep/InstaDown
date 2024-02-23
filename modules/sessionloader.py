import re
from instaloader import Instaloader, Post,TwoFactorAuthRequiredException
username = "itz_riya_.06_"
password = "q6md7q2tmpnator.live121"
loader = Instaloader(download_videos=True, download_geotags=False, download_comments=False, compress_json=False)
def sessiongen(username,password):
    try:
        loader.login(username, password)
        loader.save_session_to_file(filename=f"./instadownsession")
        return "Successfully Configured the Bot"
    except TwoFactorAuthRequiredException:
        return "Disable Two Factor Authentication and try again"
    except Exception as e:
        print(e)
        return "Invalid Username or Password.\n\n__If you're facing Still this Issue Report @riz4d"
    
