import os
import signal
import sys
import shutil
import datetime
import in_place
import time
import fileinput
import csv
process_id = None
node_id = None
f_cache = None

re = sys.argv[1]
print("Node to kill -> ", re)
source ='D:/dsg_single_faliure_recovery-dps_graph_2/src/'
destination = 'D:/dsg_single_faliure_recovery-dps_graph_2/src/'
#f=row[1]+"/"+re+".txt"
#re=str(0)
with open('D:/dsg_single_faliure_recovery-dps_graph_2/data/test.csv','r') as csvinput:
     reader = csv.reader(csvinput)

     row = next(reader)
     flag=0
     for row in reader:
         if row[0]==re:
            f=row[1]+"/"+re+".txt"
            f1=row[2]+"/"+re+".txt"
            
            src_path = os.path.join(source, f)
            src_path1 = os.path.join(source, f1)
            if  not os.path.exists(src_path1) and os.path.exists(src_path):
                shutil.copy2(src_path,src_path1)
                print(src_path)
              
           
           #f1=row[2]+"/"+re+".txt"
           
         #dst_path = os.path.join(destination, f1)
         
         #print(dst_path)
         #shutil.copy2(src_path,dst_path )
csvinput.close();         
