import pytest
from UnCodeGL.data_structures.encoder import Encoder

def test_inserting_and_checking():
    simbols = {'a','e','i','o','u'}
    e = Encoder(simbols = simbols,
        dictionary=
            {'aei':'1',
            'aeo':'2',
            'oui':'3',
            'ua':'4',
            'aio':'5'})
    assert e.encode_sentence('aeiaeoua') == '124'

    
    