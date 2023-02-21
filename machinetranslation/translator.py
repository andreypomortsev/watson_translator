import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

# authentication to the IBM cloud
authenticator = IAMAuthenticator(APIKEY)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Service location url
translator.set_service_url(URL)

def englishToFrench(englishText: str, translator=translator) -> str:
    """Takes an english text and translate it to french"""
    #write the code here
    translation = translator.translate(text=englishText, model_id="en-fr")
    frenchText = translation.get_result()["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText: str, translator=translator) -> str:
    """Traslate frenchText to English, and returns the result"""
    #write the code here
    translation = translator.translate(text=frenchText, model_id="fr-en")
    englishText = translation.get_result()["translations"][0]["translation"]
    return english_text


print('Success')