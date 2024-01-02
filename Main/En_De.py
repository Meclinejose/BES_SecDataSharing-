import binascii, random,numpy as np

from Main.en_de_ import  en_de,dec_da

def algm(msg,n):

    bits = 64
    generate = ""
    for i in range(bits): generate+=str(random.randint(1, 9))
    key = str(generate)
    'Encryption'
    encryptedMsg= en_de(str.encode(key))



    np.save("Processed//encript__",encryptedMsg)
    res = binascii.hexlify(encryptedMsg)  # convert encrypted to hexadecimal format
    encrypted = int(res,16)

    np.save("Processed//encrypted",encrypted)
    np.save("Processed//encryptedMsg",encryptedMsg)
    np.save("Processed//generate",generate)

    chunks, chunk_size = len(encryptedMsg), len(encryptedMsg)

    res = [encryptedMsg[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
    d_gen=str(msg)

    decryptedMsg = dec_da(str.encode(d_gen))
    if (n == 1):
        return (encrypted)
    else:
        return str(decryptedMsg)

