import sys # import sys package

def validate_sequence(sequence, k): # defines function called validate_sequence with arguments sequence and k
    """Ensures that k>0, the length of the sequence is >=k, and that the sequence only contains the allowed letters
    
    Parameters:
      sequence (str): Sequence of nucleic acids
      k (int): Length of kmers
      
    Returns:
      True or False (bool): True if sequence is valid and False if not
    """
    if k <= 0: # checks if k is positive integer
      return False # returns false if not
    if len(sequence) < k: # checks if length of sequence is less than k
        return False # returns false if it is
    for nucleotide in sequence: # loops through every nucleotide in the sequence
        if nucleotide  not in 'ACGT': # checks if sequence only contains A, C, G, or T
            return False # returns false if any other characters are present
    return True # returns true if the sequence is valid

def update_kmer_count(kmer_data, kmer, next_char): # defines function update_kmer_count with arguments kmer_data, kmer, and next_char
    """Adds kmer and the next character to the dictionary
    
    Parameters:
      kmer_data (dict): Dictionary of kmers
      kmer (str): String of one kmer
      next_char (str): String of character after the kmer
      
    Returns:
      kmer_data (dict): Updated kmer_data dictionary
    """
    if kmer not in kmer_data: # checks if kmer is not in kmer_data
        kmer_data[kmer] = {'count': 0, 'next_chars': {}} # adds kmer to the dictionary if not there already
    
    kmer_data[kmer]['count'] += 1 # adds one to the count of kmer
    
    if next_char not in kmer_data[kmer]['next_chars']: # checks if next_char is not in kmer
        kmer_data[kmer]['next_chars'][next_char] = 0 # adds next_char to the dictionary if not already there
    kmer_data[kmer]['next_chars'][next_char] += 1 # adds one to the count of next_char

    return kmer_data # returns updated kmer_data dictionary

def count_kmers_with_context(sequence, k): # defines function count_kmers_with_context with arguments sequence and k
    """Counts sequence of kmers and the character after them
    
    Parameters:
      sequence (str): Sequence of nucleic acids
      k (int): Length of kmers
      
    Returns:
      kmer_data (dict): Updated kmer_data dictionary
      
    """
    kmer_data = {} # creates empty dictionary
    
    for i in range(len(sequence) - k): # loops through every element in the length of the sequence - k
        kmer = sequence[i:i+k] # gets the first kmer
        next_char = sequence[i+k] # gets the next_char after the kmer
        
        kmer_data = update_kmer_count(kmer_data, kmer, next_char) # saves kmer_data, kmer, and next_char to kmer_data
    
    return kmer_data # returns updated kmer_data dictionary


def write_results_to_file(kmer_data, output_filename): # defines function write_results_to_file with arguments kmer_data and output_filename
    """Saves counts of kmers and next characters to a file
    
    Parameters:
      kmer_data (dict): kmer dictionary
      output_filename (str): Name of output file
      
    Returns:
      None
      
    """
    sorted_kmers = sorted(kmer_data.keys()) # sorts kmers in alphabetical order
    
    with open(output_filename, 'w') as f: # opens output file
        for kmer in sorted_kmers: # loops through the sorted kmers
            next_chars = kmer_data[kmer]['next_chars'] # get dictionary of next_chars
            
            next_char_str = " ".join(
                f"{char}:{freq}" 
                for char, freq in sorted(next_chars.items())
            )
            
            f.write(f"{kmer} {next_char_str}\n")


def main(): # defines main function
    """Main function with all other functions inside
    
    Parameters:
      None
      
    Returns:
      None
      
      
    """
    sequence_file = sys.argv[1] # gets argument from command line
    k = int(sys.argv[2]) # makes k an integer
    output_file = sys.argv[3] # creates output_file
    
    print(f"Reading sequences from {sequence_file}...") # prints message

    with open(sequence_file, 'r') as f: # opens file from command line
        for sequence in f: # loops through sequences in file
            sequence = sequence.strip() # removes whitespace

            if not validate_sequence(sequence, k): # checks if sequence is invalid
                print(f"  Warning: Skipping sequence") # prints if sequence is invalid
                continue # goes to next sequence
            
            kmer_data = count_kmers_with_context(sequence, k) # saves output of count_kmers_with_context to kmer_data dictionary
            
            write_results_to_file(kmer_data, output_file) # saves output to a file

if __name__ == '__main__': # checks if function is the main function
    main() # runs the main function
