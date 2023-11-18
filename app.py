import requests
import json
from bs4 import BeautifulSoup
from googletrans import Translator


L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
language = "english"
language_ = "arabic"
data = { 
    "Letters": {
        l : {
            "Words" : []
        } for l in L
}}


def get_info(word):

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print()
    try:
        data = json.loads(str(soup))[0]
    except :
        return {
        'word':word,
        'phonetic':'',
        'audio':'',
        'partOfSpeechs':[''],
        'definitions':[''],
        'examples':['']
    }

    if 'phonetic' in data.keys():
        phonetic = data["phonetic"].strip('/')
    else:
        phonetic = ''
    try:
        audio = data["phonetics"][0]["audio"].strip()
    except:
        audio = ''
    if 'meanings' in data.keys():
        meanings = data['meanings']
    else :
        meanings = ['']
    partOfSpeechs = []
    definitions = []
    examples = []
    for meaning in meanings:
        #print(list(meaning['definitions'][0].keys()))
        if 'partOfSpeech' in meaning.keys():
            partOfSpeechs.append(meaning['partOfSpeech'].strip())
        else:
            partOfSpeechs.append('')
        # if 'definition' in meaning['definitions'][0].keys():
        try :
            definitions.append(meaning['definitions'][0]["definition"].strip())
        except:
            definitions.append('')
        # if "example" in meaning['definitions'][0].keys():
        try :
            examples.append(meaning['definitions'][0]["example"].strip())
        except :
            examples.append('')
    
    return {
        'word':word,
        'phonetic':phonetic,
        'audio':audio,
        'partOfSpeechs':partOfSpeechs,
        'definitions':definitions,
        'examples':examples
    }

def get_Translation(sentence,
                    language_input= language,
                    language_output = language_):
    translator = Translator()

    translated_text = translator.translate(sentence, src=language_input, dest=language_output)
    return translated_text.text

def add_Word(word):
    letter = word[0].upper()
    info = get_info(word)
    translations = [ get_Translation(sentence) if sentence != '' else '' for sentence in info['examples'] ]
    info['translations'] = translations
    data["Letters"][letter]["Words"].append(info)

def delete_Word(word):
    letter = word[0].upper()
    for i,info in enumerate(data["Letters"][letter]["Words"]):
        if info['word'] == word:
            data["Letters"][letter]["Words"].pop(i)

word_list = [
    'Apple', 'Astronaut',
    'Bicycle', 'Balloon',
    'Chocolate', 'Carousel',
    'Dragon', 'Diamond',
    'Elephant', 'Eclipse',
    'Firefly', 'Fountain',
    'Galaxy', 'Guitar',
    'Hammock', 'Hurricane',
    'Iceberg', 'Illusion',
    'Jellyfish', 'Jigsaw',
    'Kaleidoscope', 'Keyboard',
    'Lighthouse', 'Lightning',
    'Mushroom', 'Mountain',
    'Nebula', 'Nomad',
    'Octopus', 'Oasis',
    'Paradox', 'Pegasus',
    'Quasar', 'Quicksand',
    'Rainbow', 'Robot',
    'Sushi', 'Serenade',
    'Telescope', 'Tornado',
    'Umbrella', 'Unicorn',
    'Volcano', 'Velvet',
    'Waterfall', 'Whisper',
    'Xenon', 'Xylophone',
    'Yarn', 'Yogurt',
    'Zephyr', 'Zenith'
]

for i, word in enumerate(word_list):
    add_Word(word)
    print(f"{i} | "+ "-"*40)




with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)