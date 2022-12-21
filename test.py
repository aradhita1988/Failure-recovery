import os
import shutil
#os.chdir('C:\Users\User\Desktop')
source ="D:/dsg_single_faliure_recovery-dps_graph_2/src/mn"
destination = 'D:/dsg_single_faliure_recovery-dps_graph_2/src/nm'
# defining source and destination
# paths

f='requirements.txt'
src_path = os.path.join(source, f)

dst_path = os.path.join(destination, f)
#shutil.move(src_path, dst_path)
f1 = open(dst_path, 'a+')
f2 = open(src_path, 'r') 
f1.write(f2.read()) 
#shutil.copy2(src_path,dst_path )
#os.remove(src_path)


 
