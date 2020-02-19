# -*- coding: utf-8 -*-
from re import match, search
from toolkit.data_paths import data_path
from flazzle.dicts.mediawiki.Import.open_wiki import open_wiki


def process_wiktionary():
    path = data_path(
        'dicts-wikipedia',
        'enwiktionary-20140222-pages-articles.xml'
    )
    for k, D in open_wiki(path, 'enwiktionary'):
        if k == 'article':
            #if D['title'] != 'tortoise':
            #    continue

            i = process_entry(D['data'])
            if any(x for x in i):
                #print D['title'], i
                yield D['title'], i
            elif '===Pronunciation===' in D['data']:
                print 'WARNING:', D['title']

        else:
            print k


def process_entry(s):
    #print s

    DIPA = {}
    LAudio = []
    LRhymes = []
    h1 = h2 = None

    for line in s.split('\n'):
        line = line.strip()

        # Main headings
        m = match(r'^==([^=]+)==$', line)
        if m:
            h1 = m.group(1).strip()
            #print h1

        # Subheadings
        m = match(r'^===+([^=]+)===+$', line)
        if m:
            h2 = m.group(1).strip()
            #print h1, h2


        if not (h1 == 'English' and h2 == 'Pronunciation'):
            continue
        #else:
            #print line,


        # IPA
        m = search(r'\{\{a\|(.+?)\}\} \{\{IPA\|(.+?)(\|lang=en)?\}\}', line)
        if m:
            # (variant, ipa)
            DIPA.setdefault(m.group(1), []).append(m.group(2))
        else:
            m = search(r'\{\{IPA\|(.+?)(\|lang=en)?\}\}', line)
            if m:
                DIPA.setdefault('US', []).append(m.group(1))
        #print m,


        # Audio
        m = search(r'\{\{audio\|(.+?)\|Audio(.*)(\|lang=en)?\}\}', line)
        if m:
            fnam, variant, _ = m.groups()
            variant = variant.strip().strip('()')
            LAudio.append((fnam, variant))
        #print m,

        # Rhymes
        m = search(r'\{\{rhymes\|(.+?)(\|lang=en)?\}\}', line)
        if m:
            LRhymes.append(m.group(1))
        #print m

    return DIPA, LAudio, LRhymes


if __name__ == '__main__':
    import json
    DOut = {}

    xx = 0
    for word, i in process_wiktionary():
        DOut[word] = i
        print word, i
        xx += 1

        if xx % 1000 == 0:
            print xx

        #if xx > 100:
        #    break

    with open('wiktionary.json', 'wb') as f:
        f.write(json.dumps(
            DOut, ensure_ascii=False
        ).encode('utf-8'))
