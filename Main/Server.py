import  AA
import owner


def Registration_do(do_id,do_pw,V1,a,b,c,d,f):
    AA.Registration_do(do_id, do_pw, V1, a, b, c, d, f)
def Registration_server(server_id,server_pw,a,b,c,d,f,g):
    OTP = hash(((int(server_id))+int(a))^g)

    g_ = OTP^(hash(int(server_id))+int(a))
    if(g==g_):
        '''print("server is registered with Attribute authority")'''
def Authentication(AA_id,AA_pw,server_id,server_pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T):
    sg = hash((int(AA_id))+int(b))//a
    A1 = owner.Authentication(sg, AA_id, AA_pw, server_id, server_pw, a, b, c, d, f, g, h, x, x1, x2, y1, y2, r, T)
    A1_ = hash((int(server_id))+sg+T)
    if(A1 == A1_):
        '''print("server is Authenticated with Attribute authority")'''

    return A1,sg



