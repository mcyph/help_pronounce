from help_pronounce.libs.file_tools import file_iter
from help_pronounce.libs.load_index import load_index, map_to_idx

DGlobal = {}
DWords = {}
DGlobal['David (Australian)'], DWords['David (Australian)'] = load_index('../data/sound/eng-play-it/index.tags.txt')
DGlobal['Betsy (US)'], DWords['Betsy (US)'] = load_index('../data/sound/eng-wcp-us/index.tags.txt')

for k in list(DWords.keys()):
    DWords[k] = map_to_idx(DWords[k])


LWords = []
for line in open('wordfreq.txt', 'rb'):
    line = line.strip()
    if not line: continue

    _, word, _ = line.split('\t')

    word = word.lower().strip()
    LWords.append(word)


from pprint import pprint
from text_to_speech import TTSEngines
tts_engines = TTSEngines()

pprint(tts_engines.DVoicesByEngine)

for word in LWords:
    if not word in DWords['Betsy (US)']:
        try:
            data = tts_engines.get_mp3_data('SVoxPico', 'en-US', word, 1.0, 1.0)
            with open('../data/sound/eng-prudence/%s.mp3' % word, 'wb') as f:
                f.write(data)
        except:
            print 'ERROR:', word

    #if not word in DWords['David (Australian)']:
    try:
        data = tts_engines.get_mp3_data('SVoxPico', 'en-GB', word, 1.0, 1.0)
        with open('../data/sound/eng-cmu-slt/%s.mp3' % word, 'wb') as f:
            f.write(data)
    except:
        print 'ERROR:', word
