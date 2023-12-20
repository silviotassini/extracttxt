from tika import parser


def extracttxt(filename):
    """
    Extracts text from a file using Tika.

    Parameters:
    - filename (str): The path to the file to be processed.

    Returns:
    - str or None: Extracted text if successful, None otherwise.
    """
    try:
        # Attempt to parse the file using Tika
        parsed = parser.from_file(filename)

        # Check if the 'content' key is present in the parsed result
        if 'content' in parsed:
            # Return the extracted text
            return parsed['content']
        else:
            # Print an error message if 'content' is not found
            print("Error: Unable to extract file contents.")
            return None
    except Exception as e:
        # Handle exceptions and print an error message
        print(f"Error during text extraction: {e}")
        return None
