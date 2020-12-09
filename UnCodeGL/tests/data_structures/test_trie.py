import pytest
from UnCodeGL.data_structures.trie import Trie

def test_inserting_and_checking():
    simbols = {'0' , '1' , '2'}
    t = Trie(simbols)
    t.insert('00')
    t.insert('101')
    t.insert('2')
    assert not t.search('0') 
    assert t.search('00')
    assert not t.search('10')
    assert t.search('101')
    assert t.search('2')

def test_prefix():
    simbols = {'0' , '1' , '2'}
    t = Trie(simbols)
    t.insert('0')
    t.insert('1')
    t.insert('20')
    t.insert('21')
    t.insert('22')
    assert t.is_prefix()
    t.insert('01')
    assert not t.is_prefix()

def test_words_init():
    simbols = {'0' , '1' , '2'}
    t = Trie(simbols, words = ['120','000','101'])
    assert t.search('120')
    assert not t.search('100')

def test_complete_word():
    simbols = {'0' , '2' , '1'}
    t = Trie(simbols, words = {'01','21','0112','212','011'})
    assert t.complete_word('01') == {'1','12'}
    assert t.complete_word('21') == {'2'}
    assert t.complete_word('1') == set()
    
