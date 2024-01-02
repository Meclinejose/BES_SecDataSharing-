import FL_BETS.Optimization
import numpy as np
import Main.En_De
import Main.AA
def Registration_aa(AA_id, AA_pw,a,b,c,d,f,g,h):  # Registraion with Attribute authority
    np.save("Processed//AA_id",AA_id)
    np.save("Processed//AA_pw",AA_pw)
    OTP = hash(((int(AA_id))+h)^h)
    h_ =  OTP^(hash(int(AA_id))+int(h))
    if(int(h) == h_):
        '''print("Attribute authority is Registered with Blockchain")'''

#def Encrypytion(Data,do_id,do_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r):    # Encryption
def Encrypytion(Data):  # Encryption

    En_Data = []
    for i in range(len(Data)):
        En = []
        for j in range(len(Data[i])):
            En.append(Main.En_De.algm(Data[i][j], 1))
        En_Data.append(En)
    Main.AA.Encryption(En_Data)
    return En_Data

def Key_generation(Data, En_data,ks, do_id, r, y1, y2, x1, x2, d, priv, nv):
    x = hash(int(do_id)) // r
    y = y1 + ((y2 - y1) / (x2 - (x1 + 1))) * (x - x1)
    c = 60 * x ** 3 + 6 * x ** 2 + 6
    K = int(y) ^ int((c * d))

    key, privacy, NV = FL_BETS.Optimization.Algm(Data, En_data, K)

    nv.append(NV)
    priv.append(privacy)

    return key

def Decryption(Data,do_id,do_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,K):  # Decryption
    De_Data = []
    for i in range(len(Data)):
        De = []
        for j in range(len(Data[i])):
            De.append(Main.En_De.algm(Data[i][j], K))
        De_Data.append(De)
    return De_Data

def Data_sharing(AA_id,AA_pw,De_Data):    # Data sharing
    AA_id_ = np.load("Processed//AA_id.npy")
    AA_pw_ = np.load("Processed//AA_pw.npy")
    if(AA_id==AA_id_)and(AA_pw==AA_pw_):
        Record = De_Data
        return Record






