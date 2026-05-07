import pytest # import pytest package
from kmer_analyzer import validate_sequence, update_kmer_count, count_kmers_with_context, write_results_to_file # imports functions from kmer_analyzer.py

def test_validate_sequence_basic(): # defines function
  """Checks if function works with valid sequence and k
  
  """
  sequence = 'ATGTCTGTCTGAA' # creates valid sequence
  k = 2 # creates valid length k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is True # checks if result is true
  
def test_validate_sequence_letters(): # defines function
  """Checks if function works with sequence with letter other than A, C, G, or T
  
  """
  sequence = 'ANTGTCTGTCTGAA' # creates sequence with an invalid letter in it
  k = 2 # creates valid length k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is False # checks if result is false
  
def test_validate_sequence_numbers(): # defines function
  """Checks if function works with sequence that has a number in it
  
  """
  sequence = 'A1TGTCTGTCTGAA' # creates sequence with a number in it
  k = 2 # creates valid length k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is False # checks if result is false
  
def test_validate_sequence_length(): # defines function
  """Checks if function works with sequence length shorter than k
  
  """
  sequence = 'A' # creates sequence with length smaller than k
  k = 2 # creates valid length k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is False # checks if result is false
  
def test_validate_sequence_negative(): # defines function
  """Checks if function works with invalid negative k
  
  """
  sequence = 'ATGTCTGTCTGAA' # creates valid sequence
  k = -1 # creates invalid negative k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is False # checks if result is false
  
def test_validate_sequence_empty(): # defines function
  """Checks if function works with invalid empty sequence
  
  """
  sequence = '' # creates invalid empty sequence
  k = 2 # creates valid length k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is False # checks if result is false
  
def test_validate_sequence_symbols(): # defines function
  """Checks if function works with invalid special characters
  
  """
  sequence = 'A/TGTCTGTCTGAA' # creates sequence with invalid special character
  k = 2 # creates valid length k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is False # checks if result is false
  
def test_validate_sequence_lowercase(): # defines function
  """Checks if function works if letters in sequence are lowercase
  
  """
  sequence = 'atgtctgtctgaa' # creates invalid sequence using lowercase letters
  k = 2 # creates valid length k
  result = validate_sequence(sequence, k) # saves result of validate_sequence to a variable
  assert result is False # checks if result is false

def test_update_kmer_kmer_count(): # defnes function
  """Checks if kmers are counted correctly
  
  """
  kmer_data = {} # creates empty dictionary
  kmer = 'AT' # creates kmer
  next_char = 'G' # creates next character after kmer
  update_kmer_count(kmer_data, kmer, next_char) # updates dictionary
  assert kmer_data[kmer]['count'] == 1 # checks if count of kmer is 1
  
def test_update_kmer_next_char_count(): # defines function
  """Checks if next characters are counted correctly
  
  """
  kmer_data = {} # creates empty dictionary
  kmer = 'AT' # creates kmer
  next_char = 'G' # creates next character after kmer
  update_kmer_count(kmer_data, kmer, next_char) # updates dictionary
  assert kmer_data[kmer]['next_chars'][next_char] == 1 # checks if count of next character is 1

def test_count_kmers_with_context_kmer_count(): # defines function
  """Checks if kmers are counted correctly
  
  """
  sequence = 'ATG' # creates valid sequence
  k = 2 # creates valid length k
  result = count_kmers_with_context(sequence, k) # saves output to variable
  assert result['AT']['count'] == 1 # checks if kmer count is 1
  
def test_count_kmers_with_context_next_chars_count(): # defines function
  """Checks if next characters are counted correctly
  
  """
  sequence = 'ATG' # creates valid sequence
  k = 2 # creates valid length k
  result = count_kmers_with_context(sequence, k) # saves output to variable
  assert result['AT']['next_chars']['G'] == 1 # checks if count of next character is 1

def test_write_results_to_file_basic(): # defines function
  """Checks that results are correctly saved to output file
  
  """
  kmer_data = {'AT': {'next_chars': {'G': 1}}} # creates kmer_data dictionary
  write_results_to_file(kmer_data, 'output.txt') # saves results to output file
  with open('output.txt') as f: # opens output file
    results = f.read() # reads output file
  assert 'AT G:1' in results # checks if output is correct
  
def test_write_results_to_file_sorted(): # defines function
  """Checks that results are correctly sorted in alphabetical order
  
  """
  kmer_data = {'TG': {'next_chars': {'T': 1}}, 'AT': {'next_chars': {'G': 1}}} # creates kmer_data dictionary
  write_results_to_file(kmer_data, 'output.txt') # saves results to output file
  with open('output.txt') as f: # opens output file
    lines = f.read().strip().split('\n') # reads output file line by line
  assert lines == ['AT G:1', 'TG T:1'] # checks if kmers appear alphabetically
  
