"""
read lammps log file for some thermo data
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import re
from pathlib import Path

class ReadLog(object):
	"""docstring for ClassName"""
	def __init__(self, logfile):
		super(ReadLog, self).__init__()
		self.logfile = logfile
		
	def timeunit(self,x):
		x = x*1e-3 #fs2ps
		return x

	def ReadUD(self,LogFile,):
		'''从lammps中读取thermo的数据'''
		with open(LogFile,"r",encoding="utf-8") as lf:
			thermou_list=[]
			thermod_list=[]
			for index, line in enumerate(lf,1):
				# print(line)
				if "Per MPI rank memory allocation" in line:
					# print(line)
					thermou = index+1
					thermou_list.append(thermou)
				if "Loop time of " in line:
					# print(line)
					thermod = index
					thermod_list.append(thermod)

		print(thermou_list,thermod_list)

		print("Total",len(thermou_list),",",len(thermod_list))

		return thermou_list,thermod_list

	def ReadThermo(self,LogFile,thermou_list,thermod_list,plot_factor=0):
		L_u = len(thermou_list)
		L_d = len(thermod_list)
		if L_u == L_d:
			for i in range(L_u):	
				n_line = thermod_list[i]-thermou_list[i]-1
				# print(thermou_list[i],thermod_list[i],n_line)
				if plot_factor==i:
					thermo_col = np.loadtxt(LogFile,dtype="str",encoding='utf-8',
						skiprows=thermou_list[i]-1,max_rows=1)
					thermo_data = np.loadtxt(LogFile,skiprows=thermou_list[i],max_rows=n_line,encoding='utf-8')#.reshape((1,-1))
					# print(thermo_col)
					# print(thermo_data)
					# thermo_ind = thermo_data[:,0]
					# pd_thermo = pd.DataFrame(thermo_data,columns=thermo_col,index=thermo_ind)
					# pd_thermo = pd_thermo.drop(columns=["Step"],axis=1)
					pd_thermo = pd.DataFrame(thermo_data,columns=thermo_col)
					print(pd_thermo)
				else:
					pass
		else:
			for i in range(L_d):	
				n_line = thermod_list[i]-thermou_list[i]-1
				# print(thermou_list[i],thermod_list[i],n_line)
				if plot_factor==i:
					thermo_col = np.loadtxt(LogFile,dtype="str",
						skiprows=thermou_list[i]-1,max_rows=1)
					thermo_data = np.loadtxt(LogFile,skiprows=thermou_list[i],max_rows=n_line).reshape((1,-1))
					# print(thermo_col)
					# print(thermo_data)
					# thermo_ind = thermo_data[:,0]
					# pd_thermo = pd.DataFrame(thermo_data,columns=thermo_col,index=thermo_ind)
					# pd_thermo = pd_thermo.drop(columns=["Step"],axis=1)
					pd_thermo = pd.DataFrame(thermo_data,columns=thermo_col)
					print(pd_thermo)
				else:
					pass
			print("Your the long of thermo_list is not equal ... ")
			print("ERROR! Please check the number of thermou_list and thermod_list ... ")
		return pd_thermo

