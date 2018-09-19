from rle import rle_encoder
from rle import rle_decoder
from hypothesis import given, settings
from hypothesis.strategies import text

def test_simple():
    assert rle_encoder("bbbkkk") == "b3k3"
def test_advanced():
    assert rle_encoder("ffffiiiii") == "f4i5"
def test_advanced1():
    assert rle_encoder("ffffggggbbbb444") == "f4g4b443"

def test_simple():
    assert rle_decoder("f3g6") == "fffgggggg"


@given(text())
@settings (max_examples=100)
def test_hypo(x):
    print x
    assert rle_decoder(rle_encoder(x)) == x
