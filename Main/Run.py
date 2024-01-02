import Cloud_model
import Proposed_BES_SecDataSharing.run
import Cloudsim.Parameters
import time,psutil
import FL_BETS.run
import LSAA.run
import MMSDDF.run
import PRMS.run


def callmain(key_size,block_size):
    n_user=50
    start = time.time()
    Memory,Val_Time,Norm_Vari,Cond_priv=[],[],[],[]
    cpu, memory, bandwidth,freq,ID,User_Password,do_Pw,server_password,AA_Password,Data = Cloud_model.system_model(key_size, block_size, n_user)
    a, b, c, d, r, x, x1, x2, y1, y2, f, g, h = Cloudsim.Parameters.Initialization()
    # ------------------------- Proposed ---------------
    Proposed_BES_SecDataSharing.run.callmain(key_size, ID, User_Password, do_Pw, server_password, AA_Password, n_user, a, b, c, d, r, x, x1, x2, y1, y2, f, g, h, Data,Norm_Vari,Cond_priv)
    Val_Time.append(time.time() - start)
    mem = (psutil.virtual_memory()[2])
    Memory.append(mem)
    # --------------------- Comparative Method _____________________
    FL_BETS.run.callmain(key_size, ID, User_Password, do_Pw, server_password, AA_Password, n_user, a, b, c, d, r, x, x1, x2, y1, y2, f, g, h, Data,Norm_Vari,Cond_priv)
    Val_Time.append(time.time() - start)
    mem = (psutil.virtual_memory()[2])
    Memory.append(mem)


    LSAA.run.callmain(key_size, ID, User_Password, do_Pw, server_password, AA_Password, n_user, a, b, c, d, r, x, x1, x2, y1, y2, f, g, h, Data,Norm_Vari,Cond_priv)
    Val_Time.append(time.time() - start)
    mem = (psutil.virtual_memory()[2])
    Memory.append(mem)


    MMSDDF.run.callmain(key_size, ID, User_Password, do_Pw, server_password, AA_Password, n_user, a, b, c, d, r, x, x1, x2, y1, y2, f, g, h, Data,Norm_Vari,Cond_priv)
    Val_Time.append(time.time() - start)
    mem = (psutil.virtual_memory()[2])
    Memory.append(mem)


    PRMS.run.callmain(key_size, ID, User_Password, do_Pw, server_password, AA_Password, n_user, a, b, c, d, r, x, x1, x2, y1, y2, f, g, h, Data,Norm_Vari,Cond_priv)
    Val_Time.append(time.time() - start)
    mem = (psutil.virtual_memory()[2])
    Memory.append(mem)

    return Memory,Val_Time,Norm_Vari,Cond_priv



