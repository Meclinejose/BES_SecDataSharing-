import Server
import User
def Registration_do(Client_ID,Client_Pw,V1,a,b,c,d,f):
    Server.Registration_do(Client_ID,Client_Pw,V1,a,b,c,d,f)
def Authentication(sg,MSP_ID,MSP_Pw,EP_ID,EP_Pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T):
    User.Authentication(sg,MSP_ID,MSP_Pw,EP_ID,EP_Pw,a,b,c,d,f,g,h,x,x1,x2,y1,y2,r,T)
    A1 = hash((int(EP_ID))+sg+T)
    return A1
