"""
read lammps log file for some thermo data
"""
import numpy as np
import pandas as pd
# from pathlib import Path
import matplotlib.pyplot as plt

class ReadLog(object):
	"""docstring for ClassName"""
	def __init__(self, logfile):
		super(ReadLog, self).__init__()
		self.logfile = logfile

	def timeunit(self,x):
		x = x*1e-3 #fs2ps
		return x

	def ReadUD(self,LogFile):
		'''
		read line number of thermo info from logfile
		LogFile: LAMMPS log file
		'''
		with open(LogFile,"r",encoding="utf-8") as lf:
			thermou_list=[] # top number of line in thermo info 
			thermod_list=[] # bottom number of line in thermo info 
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

				self.tot_line_number = index

		# print(thermou_list,thermod_list)
		print("Tot number of line:",self.tot_line_number)
		for i in range(len(thermou_list)):
			try:
				print("Frame-"+str(i)+":","["+str(thermou_list[i])+",",str(thermod_list[i])+"]")
			except:
				print("Frame-"+str(i)+":","["+str(thermou_list[i])+", ~]")
				print("Your logfile is incomplete..., please check it.")

		return thermou_list,thermod_list

	def ReadThermo(self,LogFile,thermou_list,thermod_list,nf_log=0):
		L_u = len(thermou_list)
		L_d = len(thermod_list)

		for i in range(L_u):
			if i==L_u-1:
				n_line = self.tot_line_number-1-thermou_list[i]-1
			else:
				n_line = thermod_list[i]-thermou_list[i]-1
			if nf_log==i:
				thermo_col = np.loadtxt(LogFile,dtype="str",encoding='utf-8',skiprows=thermou_list[i]-1,max_rows=1)
				thermo_data = np.loadtxt(LogFile,skiprows=thermou_list[i],max_rows=n_line,encoding='utf-8')#.reshape((1,-1))
				pd_thermo = pd.DataFrame(thermo_data,columns=thermo_col)
			else:
				pass
		return pd_thermo

# if __name__ == '__main__':
# 	path = "./"
# 	logfile = "1_hydrate_dissociation_log.lammps"
# 	atm2mPa = 0.101325
# 	nf_log = 3 # The number of logs in logfile

# 	Path(path+"imgs/").mkdir(parents=True,exist_ok=True)
# 	rl = ReadLog(path+logfile) 
# 	print("*",20*"-","Reading frames of themo",20*"-","*")
# 	thermou_list,thermod_list = rl.ReadUD(path+logfile)
# 	pd_thermo = rl.ReadThermo(path+logfile,thermou_list,thermod_list,nf_log)
# 	print("Your label list of thermo :\n",pd_thermo.columns)
# 	print("*",20*"-","Reading END!!!!!!!!!!!!",20*"-","*")
# 	plt.rc('font', family='Times New Roman', size=22)
# 	fig = plt.figure(figsize=(12, 10))
# 	ax = fig.add_subplot(1,1,1)
# 	ax.plot(pd_thermo["Step"]*1e-3,pd_thermo['PotEng'],color='r',label="PotEng")
# 	plt.legend(loc="best")
# 	# ax.set_xlim([0,10000])
# 	# ax.set_ylim([-800,800])
# 	ax.set_xlabel("Time (ps)")
# 	ax.set_ylabel("PotEng (kcal/mol)")
# 	# ax.grid(True)
	
# 	# plt.savefig(path+"imgs/PressTemp.png",dpi=300)
# 	plt.show()		