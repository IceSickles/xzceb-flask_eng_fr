import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get('vHvvYp0APui1nimm0vJRzKfxTfT2VsJXG7ZbNQTvyXyH')
url = os.environ.get('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/99298ab4-62fd-40cf-8f8f-8eea39e595ab')

# Set some variables
API_KEY = 'vHvvYp0APui1nimm0vJRzKfxTfT2VsJXG7ZbNQTvyXyH'
API_URL = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/99298ab4-62fd-40cf-8f8f-8eea39e595ab'
MODEL_ID = 'en-fr'
TEXT_TO_TRANSLATE = 'Your content you want to translate here'

# Prepare the Authenticator
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(API_URL )

# Translate
def english_to_french(english_text):
    """ This is for translating """
    translation = language_translator.translate(
    text=TEXT_TO_TRANSLATE,
    model_id=MODEL_ID).get_result()
    return translation

def french_to_english(french_text):
    """ This is for translating """
    translation = language_translator.translate(
    text=TEXT_TO_TRANSLATE,
    model_id=MODEL_ID).get_result()
    return translation

# Print results
print(json.dumps((english_to_french, french_to_english), indent=2, ensure_ascii=False))
