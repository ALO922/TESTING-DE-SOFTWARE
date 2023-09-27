import unittest
from nose2.tools import params
from string_handler import string_handler


@params (('AVE','V'),('ROMA','RM'),('SELFIE','SLF'),('INTeR1','NTR1'),('aTLeT1SMO','TLT1SM'))

def test_removeVowels(int,exp):
    assert string_handler.removeVowels(int) == exp