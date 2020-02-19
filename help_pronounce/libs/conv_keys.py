DHeaders = {}
DHeaders['Pronounced Text Info'] = {
    # Locals
    'SWAC_TEXT': 'Text',
    'SWAC_LANG': 'Language', # iso 639-code - CONVERT ME!
    'SWAC_ALPHAIDX': 'Alpha Index', # |-delimited indexes (WARNINGL: OFTEN INCLUDES ONLY THE MAIN WORD!)
    'SWAC_BASEFORM': 'Base Form',
    'SWAC_FORM_NAME': 'Form Name',
    'SWAC_FORM_REF': 'Form Reference',
    'SWAC_HOMOGRAPHIDX': 'Homograph Index',
    'SWAC_HOMOGRAPHIDX_REF': 'Homograph Index Reference'
}

DHeaders['Pronunciation Info'] = {
    # Locals
    'SWAC_PRON_INTONATION': 'Intonation',
    'SWAC_PRON_SPEED': 'Speed',
    'SWAC_PRON_COMMENT': 'Comment',
    'SWAC_PRON_API': 'IPA Transcription',
    'SWAC_PRON_PHON': 'Phonetic Transcription'
}

DHeaders['Speaker Info'] = {
    # Globals
    'SWAC_SPEAK_NAME': 'Name',
    'SWAC_SPEAK_GENDER': 'Gender',
    'SWAC_SPEAK_BIRTH_YEAR': 'Birth Year',
    'SWAC_SPEAK_LANG': 'Language', # iso 639-code - CONVERT ME!
    'SWAC_SPEAK_LANG_COUNTRY': 'Country', # Two-letter language code - ADD A FLAG/LINK!
    'SWAC_SPEAK_LANG_REGION': 'Region',
    'SWAC_SPEAK_PRON': 'Pronunciation',
    'SWAC_SPEAK_LIV_COUNTRY': 'Residing in Country', # Two-letter language code - ADD A FLAG/LINK!
    'SWAC_SPEAK_LIV_TOWN': 'Residing in Town',
    'SWAC_SPEAK_CONTACT': 'Contact', # E-Mail?
    'SWAC_SPEAK_DESC': 'Description'
}

DHeaders['Collection Info'] = {
    # Globals
    'SWAC_COLL_NAME': 'Name',
    'SWAC_COLL_SECTION': 'Section',
    'SWAC_COLL_DESC': 'Description',
    'SWAC_COLL_ORG': 'Originating From',
    'SWAC_COLL_ORG_URL': 'Originating URL', # URL
    'SWAC_COLL_LICENSE': 'License',
    'SWAC_COLL_COPYRIGHT': 'Copyright',
    'SWAC_COLL_AUTHORS': 'Authors',
    'SWAC_COLL_URL': 'URL'
}

DHeaders['Technical Info'] = {
    # Globals
    # 1: very poor
    # 2: poor
    # 3: normal
    # 4: good
    # 5: very good
    'SWAC_TECH_QLT': 'Quality',
    'SWAC_TECH_DATE': 'Date',
    'SWAC_TECH_SOFT': 'Software'
}

def conv_keys(DMap):
    """
    Convert {'UNDERSCORE_KEY': Value, ...} to
    {'header': {'Printable key': Value, ...}, ...}
    """
    DRtn = {}
    for key in DMap:
        set_ = False
        for header in DHeaders:
            if key in DHeaders[header]:
                set_ = True
                conv_key = DHeaders[header][key]
                if not header in DRtn:
                    DRtn[header] = {}
                DRtn[header][conv_key] = DMap[key]
        assert set_, 'key %s not set' % key
    return DRtn
