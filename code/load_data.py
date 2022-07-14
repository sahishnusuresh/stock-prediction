import pickle
import networkx as nx
with open('/home/sahi/Desktop/psp_ad/PSP_AD/VG/Close/IVC.BO.pickle','rb') as ivsbograph:
    result=pickle.load(ivsbograph)
print(type(result))
G=nx.from_numpy_matrix(result['2021-10-06 '])
nx.draw(G)
print(G)