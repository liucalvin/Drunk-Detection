import requests
import json


# defining the api-endpoints
API_ENDPOINT_PARAMETERS = "https://api-us.faceplusplus.com/facepp/v3/detect"
API_ENDPOINT_METRICS = "https://api-us.faceplusplus.com/facepp/v3/face/analyze"

# your API key here
API_KEY = "kIUCMuGnUQd6IubuCqgIrBlDybZAq3HY"
API_SECRET_KEY = "APjSP3feDjklNt27__tkKnqiOAsQymmV"


def face_plus_plus_analysis(encodedImage):
    # parameters to be sent to api
    tokenParameters = {'api_key': API_KEY,
                       'api_secret': API_SECRET_KEY,
                       'image_base64': encodedImage}

    # sending post request and saving response as response object
    parametersR = requests.post(
        url=API_ENDPOINT_PARAMETERS, data=tokenParameters)

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
    return pastebin_url2
