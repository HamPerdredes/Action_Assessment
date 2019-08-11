import numpy as np
from tools import cal_angle,trans_data
action_types=['tennis_front']
#用户选定动作类型，读取不同的模型进行分类
#考虑基于动作函数的变化去区分由一个步骤到另一个步骤的转变
#主要考虑对清晰拍摄到的帧，由其数据去对每一个部件拟合一个时序方程，并与标准动作得到的方程进行对比
def action_cut(file_string,action_type):
    data=[]
    with open(file_string,'r') as fp :
        while True :
            lines=fp.readline()
            if not lines :
                break
            tmp=[float(i) for i in lines.split()]
            data.append(tmp)
        data=np.array(data)
    frame_num=data.shape[0]
    eight_angs=trans_data(data)




action_cut('origin_data_0.txt',0)












