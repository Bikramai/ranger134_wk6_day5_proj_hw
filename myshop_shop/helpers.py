#Here in helpers.py we are making api call 

import decimal
import requests 
import requests_cache 
import json 


#setup our api cache location (this is going to make a temporary database storage for our api calls)

# requests_cache.install_cache('image_cache', backend='sqlite')



def get_character(name):

   

    # response = requests.get(url, headers=headers)
    # data = response.json()
    # print(data)
    # # name = [character.get('name') for character in data]
    # homeworld = ""

    # for character in data:
    #      if character['name'] == name:
    #         homeworld = character["homeworld"]
    # homeworld = [character.get('homeworld') for character in data]
    # return  homeworld

    
    #This is the api I tried but doesn't work not sure what i did woring
    #question to ryan and alex

    url = "https://star-wars-characters.p.rapidapi.com/46DYBV/star_wars_characters"

    headers = {
        "X-RapidAPI-Key": "55def16c37mshf2200fdea0b6328p1d9d57jsn0004b8652316",
        "X-RapidAPI-Host": "star-wars-characters.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    print(data)

    
   ### question here confusing about accessing data?
 
    # prod_id = "" 
    # if 'items' in data.keys():
    #     items = data['items'][0]['name']

    # return prod_id



    # def get_image(search):
    #     url = "https://google-search72.p.rapidapi.com/imagesearch"

    #     querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    #     headers = {
    #         "X-RapidAPI-Key": "55def16c37mshf2200fdea0b6328p1d9d57jsn0004b8652316",
    #         "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    #     }

    #     response = requests.get(url, headers=headers, params=querystring)

    #     data = response.json()

    #     img_url = ""

    #     if 'items' in data.keys():
    #         img_url = data['items'][0]['originalImageUrl'] 

    #     return img_url 


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it



# now we need to import the helper.py to models.py #