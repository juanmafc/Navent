import json
import requests
import urllib.request


searchEngineId = "004100495959909934680:rfmbtoi24pw"
googleAPIKey = "AIzaSyAqEHiJXh_9HfCqPoQ9nsGwBMHj3UvNF3o"
parameters = {"q" : "John Cena", "cx" : searchEngineId, "key": googleAPIKey, "searchType" : "image", "start" : 10}
#MAS DE 10 RESULTADOS
#https://stackoverflow.com/questions/16925762/getting-more-than-10-results-by-google-custom-search-api-v1-in-java
#usar start=indice VAN DE 1 A 10, 11 A 20
#response = requests.get("https://www.googleapis.com/customsearch/v1", params=parameters)



#imagesJson = response.json()
#print(json.dumps(imagesJson, indent=4, sort_keys=True))


json_data=open("respuesta.json").read()
data = json.loads(json_data)
#print(json.dumps(data, indent=4, sort_keys=True))
print(data["items"][0]["image"]["thumbnailLink"])
thumbnailURL = data["items"][3]["image"]["thumbnailLink"]
urllib.request.urlretrieve(thumbnailURL, "images/jc1.jpg")

