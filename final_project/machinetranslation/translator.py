import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('5weYcZR01Dtv6xVvyDO7h4eYYBlUKBa-ss-fCqPJx6IZ')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e2ec6a43-d5d8-41b1-b067-34225efdb0d0')

def englishToFrench(englishText):
    translation = language_translator.translate(text=englishText, model_id="en-fr").get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    translation = language_translator.translate(text=frenchText, model_id="fr-en").get_result()
    englishText = translation['translations'][0]['translation']
    return englishText    