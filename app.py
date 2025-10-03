from flask import Flask, render_template
import requests

app = Flask(__name__)

SURAH_LIST_API_URL = 'https://quranapi.pages.dev/api/surah.json'
SURAH_DETAIL_API_URL = 'https://quranapi.pages.dev/api/{number}.json'

@app.route('/')
def index():
    try:
        response = requests.get(SURAH_LIST_API_URL)
        response.raise_for_status()
        surahs = response.json()
        surah_names = [surah['surahName'] for surah in surahs]
        return render_template('index.html', surahs=surahs, surah_names=surah_names)
    except requests.RequestException as e:
        error_msg = f'Error fetching surah list: {str(e)}'
        print(error_msg)
        return render_template('index.html', error=error_msg)

@app.route('/surah/<int:number>')
def get_surah(number):
    try:
        url = SURAH_DETAIL_API_URL.format(number=number)
        response = requests.get(url)
        response.raise_for_status()
        surah_data = response.json()
        print(f"API response for surah {number}: {surah_data}")
        return render_template('surah.html', surah=surah_data)
    except requests.RequestException as e:
        error_msg = f'Error fetching surah {number}: {str(e)}'
        print(error_msg)
        return render_template('surah.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)