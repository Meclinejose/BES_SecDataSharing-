import Main.User
import Main.Data_owner
import Main.Server
import Main.AA
import FL_BETS.Block_chain
import time
import numpy as np
import random


def User_perf_threshold(user_ID):
    if np.asarray(user_ID)<=10:
        User_ind=1
    else:
        User_ind=0
    return User_ind
def spoof(data):
    spoofed = []
    for i in range(len(data)):
        spoofed.append(data[i]+str(random.randint(1,100)))
    return spoofed

def callmain(ks,ID,User_Password,do_Pw,server_password,AA_Password,n_usr,a, b, c, d, r, x, x1, x2, y1, y2, f, g, h,Data,Norm_V,PRI):
    T = time.time()
    P = random.randint(1,10)
    priv,nv=[],[]
    for i in range(n_usr):
        user_ID = ID[i]
        user_Pw = User_Password[i]
        DO_ID = ID[i]
        DO_Pw = do_Pw[i]
        Server_ID, Server_Pw = ID[i], server_password[i]
        AA_ID, AA_Pw = ID[i], AA_Password[i]

        V1 = Main.User.Registration_user(user_ID,user_Pw,a,b,c,d)
        V2 = Main.Data_owner.Registration_do(DO_ID,DO_Pw,V1,a,b,c,d,f)
        # Registration is done between server and Attribute authority #
        Main.Server.Registration_server(Server_ID,Server_Pw,a,b,c,d,f,g)
        # Registration between Attribute authority & Block Chain #
        Main.AA.Registration_aa(AA_ID, AA_Pw,a,b,c,d,f,g,h)
        #---------------------------------------------------------------------------------------#

        En_data= FL_BETS.Block_chain.Encrypytion(Data)


        Gen_key=FL_BETS.Block_chain.Key_generation(Data, En_data, DO_ID, ks, r, y1, y2, x1, x2, d, priv, nv)

        De_Data = FL_BETS.Block_chain.Decryption(Data, DO_ID, DO_Pw, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, Gen_key)


        A1,Sg = Main.Server.Authentication(AA_ID,AA_Pw,Server_ID,Server_Pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T)
        Main.User.Authentication_(user_ID,user_Pw,AA_ID,AA_Pw,Server_ID,Server_Pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1)
        # Authentication is done between Data owner and user #
        A3 = Main.Data_owner.Authentication_(DO_ID,DO_Pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1)
        # DAC is done between Data owner and Attribute authority #
        Main.AA.Data_Access_control(DO_ID,DO_Pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P)
        Spwd = Main.Data_owner.Validation(DO_ID,DO_Pw,user_ID,user_Pw,Server_ID,Server_Pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P)
        # data sharing in between Data owner and Attribute authority #
        Main.Data_owner.Data_Sharing(AA_ID,AA_Pw,DO_ID,DO_Pw,user_ID,user_Pw,Server_ID,Server_Pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data)
        Main.Data_owner.Download(DO_ID,DO_Pw,AA_ID,AA_Pw,user_ID,user_Pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data,Gen_key,Server_ID, Server_Pw)
    privacy=np.mean(priv)
    Norm_Var=np.mean(nv)
    Norm_V.append(Norm_Var)
    PRI.append(privacy)
    #return privacy,Norm_Var

