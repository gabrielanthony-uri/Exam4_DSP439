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

def test_count_kmers_with_context_kmer_count():
  sequence = 'ATG'
  k = 2
  result = count_kmers_with_context(sequence, k)
  assert result['AT']['count'] == 1
  
def test_count_kmers_with_context_next_chars_count():
  sequence = 'ATG'
  k = 2
  result = count_kmers_with_context(sequence, k)
  assert result['AT']['next_chars']['G'] == 1

def test_write_results_to_file_basic():
  kmer_data = {'AT': {'next_chars': {'G': 1}}}
  write_results_to_file(kmer_data, 'output.txt')
  with open('output.txt') as f:
    results = f.read()
  assert 'AT G:1' in results
  
def test_write_results_to_file_sorted():
  kmer_data = {'TG': {'next_chars': {'T': 1}}, 'AT': {'next_chars': {'G': 1}}}
  write_results_to_file(kmer_data, 'output.txt')
  with open('output.txt') as f:
    lines = f.read().split('\n')
  assert lines == ['AT G:1', 'TG T:1']
  
