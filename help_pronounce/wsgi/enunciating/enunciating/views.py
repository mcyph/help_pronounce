import os
from django.http import HttpResponse, StreamingHttpResponse
from django.template import RequestContext, loader
from help_pronounce.libs.load_index import load_index, map_to_idx
from help_pronounce.libs.load_svox import load_svox
from help_pronounce.libs.load_cmu import open_britfone, open_cmu
from help_pronounce.wsgi.enunciating.enunciating.wiktionary import wiki_search

DJ_PROJECT_DIR = os.path.dirname(__file__)

DIndex = {}
#from os import getcwdu
#print getcwdu()

DGlobal = {}
DWords = {}

DATA_DIR = DJ_PROJECT_DIR + '/../../../data/'
DSetKey = {
    'David (Australian)': 'eng-play-it',
    'Betsy (US)': 'eng-wcp-us',
    'Text-to-Speech (US)': 'eng-svox-us',
    'Text-to-Speech (UK)': 'eng-svox-gb'
}

DGlobal['David (Australian)'], DWords['David (Australian)'] = load_index(
    DATA_DIR+'sound/eng-play-it/index.tags.txt'
)
DGlobal['Betsy (US)'], DWords['Betsy (US)'] = load_index(
    DATA_DIR+'sound/eng-wcp-us/index.tags.txt'
)
for k in list(DWords.keys()):
    DWords[k] = map_to_idx(DWords[k])

DWords['Text-to-Speech (US)'] = load_svox(DATA_DIR, 'us')
DWords['Text-to-Speech (UK)'] = load_svox(DATA_DIR, 'gb')


DBritFone = open_britfone()
DCMUDict = open_cmu()

#print 'BETSY:', DWords['Betsy (US)']


def index(r):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context))


def dynamic(r):
    if not r.GET['q'].strip():
        return HttpResponse('')
    q = r.GET['q'].lower().strip()

    # Add phones info
    cmu_pronunciations = []
    if q in DBritFone:
        for phones in DBritFone[q]:
            cmu_pronunciations.append(("British (britfone)", phones))
    if q in DCMUDict:
        for phones in DCMUDict[q]:
            cmu_pronunciations.append(("American (cmudict)", phones))

    # Search for plain audio files
    audio_files = []
    for key in DWords:
        i_audio_files = DWords[key].get(q, [])
        if i_audio_files:
            audio_files.append([DSetKey[key], key, i_audio_files])

    # Search for wiktionary information
    LWiki = wiki_search(DATA_DIR, r.GET['q'].strip())

    template = loader.get_template('dynamic.html')
    context = {
        'cmu_pronunciations': cmu_pronunciations,
        'audio_files': audio_files,
        'LWiki': LWiki
    }
    return HttpResponse(template.render(context))


def get_sound(r):
    fnam = r.GET['file']
    key = r.GET['key']
    assert key in ('eng-wcp-us', 'eng-play-it', 'eng-svox-gb', 'eng-svox-us')
    assert not '.' in fnam
    assert not fnam.startswith('/')
    assert not fnam.startswith('\\')
    fnam = fnam.replace('\\', '/')

    f = open(DJ_PROJECT_DIR+'/../../../data/sound/%s/%s.mp3' % (key, fnam), 'rb')
    return HttpResponse(f, content_type='audio/mpeg')


