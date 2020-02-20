from help_pronounce.get_package_dir import get_package_dir


def _open_cmu_format(path, encoding, delim):
    D = {}

    with open(path, 'r', encoding=encoding) as f:
        for line in f:
            if line.startswith(';;;'):
                continue
            elif not line.strip():
                continue

            word, phones = line.split(delim)
            word = word.rstrip('()0123456789')
            phones = phones.split()
            D.setdefault(word.lower(), []).append(phones)

    return D


def open_cmu():
    return _open_cmu_format(
        f'{get_package_dir()}/data/cmudict/cmudict-0.7b',
        encoding='latin-1',
        delim='  '
    )


def open_britfone():
    return _open_cmu_format(
        f'{get_package_dir()}/data/britfone/britfone.main.3.0.1.csv',
        encoding='utf-8',
        delim=', '
    )


if __name__ == '__main__':
    for k, L in open_cmu().items():
        print(k, L)

    for k, L in open_britfone().items():
        print(k, L)
