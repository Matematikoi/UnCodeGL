import pytest
from UnCodeGL import code
from UnCodeGL import source

def test_constructor():
    c = code.Code({'a':'0','b':'10','c':'11','d':'12'})
    assert c.code_alphabet == {'0','1','2'}
    assert c.source_words == {'a','b','c','d'}
    assert c.arity == 3

def test_is_prefix_false():
    c = code.Code({'a':'0','b':'10','c':'11','d':'112'})
    assert not c.is_prefix()

def test_is_prefix_true():
    c = code.Code({'a':'0','b':'10','c':'11','d':'12'})
    assert c.is_prefix()

def test_kraft_inequality_true():
    metric, can_be_instantaneous = code.Code.kraft_inequality_metric(
                    words_length = [4,4,3,6],
                    arity= 2)
    assert metric == 0.265625 
    assert can_be_instantaneous

def test_kraft_inequality_false():
    metric, can_be_instantaneous = code.Code.kraft_inequality_metric(
                    words_length = [3,1,2,1],
                    arity= 2)
    assert metric == 1.375
    assert not can_be_instantaneous


def test_uniquely_decodable_valid():
    c = code.Code(
        {'a':'01',
         'b':'21',
         'c':'0112',
         'd':'212',
         'e':'011'}
    )
    assert c.is_uniquely_decodable()

def test_uniquely_decodable_invalid():
    c = code.Code(
        {'a':'01',
         'b':'21',
         'c':'0110',
         'd':'212',
         'e':'1001'}
    )
    assert not c.is_uniquely_decodable()

def test_decoding_brute_force():
    c = code.Code(
        {'a':'01',
         'b':'21',
         'c':'0112',
         'd':'212',
         'e':'011'}
    )
    assert c.encode('abcade') == '0121011201212011'
    assert c.decode(c.encode('abcade')) == 'abcade'

def test_decoding_trie():
    """UnCodeGL will only use data structure to decode
    when is a prefix code
    """
    c = code.Code(
        {'a':'012',
         'b':'210',
         'c':'0112',
         'd':'212',
         'e':'010'}
    )
    s = 'bcdaeba'
    assert c.encode(s) == '2100112212012010210012'
    assert c.decode(c.encode(s)) == s

def test_word_length():
    s = source.Source({
        'a':1/4,
        'b':1/4,
        'c':1/2
    })
    c1 = code.Code({
        'a':'01',
        'b':'1',
        'c':'00',
    })
    assert abs(c1.get_word_length(s) - 1.75) < 0.00001

    c2 = code.Code({
        'a':'01',
        'b':'00',
        'c':'1',
    })

    assert abs(c2.get_word_length(s) - 1.5) < 0.00001

def test_huffman_1():
    s = source.Source({
        'a':0.49,
        'b':0.26,
        'c':0.12,
        'd':0.04,
        'e':0.04,
        'f':0.03,
        'g':0.02
    })
    c = code.Code.make_huffman_code(s, {'0','1','2'})
    assert abs(c.get_word_length(s)-1.34)<0.00001

def test_huffman_2():
    s = source.Source(base_string = 'aabbcccaadeeeaabcaadcdabbedededecacaeeddccccdcdceaaaddeaaabedbb')
    c_binary = code.Code.make_huffman_code(s, {'0','1'})
    c_ternary = code.Code.make_huffman_code(s, {'0','1','2'})
    assert abs(c_binary.get_word_length(s) - 2.317460317460317) < 0.000001
    assert abs(c_ternary.get_word_length(s) - 1.6507936507936505) < 0.000001
