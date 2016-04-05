from django.http import HttpResponse, StreamingHttpResponse
from django.template import RequestContext, loader


from load_index import load_index, map_to_idx


DIndex = {}

from os import getcwdu
print getcwdu()

DGlobal = {}
DWords = {}

DSetKey = {'David (Australian)': 'eng-play-it', 'Betsy (US)': 'eng-wcp-us'}
DGlobal['David (Australian)'], DWords['David (Australian)'] = load_index('../../data/sound/eng-play-it/index.tags.txt')
DGlobal['Betsy (US)'], DWords['Betsy (US)'] = load_index('../../data/sound/eng-wcp-us/index.tags.txt')

for k in list(DWords.keys()):
    DWords[k] = map_to_idx(DWords[k])

print 'BETSY:', DWords['Betsy (US)']


def index(r):
    template = loader.get_template('index.html')
    context = RequestContext(r, {})
    return HttpResponse(template.render(context))


def dynamic(r):
    audio_files = []

    for key in DWords:
        i_audio_files = DWords[key].get(r.GET['q'].lower().strip(), [])
        if i_audio_files:
            audio_files.append([DSetKey[key], key, i_audio_files])

    print audio_files
    template = loader.get_template('dynamic.html')
    context = RequestContext(r, {
        'audio_files': audio_files
    })
    return HttpResponse(template.render(context))


def get_sound(r):
    fnam = r.GET['file']
    key = r.GET['key']
    assert key in ('eng-wcp-us', 'eng-play-it')
    assert not '.' in fnam
    assert not fnam.startswith('/')
    assert not fnam.startswith('\\')
    fnam = fnam.replace('\\', '/')

    f = open('../../data/sound/%s/%s.mp3' % (key, fnam), 'rb')
    return HttpResponse(f, content_type='audio/mpeg')



