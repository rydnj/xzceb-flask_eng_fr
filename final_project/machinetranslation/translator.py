"""
COURSE-5: PYTHON PROJECT FOR AI AND APPLICATION DEVELOPMENT

FINAL PROJECT

Program to translates English to French and vice versa using IBM Watson's Language Translator api

"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))

# translation = language_translator.translate(
#     text='Hello, how are you today?',
#     model_id='en-es').get_result()
# print(json.dumps(translation, indent=2, ensure_ascii=False))

def englishToFrench(englishText):
    """
    Method to convert given englishText to french using the translate function
    """
    #write the code here
    if englishText is None:
        return None

    translation = language_translator.translate(text=englishText ,model_id='en-fr').get_result()

    french_text=translation['translations'][0]['translation']

    return french_text

def frenchToEnglish(frenchText):
    """
    Method to convert given frenchText to english using the translate function
    """
    #write the code here
    if frenchText is None:
        return None

    translation = language_translator.translate(text=frenchText ,model_id='fr-en').get_result()

    english_text=translation['translations'][0]['translation']

    return english_text
