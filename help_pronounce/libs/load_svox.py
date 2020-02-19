from os import listdir


def load_svox(data_dir, variant):
    D = {}

    for fnam in listdir(u'%ssound/eng-svox-%s' % (data_dir, variant)):
        D[fnam.replace('.mp3', '')] = [fnam.replace('.mp3', '')]

    return D

