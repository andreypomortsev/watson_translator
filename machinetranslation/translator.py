""" This module translate French to English and English to French.

french_to_english: Translates French to English. 
englich_to_french: Translates English to French. """

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

def english_to_french(english_text: str) -> str:
    """Takes an english text and translate it to french"""
    #write the code here
    if english_text == '':
        return english_text
    translation = translator.translate(text=english_text, model_id="en-fr")
    french_text = translation.get_result()["translations"][0]["translation"]
    return french_text

def french_to_english(french_text: str) -> str:
    """Traslate french_text to English, and returns the result"""
    #write the code here
    if french_text == '':
        return french_text
    translation = translator.translate(text=french_text, model_id="fr-en")
    english_text = translation.get_result()["translations"][0]["translation"]
    return english_text
