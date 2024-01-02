import AA
import owner
import Data_owner
import numpy as np
def Registration_user(user_id,user_pw,a,b,c,d):
    V1 = AA.Registration_user(user_id, user_pw, a, b, c, d)
    return V1
def Registration_do(do_id,do_pw,V1,a,b,c,d,f):
    owner.Registration_do(do_id, do_pw, V1, a, b, c, d, f)
    V2 = hash((int(do_id))+int(a))^f

    f_ = V2 ^ (hash(int(do_id))+int(a))
    if(int(f)==f_):
        print("Data owner is Registered with User")

    return V2
def Authentication(sg,AA_id,AA_pw,server_id,server_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T):
    Data_owner.Authentication(sg, AA_id, AA_pw, server_id, server_pw, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T)
def Authentication_(user_id,user_pw,AA_id,AA_pw,server_id,server_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1):
    U = 0
    for j in range(len(user_pw)):
        U += ord(user_pw[j])

    A2 = (hash((int(user_id))+U))//r+T
    AA.Authentication(user_id, user_pw, AA_id, AA_pw, server_id, server_pw, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, A2)

def Authentication__(do_id,do_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,A3):
    A3_ = hash((int(do_id))+Sg+int(a))//(int(r)+T)
    if(A3_==A3):
        print("Data owner is Authenticated with user")
def Data_Access_control(do_id,do_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,TSC,P):

    TSC_ = hash(Sg)//int(r)
    if(int(TSC)==TSC_):
        C = (hash(TSC)+int(a))//int(P)
        AC = Data_owner.Data_Access_control(C, do_id, do_pw, Sg, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, TSC, P)
        AC_ = C*hash((int(do_id))+int(d)+int(b))
        if(AC==AC_):
            print("Denies Access to the Data owner")

def Validation(do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P):
    Spwd = AA.Validation(do_id, do_pw, user_id, user_pw, server_id, server_pw, Sg, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, P)
    return Spwd
def Validation_(Spwd,do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P):

    S = Data_owner.Validation_(Spwd, do_id, do_pw, user_id, user_pw, server_id, server_pw, Sg, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, P)
    return S
def Data_sharing(AA_id,AA_pw,do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data):
    AA.Data_sharing(AA_id, AA_pw, do_id, do_pw, user_id, user_pw, server_id, server_pw, Sg, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, P, De_Data)
def Download(do_id,do_pw,AA_id,AA_pw,user_id,user_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data,K,server_id, server_pw):
    DO_Id_ = np.load("Processed//Data_OwnerID_pw.npy")
    DO_pw_ = np.load("Processed//do_pw.npy")
    np.save("Processed//user_id",user_id)
    np.save("Processed//user_pw",user_pw)
    if(do_id==DO_Id_) and (do_pw==DO_pw_):
        '''print("Valid")'''
        Dh1,Ky = AA.Download(do_id, do_pw, AA_id, AA_pw, user_id, user_pw, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, P, De_Data, K, server_id, server_pw)

        Dh__ = []
        for i in range(len(De_Data)):
            Dh = []
            for j in range(len(De_Data[i])):
                Dh.append(str(De_Data[i][j]) + str(Ky)) #(hash(int(AA_id)) +
            Dh__.append(Dh)
        for ii in range(len(Dh__)):
            for jj in range(len(Dh__[ii])):
                if(Dh1[ii][jj]!= Dh__[ii][jj]):
                    '''print("Send the record to encrypted manner")'''
            Data_owner.Download_(Dh1)