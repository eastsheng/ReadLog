# -*- coding: utf-8 -*-
"""
read lammps log file for some thermo data
"""
import numpy as np
import pandas as pd
# from pathlib import Path
import matplotlib.pyplot as plt

version = "1.2.1"

def print_readlog():
    cloud = [
	"                        _  _               ",
	" _ __   ___   __ _   __| || |  ___    __ _ ",
	"| '__| / _ \ / _` | / _` || | / _ \  / _` |",
	"| |   |  __/| (_| || (_| || || (_) || (_| |",
	"|_|    \___| \__,_| \__,_||_| \___/  \__, |",
	"                                     |___/ ",
    ]
    print("\n")
    print(22*"- ")
    print(22*". ")
    for line in cloud:
        print(line)
    print('@readlog-'+version,", Good Luck!")
    print(22*". ")
    print(22*"- ")
    return None

print_readlog()


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
		try:
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

		except:
			with open(LogFile,"r",encoding="gb18030") as lf:
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
				print("Warning: Your logfile is incomplete...\nPlease check it.")

		return thermou_list,thermod_list

	def ReadThermo(self,LogFile,thermou_list,thermod_list,nf_log=0):
		L_u = len(thermou_list)
		L_d = len(thermod_list)

		for i in range(L_u):
			if L_u == L_d:
				n_line = thermod_list[i]-thermou_list[i]-1
			elif L_u>L_d:
				if i==L_u-1:
					n_line = self.tot_line_number-1-thermou_list[i]-1
				else:
					n_line = thermod_list[i]-thermou_list[i]-1

			if nf_log==i:
				try:

					thermo_col = np.loadtxt(LogFile,dtype="str",encoding='utf-8',skiprows=thermou_list[i]-1,max_rows=1)
					thermo_data = np.loadtxt(LogFile,skiprows=thermou_list[i],max_rows=n_line,encoding='utf-8')#.reshape((1,-1))
				except:
					thermo_col = np.loadtxt(LogFile,dtype="str",encoding='gb18030',skiprows=thermou_list[i]-1,max_rows=1)
					thermo_data = np.loadtxt(LogFile,skiprows=thermou_list[i],max_rows=n_line,encoding='gb18030')#.reshape((1,-1))
					
				pd_thermo = pd.DataFrame(thermo_data,columns=thermo_col)
			else:
				pass
		return pd_thermo

	def ReadRunTime(self):
		LogFile=self.logfile
		with open(LogFile,"r",encoding="utf-8") as lf:
			for index, line in enumerate(lf,1):
				if "Total wall time" in line:
					isTTime = True
			try:
				if isTTime == True:
					print("\n-------------------------------\n")
					print("---", line)					
					print("-------------------------------\n")
			except:
				print("\n-------------------------------\n")
				print("Warning: No Total wall time in Your Logfile...\n\nPlease check it.")
				print("\n-------------------------------\n")
	
		return 


if __name__ == '__main__':
	path = "./"
	logfile = "log.lammps"
	# logfile = "log_incomplete.lammps"
	atm2mPa = 0.101325
	nf_log = 0 # The number of logs in logfile

	# Path(path+"imgs/").mkdir(parents=True,exist_ok=True)
	rl = ReadLog(path+logfile) 
	rl.ReadRunTime()

	"""
	print("*",20*"-","Reading frames of themo",20*"-","*")
	thermou_list,thermod_list = rl.ReadUD(path+logfile)
	pd_thermo = rl.ReadThermo(path+logfile,thermou_list,thermod_list,nf_log)
	print("Your label list of thermo :\n",pd_thermo.columns)
	print("*",20*"-","Reading END!!!!!!!!!!!!",20*"-","*")
	plt.rc('font', family='Times New Roman', size=22)
	fig = plt.figure(figsize=(12, 10))
	ax = fig.add_subplot(1,1,1)
	ax.plot(pd_thermo["Step"]*1e-3,pd_thermo['PotEng'],color='r',label="PotEng")
	plt.legend(loc="best")
	# ax.set_xlim([0,10000])
	# ax.set_ylim([-800,800])
	ax.set_xlabel("Time (ps)")
	ax.set_ylabel("PotEng (kcal/mol)")
	# ax.grid(True)
	
	# plt.savefig(path+"imgs/PressTemp.png",dpi=300)
	# plt.show()	
	"""	