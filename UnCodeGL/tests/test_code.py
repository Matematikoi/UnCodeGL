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
    assert abs(c_ternary.get_word_length(s) - 1.5238095238095237) < 0.000001

def test_huffman_3():
    s = source.Source({
    'A': 0.18714983403983043,
    'B': 0.00012422018715508277,
    'C': 9.997600575861794e-07,
    'D': 0.00018145645045189156,
    'E': 0.000181206510437495,
    'F': 2.4994001439654485e-07,
    'G': 0.015813704710869392,
    'H': 0.0016503539150603856,
    'I': 0.007314744461329281,
    'J': 1.999520115172359e-06,
    '0': 0.0007353235223546349,
    '1': 0.0039295569063424775,
    '2': 0.002786081340478285,
    '3': 0.0017475805806606414,
    '4': 0.001256948332400224,
    '5': 0.0010270035191554028,
    '6': 0.0009242781732384228,
    '7': 0.0008440474286171319,
    '8': 0.0008075561865152364,
    '9': 0.0007700651843557546,
    'K': 0.002064004638886667,
    'L': 0.0037888406782372232,
    'M': 7.498200431896344e-07,
    'N': 0.0007848116452051508,
    'O': 2.4994001439654485e-07,
    'P': 2.4994001439654485e-07,
    'a': 0.0852215468287611,
    'b': 0.012018115652243462,
    'c': 0.02543689514516516,
    'd': 0.04101315684235783,
    'e': 0.09827666360073582,
    'f': 0.004158252019515317,
    'g': 0.006718387586979125,
    'h': 0.012569233383987842,
    'i': 0.04051352675357914,
    'j': 0.008708659921618811,
    'k': 1.7745741022154683e-05,
    'l': 0.04147654562904903,
    'm': 0.020000699832040312,
    'n': 0.04507543189634488,
    'o': 0.07263956650403904,
    'p': 0.016297338638726705,
    'q': 0.008388486763176838,
    'r': 0.04958185035591458,
    's': 0.0643380588658722,
    't': 0.030299728065264337,
    'u': 0.030096526833559945,
    'v': 0.00980689634487723,
    'w': 1.999520115172359e-06,
    'x': 0.00036991122130688634,
    'y': 0.01395914980404703,
    'z': 0.0028780592657762136,
    'Q': 3.2492201871550826e-06,
    'R': 0.00012422018715508277,
    'S': 4.998800287930897e-07,
    'T': 0.0007883108054067023,
    'V': 0.007120791010157562,
    'U': 0.005069533312005119,
    'W': 0.005639646484843637,
    'X': 0.0013276813564744461,
    'Y': 0.004972306646404863,
    'Z': 0.0011747180676637606,
    '-': 3.049268175637847e-05})
    c = code.Code.make_huffman_code(s, code_alphabet={'0','1','2'})
    assert abs(c.get_word_length(s) -2.7978700111973134) < 0.00001
