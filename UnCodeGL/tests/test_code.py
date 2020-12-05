import pytest
from UnCodeGL import code

def test_constructor():
    c = code.Code({'a':'0','b':'10','c':'11','d':'12'})
    assert c.code_alphabet == {'0','1','2'}
    assert c.source_alphabet == {'a','b','c','d'}
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
    print (metric, can_be_instantaneous)
    assert metric == 1.375
    assert not can_be_instantaneous


