def chunking_by(numbers, chunck):
  #Function takes 2 parameters: numbers,and chunck

  #numbers: the list of numbers to be chunked

  #chunck: the size of each chunk

  #Check if the list 'numbers' is empty
    if not numbers:
      
        return []
      
    #Create an empty list to store chunked variable
    chunks = []

    # Iterate through 'numbers' and create chunks of size 'chunck'
    for x in range(0, len(numbers), chunck):
      
      # Append a chunk of size 'chunk' to 'chunks'
        chunks.append(numbers[x:x + chunck])
        
    return chunks


