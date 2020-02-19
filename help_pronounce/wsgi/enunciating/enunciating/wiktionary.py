import json
import sqlite3


def wiki_search(data_dir, word):
    """
    Returns (
      dict of IPA pronunciations,
      filenames/language for sounds on Wiktionary,
      rhymes with info
    )
    """
    conn = sqlite3.connect(data_dir + 'wiktionary.db')
    c = conn.cursor()
    c.execute('SELECT v FROM wiktionary WHERE k=?', (word,))
    r = c.fetchone()

    if not r:
        c.execute('SELECT v FROM wiktionary WHERE k=? COLLATE NOCASE', (word,))
        r = c.fetchone()

    c.close()
    conn.close()

    return process(*json.loads(r[0])) if r else None


DMap = {
    'RP': 'Received Pronunciation',
    'AmE': 'US',
    'AusE': 'Australian'
}



def process(DIPA, LAudio, LRhymes):
    n_DIPA = {}

    for k, v in DIPA.items():
        k = k.replace(')', '').replace(',', ' ').replace('|', ', ')
        v = [i.replace('{{IPAchar|', '').replace('}}', '').replace('}}', '') for i in v]
        n_DIPA[DMap.get(k, k)] = v

    n_LAudio = []
    for fnam, lang in LAudio:
        lang = lang.replace(')', '').replace(',', ' ').replace('|', ', ')
        lang = DMap.get(lang, lang)
        n_LAudio.append((fnam, lang))

    return n_DIPA, n_LAudio, LRhymes

