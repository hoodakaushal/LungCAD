__author__ = 'ashutosh'

import os
import sys

# rnadom_output.py source
# python rnadom_output.py ~/Documents/Lungdata/1.3.12.2.1107.5.1.3.24061.2.0.409416063553031 list -FP-  ~/Documents

def main():
    source_folder = sys.argv[1]
    source_file_name = sys.argv[3]
    list_of_files = sys.argv[2]
    des_folder = sys.argv[4]
    f = open(list_of_files)
    print ("list opened")
    # os.system("mkdir " + des_folder)
    # print (des_folder+ " Directory made")
    if source_file_name.find("-FP-") > -1:
        i = 0
        for line in f:
            line = line[:-1]
            print line
            if line.find("-FP-") > -1:
                os.system(
                    "cp " + "\'" + source_folder + "/" + line + "\'" + " " + "\'" + des_folder + "/" + line + "\'")
                print "copied"
                i += 1
                if i == 20:
                    break

    if source_file_name.find("-TP-") > -1:
        i = 0
        for line in f:
            line = line[:-1]
            if line.find("-TP-") > -1:
                os.system(
                    "cp " + "\'" + source_folder + "/" + line + "\'" + " " + "\'" + des_folder + "/" + line + "\'")
                print "copied"
                i += 1
                if i == 20:
                    break
    print("Done")


main()
