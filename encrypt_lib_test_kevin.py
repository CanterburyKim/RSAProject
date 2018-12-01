from encrypt_lib_kevin import *

h = 'my name is kevin. hello there'
q = split_message_into_chunks(h)
print(h)
print(q)

print('--------------------------Chunks to Num---------------------')
d = convert_chunks_into_numbers(q)
print(d)


print('-------------------------Nums to Base64----------------------')
d = base64_encode_numbers(d)
print(d)
