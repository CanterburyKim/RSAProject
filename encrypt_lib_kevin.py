def split_message_into_chunks(message):
    chunks = []
    message_length = len(message) / 5
    counter2 = 5
    counter1 = 0
    while message_length > 0:
        five_letters = message[counter1:counter2]
        print(five_letters)
        message_length = message_length - 1
        chunks.append(five_letters)
        counter2 = counter2 + 5
        counter1 = counter1 + 5


    # Take a long message and then split it into
    # 5-character chunks.  Put those chunks into
    # a list and then return that list
    # TODO: Kevin
    return chunks

def convert_chunks_into_numbers(chunks_of_strings):
    """
    Takes in a list of chunks of strings and then
    convert them all into numbers.  Put those numbers
    into a list and return that list.
    """
    # TODO: Kevin
    numbers = [7,5,6,4]

    return numbers


def base64_encode_numbers(numbers):
    """
    takes list of numbers and then base64 encodes them
    """
    # TODO: Kevin

    # TODO use library base64 encode function to encode
    # each of the numbers in the list

    base64_encoded_strings= ['aaaaa','bcdef','ghtff']
    return base64_encoded_strings
