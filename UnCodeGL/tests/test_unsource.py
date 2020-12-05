import pytest
import sys
import os

from UnCodeGL import source

def test_constructor():
    # Test base string
    s = source.Source(base_string="aaaeeioooo")
    assert {'a': 0.3, 'e': 0.2, 'i': 0.1, 'o': 0.4} == s.dictionary
    # Test error when dictionary probs don't add up to 1
    try :
        s = source.Source({'a':0.5,'b':0.4})    
    except Exception as e:
        assert e.args[0] == 'dictionary probabilites does not add up to 1'
    # Test dictionary when using *args with the dictionary
    s= source.Source({'e': 0.25, 'a': 0.2, 'u': 0.2, 'o': 0.2, 'i': 0.15})
    assert s.dictionary == {'e': 0.25, 'a': 0.2, 'u': 0.2, 'o': 0.2, 'i': 0.15}
    # Test dictionary when passing the dictionary using **kargs
    s= source.Source(dictionary= {'e': 0.25, 'a': 0.2, 'u': 0.2, 'o': 0.2, 'i': 0.15})
    assert s.dictionary == {'e': 0.25, 'a': 0.2, 'u': 0.2, 'o': 0.2, 'i': 0.15}

def test_alphabet():
    s= source.Source(base_string = 'aeiouaeoiuaeoaiue')
    assert s.get_alphabet() == ['a','e','i','o','u']