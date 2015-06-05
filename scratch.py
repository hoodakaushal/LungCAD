# __author__ = 'hooda'
#
# import os
# import paramiko
#
#
# def getFiles(path):
#     paths = [os.path.join(path, fn) for fn in next(os.walk(path))[1]]
#     files = []
#     for folder in paths:
#         files += [os.path.join(folder, fn) for fn in next(os.walk(folder))[2]]
#     files.sort()
#     return files
#
# def upoad():
#     hostAddress = 'ec2-52-25-102-252.us-west-2.compute.amazonaws.com'
#     userName = 'client_user'
#     userPassword = 'client_password'
#
#     paths = getFiles('/home/hooda/Code/Lungdata')
#
#     fpLimit = 1000
#     tpLimit = 800
#     fpDone = 0
#     tpDone = 0
#
#     i = 0
#     while (tpDone < tpLimit) and i < len(paths):
#         print i
#         cand = paths[i]
#         if os.path.basename(cand) == '1.3.6.1.4.1.9328.50.3.34596-TP-66-ACS-(-88x254x-541)-Dia_15.7427-Dens_3-Conf_4-ID_34559.mhd':
#             print("found the TP")
#         # if cand.find('-FP-') > -1 and fpDone < fpLimit:
#         #
#         #     print("found FP")
#         #     upload2(cand, hostAddress, userName, userPassword)
#         #     upload2(paths[i+1], hostAddress, userName, userPassword)
#             # fpDone += 1
#
#         if cand.find('-TP-') > -1 and tpDone < tpLimit:
#             print("found TP")
#             upload2(cand, hostAddress, userName, userPassword)
#             upload2(paths[i+1], hostAddress, userName, userPassword)
#             tpDone += 1
#         i += 2
#
#
# def upload2(source, host, user, passwd):
#     print("will upload", source)
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host, username=user, password=passwd)
#     ftp = ssh.open_sftp()
#
#     ftp.put(source, '/home/' + user + '/' + os.path.basename(source))
#
#
# upoad()


######################################################################################################################

