import streamlit as st
import json
with open("data.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

st.title("Dictionary Interface")

# Select a letter
selected_letter = st.sidebar.selectbox("Select a letter", list(data['Letters'].keys()))

# Custom HTML and CSS
custom_styles = """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
        }
        .header {
            background-color: #007BFF;
            padding: 10px;
            color: white;
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .word-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .word {
            font-size: 20px;
            font-weight: bold;
            color: #007BFF;
        }
        .phonetic {
            font-style: italic;
            margin-top: 5px;
            color: #6c757d;
        }
        .part-of-speech {
            margin-top: 10px;
            font-weight: bold;
            color: #28a745;
        }
        .definition, .example, .translation {
            margin-top: 10px;
        }
        .audio {
            margin-top: 10px;
        }
        .warning {
            background-color: #ffc107;
            color: #856404;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
"""

# Display custom styles
st.markdown(custom_styles, unsafe_allow_html=True)

# Display words for the selected letter
if data['Letters'][selected_letter]['Words']:
    st.markdown('<div class="header">Words Starting with ' + selected_letter + '</div>', unsafe_allow_html=True)
    for word_data in data['Letters'][selected_letter]['Words']:
        st.markdown('<div class="word-container">', unsafe_allow_html=True)
        st.markdown('<div class="word">'+'<b>Word:  ' + word_data['word'] +'<br>' +'</div>', unsafe_allow_html=True)
        st.markdown('<div class="phonetic">' +'<b>Phonetic:  '+ word_data['phonetic'] +'<br>' + '</div>', unsafe_allow_html=True)
        if word_data['audio'] != '':
            st.audio(word_data['audio'], format='audio/mp3') #, start_time=0, key=word_data['word'])
        st.markdown('<div class="part-of-speech">'+'<b>Part of speechs:  ' + ', '.join(word_data['partOfSpeechs']) +'<br>'  + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="definition">' + '<b>Definitions:</b><br>' + '<br>'.join('- ' + d for d in word_data['definitions'] if d != '') + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="example">' + '<b>Examples:</b><br>' + '<br>'.join('- ' + e for e in word_data['examples'] if e != '') + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="translation">' + '<b>Translations:</b><br>' + '<br>'.join('- ' + t for t in word_data['translations'] if t != '') + '</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="warning">No words found for the letter ' + selected_letter + '</div>', unsafe_allow_html=True)