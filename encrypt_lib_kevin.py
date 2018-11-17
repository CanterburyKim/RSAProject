def split_message_into_chunks(message):
    chunks = []
    message_length = len(message) / 5
    counter2 = 5
    counter1 = 0
    while message_length > 0:
        five_letters = message[counter1:counter2]
        message_length = message_length - 1
        chunks.append(five_letters)
        counter2 = counter2 + 5
        counter1 = counter1 + 5
    # Take a long message and then split it into
    # 5-character chunks.  Put those chunks into
    # a list and then return that list
    return chunks

# ALL GOOD ^^^

def convert_chunks_into_numbers(chunks_of_strings):
    counter1 = 0
    list_of_chunks_to_num = []
    counter3 = -1
    for chunks in chunks_of_strings:

        chunk = chunks_of_strings[counter1]
        print(chunk)
        chunk_char = [ord(chars) for chars in chunk]
        print(chunk_char)

        counter1 = counter1 + 1
        Length = len(chunk)
        Length = Length - 1
        counter2 =0
        TotalVal = 0
        counterl = Length

        while Length-Length <= counter2 <= Length:
            num = chunk_char[counter2]
            print('{0:08b}'.format(num))
            print('{:08x}'.format(num))

            num = num << (8*counterl)
            print('{0:08b}'.format(num))

            counter2= counter2 + 1
            counterl = counterl - 1

            TotalVal = TotalVal + num
            print('{:08x}'.format(TotalVal))
            print('------------------------------------------------')
            print('')

            if counterl == -1:
                list_of_chunks_to_num.append(TotalVal)
                print('{:08x}'.format(TotalVal))
                TotalVal = 0
                print(list_of_chunks_to_num)
    return list_of_chunks_to_num

h = 'my name is kvin. hello haiaic'
print(h)
h = split_message_into_chunks(h)
print(h)
h = convert_chunks_into_numbers(h)
print(h)


# Takes in a list of chunks of strings and then
# convert them all into numbers.  Put those numbers
# into a list and return that list.
# TODO: Kevin

def base64_encode_numbers(numbers):

    base64_encoded_strings= ['aaaaa','bcdef','ghtff']
    return base64_encoded_strings

#takes list of numbers and then base64 encodes them
# TODO: Kevin
# TODO use library base64 encode function to encode
# each of the numbers in the list
