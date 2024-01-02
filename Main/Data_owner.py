import User
def Registration_do(do_id,do_pw,V1,a,b,c,d,f):
    V2 = User.Registration_do(do_id, do_pw, V1, a, b, c, d, f)
    return V2
def Authentication(sg,AA_id,AA_pw,server_id,server_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T):
    return sg

def Authentication_(do_id,do_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1):
    A3 = (hash(int(do_id))+Sg+int(a))//(int(r)+T)
    User.Authentication__(do_id, do_pw, Sg, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, A3)
    return A3
def Data_Access_control(C,do_id,do_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,TSC,P):
    C_ = (hash(TSC)+int(a))//int(P)
    if(C==C_):
        AC = C*hash(int(do_id)+int(d)+int(b))
        return AC
def Validation(do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P):
    Spwd = User.Validation(do_id, do_pw, user_id, user_pw, server_id, server_pw, Sg, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, P)
    return Spwd
def Validation_(Spwd,do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P):
    U = 0
    for j in range(len(do_pw)):
        U += ord(do_pw[j])
    S = hash(Spwd ^ U)
    return S

def Data_Sharing(AA_id,AA_pw,do_id,do_pw,user_id,user_pw,server_id,server_pw,Sg,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data):
    User.Data_sharing(AA_id, AA_pw, do_id, do_pw, user_id, user_pw, server_id, server_pw, Sg, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, P, De_Data)
def Download(do_id,do_pw,AA_id,AA_pw,user_id,user_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T,A1,P,De_Data,K,server_id, server_pw):
    User.Download(do_id, do_pw, AA_id, AA_pw, user_id, user_pw, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T, A1, P, De_Data, K, server_id, server_pw)
def Download_(Dh):
    return Dh