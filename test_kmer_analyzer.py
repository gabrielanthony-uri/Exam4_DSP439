import pytest
from kmer_analyzer import validate_sequence, update_kmer_count, count_kmers_with_context, write_results_to_file

def test_validate_sequence_basic():
  sequence = 'ATGTCTGTCTGAA'
  k = 2
  result = validate_sequence(sequence, k)
  assert result is True
  
def test_validate_sequence_letters():
  sequence = 'ANTGTCTGTCTGAA'
  k = 2
  result = validate_sequence(sequence, k)
  assert result is False
  
def test_validate_sequence_numbers():
  sequence = 'A1TGTCTGTCTGAA'
  k = 2
  result = validate_sequence(sequence, k)
  assert result is False
  
def test_validate_sequence_length():
  sequence = 'A'
  k = 2
  result = validate_sequence(sequence, k)
  assert result is False
  
def test_validate_sequence_negative():
  sequence = 'ATGTCTGTCTGAA'
  k = -1
  result = validate_sequence(sequence, k)
  assert result is False
  
def test_validate_sequence_empty():
  sequence = ''
  k = 2
  result = validate_sequence(sequence, k)
  assert result is False
  
def test_validate_sequence_symbols():
  sequence = 'A/TGTCTGTCTGAA'
  k = 2
  result = validate_sequence(sequence, k)
  assert result is False
  
def test_validate_sequence_lowercase():
  sequence = 'atgtctgtctgaa'
  k = 2
  result = validate_sequence(sequence, k)
  assert result is False

def test_update_kmer_kmer_count():
  kmer_data = {}
  kmer = 'AT'
  next_char = 'G'
  update_kmer_count(kmer_data, kmer, next_char)
  assert kmer_data[kmer]['count'] == 1
  
def test_update_kmer_next_char_count():
  kmer_data = {}
  kmer = 'AT'
  next_char = 'G'
  update_kmer_count(kmer_data, kmer, next_char)
  assert kmer_data[kmer]['next_chars'][next_char] == 1
