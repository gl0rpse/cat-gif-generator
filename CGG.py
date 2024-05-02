import requests
import webbrowser

# API KEY AND URL FOR TheCatAPI where gifs will be pulled from
API_KEY = 'live_8P0IpvzMB7nGPMTil22sVyM50nfhxTCdlBFNcajuOHBJeQPpWsmLLa5I6XaodhVs'
BASE_URL = 'https://api.thecatapi.com/v1/images/search'

## getGif()
## Helper method to get a cat gif using the API
def getGif():
    headers = {
        'x-api-key': API_KEY
    }
    params = {
        'mime_types': 'gif',
        'limit': 1
    }
    response = requests.get(BASE_URL, params=params, headers=headers)
    data = response.json()
    if data:
        gif_url = data[0]['url']
        return gif_url
    else:
        return None

## Main Method
def main():
    catGif = getGif()
    if catGif:
        print("Here's a pretty kitty for you: ", catGif)
        webbrowser.open(catGif)  # Will open the gif in a web browser
    else:
        print("Sorry, couldn't find a cat GIF.") 

if __name__ == '__main__':
    main()