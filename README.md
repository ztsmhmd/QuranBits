# QuranBits

- Surah List: Displays all 114 surahs with names, Arabic names, translations, revelation place, and total ayahs.
- Ayah Details: Shows verse-by-verse text for a selected surah in Arabic (with diacritics), simplified Arabic, and English translation.
- Audio Playback: Includes a dropdown to select from three reciters (Mishary Rashid Al Afasy, Abu Bakr Al Shatri, Nasser Al Qatami) for whole-surah audio.
- Responsive Design: Uses the Amiri font for Arabic text and a clean, table-based layout.

## Installation

Clone the Repository (or download the files):
```
git clone https://github.com/ztsmhmd/QuranBits.git
cd QuranBits
```

### Set Up a Virtual Environment (recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install Dependencies:
```
pip install -r requirements.txt
```


## Usage

Run the Application:
```
python app.py
```

The app will start in debug mode on http://127.0.0.1:5000/.

### Access the App:

Open your browser and navigate to http://127.0.0.1:5000/.
View the list of surahs in a table or simple list.
Click a surah name (e.g., "Al-Ikhlaas") to see its ayahs and play audio.
Use the reciter dropdown to switch between audio narrations.


### Debugging:

Check the terminal for API response logs if errors occur.
Verify audio URLs (e.g., https://github.com/The-Quran-Project/Quran-Audio-Chapters/raw/refs/heads/main/Data/1/112.mp3) in a browser if playback fails.



## Project Structure

```
quran_app/
├── .gitignore         
├── app.py              
├── templates/          
│   ├── index.html      
│   └── surah.html      
└── requirements.txt    
```

## API Details
The app uses the Quran API with the following endpoints:

https://quranapi.pages.dev/api/surah.json: Lists all 114 surahs.
https://quranapi.pages.dev/api/{number}.json: Provides details for a specific surah, including ayahs and audio URLs.

Audio is sourced from the audio object in the API response, with three reciters selected for playback.
Contributing
Contributions are welcome!

## License
This project is licensed under the GNU License. See the LICENSE file for details.
Contact
For issues or suggestions, please open an issue on the repository or contact the maintainer.
