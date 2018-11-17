from encrypt_lib_kevin import *

print('String to Chunks')
h = 'my name is kevin. hello there'
q = split_message_into_chunks(h)
print(h)
print(q)

print('--------------------------Chunks to Num---------------------')
d = convert_chunks_into_numbers(q)
print(d)
