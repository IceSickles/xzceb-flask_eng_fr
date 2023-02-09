import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['vHvvYp0APui1nimm0vJRzKfxTfT2VsJXG7ZbNQTvyXyH']
url = os.environ['https://api.us-east.language-translator.watson.cloud.ibm.com/instances/99298ab4-62fd-40cf-8f8f-8eea39e595ab']

# Set some variables
api_key = 'vHvvYp0APui1nimm0vJRzKfxTfT2VsJXG7ZbNQTvyXyH'
api_url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/99298ab4-62fd-40cf-8f8f-8eea39e595ab'
model_id = 'en-fr'
text_to_translate = 'Your content you want translate here'

# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(api_url )

# Translate
def englishToFrench(englishText):
    translation = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()
    return frenchText
    

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()
    return englishText

# Print results
print(json.dumps(translation, indent=2, ensure_ascii=False))
