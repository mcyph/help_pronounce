from help_pronounce.libs.file_tools import file_iter
from help_pronounce.libs.conv_keys import conv_keys


def load_index(path):
    """
    Load "Shtooka" audio index files
    """
    DGlobal = {}
    DMap = {}

    seek = 0
    header = None
    for line in file_iter(path):
        seek += len(line)
        if line[0] == '[' and line[-1] == ']':
            header = line.strip('[]')
            continue

        line = line.split('#')[0].strip()
        if not line:
            continue

        if line[0] == '[' and line[-1] == ']':
            header = line.strip('[]')
            continue

        if not header:
            # WARNING!
            continue

        key = line.split('=')[0]
        val = '='.join(line.split('=')[1:])
        if header == 'GLOBAL':
            DGlobal[key] = val
        else:
            if not header in DMap:
                DMap[header] = {}
            DMap[header][key] = val

    for fnam in DMap:
        # TODO: What
        #print fnam
        DMap[fnam] = conv_keys(DMap[fnam])

    return conv_keys(DGlobal), DMap


def map_to_idx(DMap):
    D = {}
    #print DMap.keys()

    for fn, i_D in DMap.items():
        if not fn.endswith('.wav') and not fn.endswith('.ogg') and not fn.endswith('.mp3'):
            #print fn
            continue

        #print i_D

        D.setdefault(
            i_D['Pronounced Text Info']['Text'].lower(), []
        ).append(
            fn.replace('.wav', '').replace('.ogg', '').replace('.mp3', '')
        )

    return D
