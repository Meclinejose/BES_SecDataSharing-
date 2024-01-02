import Proposed_BES_SecDataSharing.Block_chain
import User
import numpy as np
def Registration_user(user_id,user_pw,a,b,c,d):
    v1 = (hash((int(user_id))+int(d)))^int(c)
    e = c
    e_ = v1 ^ (hash(int(user_id))+int(d))
    if(int(e)==e_):
        '''print("user is verified with Attribute authorty")'''
    return v1

def Registration_do(do_id,do_pw,V1,a,b,c,d,f):
    np.save("Processed//Data_OwnerID_pw", do_id)
    np.save("Processed//do_pw", do_pw)

def Registration_aa(aa_id, aa_pw,a,b,c,d,f,g,h):
    Proposed_BES_SecDataSharing.Block_chain.Registration_aa(aa_id, aa_pw, a, b, c, d, f, g, h)
def Encryption(En_Data):
    return En_Data

def Authentication(user_id,user_pw,aa_id,aa_pw,server_id,server_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,A2):
    U = 0
    for j in range(len(user_pw)):
        U += ord(user_pw[j])
    A2_ = hash((int(user_id))+U)//r+T
    if(A2==A2_):
        print("user is Authenticated with Attribute authorty")
def Data_Access_control(do_id,do_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P):
    r = 1
    TSC = hash(Sg)//int(r)
    User.Data_Access_control(do_id,do_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,TSC,P)

def Validation(do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P):
    DO_ID_ = np.load("Processed//Data_OwnerID_pw.npy")
    DO_PW_ = np.load("Processed//do_pw.npy")

    if(do_id==DO_ID_)and(do_pw==DO_PW_):
        c= 1
        r = 1
        Spwd = hash(int(c)+Sg)//int(r)
        S = User.Validation_(Spwd,do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P)
        U = 0
        for j in range(len(do_pw)):
            U += ord(do_pw[j])
        S_ =  hash(Spwd^U)
        if(S==S_):
            print("Data owner is Validated")
    return Spwd

def Data_sharing(aa_id,aa_pw,do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data):
    C_id = np.load("Processed//Data_OwnerID_pw.npy")
    C_Pw = np.load("Processed//do_pw.npy")
    if(C_id==do_id) and (do_pw==C_Pw):
        print("Validated")
    Records = Proposed_BES_SecDataSharing.Block_chain.Data_sharing(aa_id, aa_pw, De_Data)
def Download(do_id,do_pw,aa_id,aa_pw,user_id,user_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data,K,server_id, server_pw):
    user_id_ = np.load("Processed//User_Id.npy")
    user_pw_ = np.load("Processed//user_pw.npy")
    U = 0
    for j in range(len(server_pw)):
        U += ord(server_pw[j])
    if(user_id==user_id_)and(user_pw_==user_pw):
        r = 1
        K = 0.1
        U =1
        Ky = (hash((int(aa_id))+K))+ (hash(int(U))//int(r))
        Dh_ = []
        for i in range(len(De_Data)):
            Dh = []
            for j in range(len(De_Data[i])):
                #int(aa_id))
                Dh.append(hash(De_Data[i][j])+int(Ky))
            Dh_.append(Dh)
    return Dh_,Ky