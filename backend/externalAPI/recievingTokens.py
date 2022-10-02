import requests
import json
import os
import time

sober_set = []
drunk_set = []

sober_files = os.listdir("../../ml/training-img/sober-img")
drunk_files = os.listdir("../../ml/training-img/drunk-img")


DRUNK_BASE_URL = "https://github.com/maxmastali/Drunk-Detection/blob/main/ml/training-img/drunk-img/"
SOBER_BASE_URL = "https://github.com/maxmastali/Drunk-Detection/blob/main/ml/training-img/sober-img/"

#listdear

# defining the api-endpoints
API_ENDPOINT_PARAMETERS = "https://api-us.faceplusplus.com/facepp/v3/detect"

API_ENDPOINT_METRICS = "https://api-us.faceplusplus.com/facepp/v3/face/analyze"

# your API key here
API_KEY = "kIUCMuGnUQd6IubuCqgIrBlDybZAq3HY"

API_SECRET_KEY = "APjSP3feDjklNt27__tkKnqiOAsQymmV"

imageURLS = []
noSpacesImageURLS = []

for img in sober_files:
    imageURLS.append(f'{SOBER_BASE_URL}{img}?raw=true')

for img in drunk_files:
    imageURLS.append(f'{DRUNK_BASE_URL}{img}?raw=true')

for url in imageURLS:
    noSpacesImageURLS.append(url.replace(" ","%20"))

index = 0

#"https://github.com/maxmastali/Drunk-Detection/blob/main/ml/taining-img/sober-img/Screenshot%202022-10-01%20124835.jpg?raw=true""
#https://github.com/maxmastali/Drunk-Detection/blob/main/ml/taining-img/sober-img/Capture4.PNG?raw=true
for url in noSpacesImageURLS:

    # parameters to be sent to api
    tokenParameters = {'api_key': API_KEY,
                       'api_secret': API_SECRET_KEY,
                       'image_url': url}

    # sending post request and saving response as response object
    parametersR = requests.post(url=API_ENDPOINT_PARAMETERS, data=tokenParameters)

    # extracting response text
    pastebin_url = parametersR.text

    jsonResponse = json.loads(pastebin_url)
    faces = jsonResponse["faces"]
    face = faces[0]
    token = face["face_token"]


    metricParameters = {'api_key': API_KEY,
                        'api_secret': API_SECRET_KEY,
                        'face_tokens': token,
                        'return_landmark': "1",
                        'return_attributes': "gender,age,smiling,headpose,skinstatus,eyegaze,mouthstatus,beauty,emotion,eyestatus,blur,facequality"}

    # sending post request and saving response as response object
    metricsR = requests.post(url=API_ENDPOINT_METRICS, data=metricParameters)

    # extracting response text
    pastebin_url2 = metricsR.text

    if DRUNK_BASE_URL in url:
        # open text file
        text_file = open(f'../../ml/training-json/drunk/{url[len(SOBER_BASE_URL):-13]}.json', "w")
    else:
        text_file = open(f'../../ml/training-json/sober/{url[len(SOBER_BASE_URL):-13]}.json', "w")

    # write string to file
    n = text_file.write(pastebin_url2)

    # close file
    text_file.close()

    index+=1

    time.sleep(.5)

