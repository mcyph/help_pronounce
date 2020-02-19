from __future__ import with_statement
import codecs


def file_iter(path, encoding='utf-8', errors='strict'):
    """
    Iterate through a file's contents with the
    benefits of `with` with less indentation
    """
    with codecs.open(path, 'rb', encoding, errors=errors) as f:
        for line in f:
            yield line


def file_read(path, encoding='utf-8', errors='strict'):
    """
    Return a file's contents as a string
    """
    with codecs.open(path, 'rb', encoding, errors=errors) as f:
        return f.read()


def file_write(path, txt, encoding='utf-8'):
    """
    Update a file's contents with a string
    """
    with codecs.open(path, 'wb', encoding) as f:
        f.write(txt)
