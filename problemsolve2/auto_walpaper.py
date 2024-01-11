import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')


dict_content = json.loads(content)

# get the image url
image_url = dict_content['url']

# download doing

res = requests.get(image_url)

# save the iimage

with open('apod.png','wb') as image:
    image.write(res.content)

# set as walpaper
    
try:
    PyWallpaper.change_wallpaper('./apod.png')
    print("Wallpaper set successfully")
except Exception as e:
    print(f"Error setting wallpaper: {e}")


