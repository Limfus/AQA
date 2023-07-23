"""
Home-task 11 Generators

# #############################################################################
# write generator function that has as input some range value and chunk_size
# produces output as lists with len == chunk size
# Example:
# Call:  chunk_generator(range(11), chunk_size=3) ->
# Output:  [0, 1, 2]
#          [3, 4, 5]
#          [6, 7, 8]
#          [9, 10]
# #############################################################################

"""


def chunk_generator(data_range, chunk_size):
    # Create a lambda function to get the next chunk
    next_chunk = lambda x: [x + i for i in range(chunk_size)]

    # Initialize the start index to 0
    start_index = 0

    # Continue until we've covered the entire data_range
    while start_index < len(data_range):
        # Get the next chunk using the lambda function
        chunk = next_chunk(start_index)

        # Update the start_index for the next chunk
        start_index += chunk_size

        # Yield the chunk as output
        yield chunk

# Example usage
if __name__ == "__main__":
    for chunk in chunk_generator(range(11), chunk_size=3):
        print(chunk)
