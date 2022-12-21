import csv
import os
import shutil

with open('D:/dsg_single_faliure_recovery-dps_graph_2/data/test.csv','r') as csvinput:
     reader = csv.reader(csvinput)
     all = []
     row = next(reader)
     all.append(row)
     for row in reader:
         
         source ='D:/dsg_single_faliure_recovery-dps_graph_2/src/'
         destination = 'D:/dsg_single_faliure_recovery-dps_graph_2/src/'
         f=row[2]+"/"+row[0]+".txt"
         f1=row[1]+"/"+row[0]+".txt"
         src_path = os.path.join(source, f)
         dst_path = os.path.join(destination, f1)
         if  not os.path.exists(dst_path):
             print("hi")
             shutil.copy2(src_path,dst_path )
         else:
              f1 = open(dst_path, 'a+')
              f2 = open(src_path, 'r') 
              f1.write(f2.read()) 
csvinput.close();         
with open('D:/dsg_single_faliure_recovery-dps_graph_2/data/sample.csv','r') as csvinput:
     reader = csv.reader(csvinput) 
     row = next(reader)  
     for row in reader:
         source ='D:/dsg_single_faliure_recovery-dps_graph_2/src/'
         f=row[1]+"/"+row[0]+".txt"  
         src_path = os.path.join(source, f)  
         #os.remove(src_path)
         f = open(src_path, "r+")
         f.seek(0) 
         f.truncate()  
  
# absolute file positioning
        
  
# to erase all data 
