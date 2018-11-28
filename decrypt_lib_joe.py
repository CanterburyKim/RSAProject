def convert_numbers_to_strings(numbers):
    """
    numbers is a list of numbers.
    Convert each of those into a string,
    put it into a list and return that list
    """
    num_string_list=[]
    for num in numbers:
        num_str=convert_number_to_string(num)
        num_string_list.append(num_str)
            
    return(num_string_list)

    # TODO: Joe


def temp_test():
    """
    numbers is a list of numbers.
    Convert each of those into a string,
    put it into a list and return that list
    """
    # TODO: Joe

    converted_string = 'convx'
    return converted_string


def assemble_message_from_chunks(message_chunks):

    """
    Take a long message and then split it into
    5-character chunks.  Put those chunks into
    a list and then return that list
    """
    assembled_message = ''
    for chunck in message_chunks:
        # print(chunck)
        assembled_message+=chunck

    print (assembled_message)


    return assembled_message
