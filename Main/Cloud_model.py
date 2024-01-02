import Cloudsim.Run


def system_model(ks,bs,n_users):

    cpu, memory, bandwidth,freq,ID,User_Password,do_Pw,server_password,AA_Password,Data = Cloudsim.Run.cloud_sim(ks,bs, n_users)  # cpu, memory, bandwidth, frequency


    return cpu, memory, bandwidth,freq,ID,User_Password,do_Pw,server_password,AA_Password,Data