import json
import requests
import urllib



searchEngineId = "004100495959909934680:rfmbtoi24pw"
googleAPIKey = "AIzaSyAqEHiJXh_9HfCqPoQ9nsGwBMHj3UvNF3o"
colors = ["", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink", "black", "brown", "gray", "white"]

def searchImages(query, startIndex):
    parameters = {"q" : query, "cx" : searchEngineId, "key": googleAPIKey, "searchType" : "image", "start" : startIndex}
    response = requests.get("https://www.googleapis.com/customsearch/v1", params=parameters)
    return response.json()

def saveThumbnail(imageData, imageIndex):
    thumbnailURL = imageData["image"]["thumbnailLink"]
    thumbnailFileName = "images/" + str(imageIndex) + "_jc" + ".jpg"
    urllib.urlretrieve(thumbnailURL, thumbnailFileName)


imageIndex = 0
for color in colors:
    query = "John Cena " + color
    for i in range(1,50,10):
        imagesJson = searchImages(query, i)
        for imageData in imagesJson["items"]:
            saveThumbnail(imageData, imageIndex)
            imageIndex = imageIndex + 1
