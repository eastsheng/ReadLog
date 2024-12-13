# -*- coding: utf-8 -*-
"""
read lammps log file for some thermo data
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
from pathlib import Path
import logging
import sys

def __version__():
	version = "1.2.3"
	return version

def print_readlog():
    cloud = [
	" _ __   ___   __ _   __| || |  ___    __ _ ",
	"| '__| / _ \ / _` | / _` || | / _ \  / _` |",
	"| |   |  __/| (_| || (_| || || (_) || (_| |",
	"|_|    \___| \__,_| \__,_||_| \___/  \__, |",
	"                                     |___/ ",
    ]
    print(22*"- ")
    print(22*"..")
    for line in cloud:
        print(line)
    version = __version__()
    print('@readlog-'+version,", Good Luck!")
    print(22*"..")
    print(22*"- ")
    return None

print_readlog()

def print_line(func):
    
    def wrapper(*args, **kwargs):
        print(21*"-","ReadLog Start ",21*"-")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(20*"-","Run time:",round(elapsed_time,2),"s ",20*"-")
        return result
    return wrapper

class ReadLog(object):
	"""
	docstring for ReadLog
	read thermo info from lammps logfile;
	a instantiation: 	
		rl = ReadLog(logfilename)
		pd_thermo = rl.ReadThermo(0)
	"""
	def __init__(self, logfile):
		"""
		logfile: log file name
		"""
		super(ReadLog, self).__init__()
		self.logfile = logfile

	def ReadUD(self):
		'''
		read line number of thermo info from logfile, return thermou_list,thermod_list
		'''
		LogFile = self.logfile
		try:
			with open(self.logfile,"r",encoding="utf-8") as lf:
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
	
	@print_line
	def ReadThermo(self,nf_log=0):
		"""
		read thermo from logfile, return pd_thermo
		nf_log: number of thermo frames in log file, default nf_log = 0
		"""
		thermou_list,thermod_list = self.ReadUD()
		L_u = len(thermou_list)
		L_d = len(thermod_list)
		LogFile = self.logfile
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
	
	@print_line
	def ReadRunTime(self):
		"""
		read Total Run Time from logfile
		"""
		LogFile=self.logfile
		with open(LogFile,"r",encoding="utf-8") as lf:
			for index, line in enumerate(lf,1):
				if "Total wall time" in line:
					isTTime = True
			try:
				if isTTime == True:
					print("\n"+line)					
			except:
				print("Warning: No 'Total wall time' in Your Logfile...\n\nPlease check it.")
	
		return 

	@print_line
	def ReadTimestep(self):
		"""
		read Time step from logfile, return time_step
		"""
		LogFile=self.logfile
		with open(LogFile,"r",encoding="utf-8") as lf:
			have_timestep=[]
			for index, line in enumerate(lf,1):
				if "timestep" in line:
					have_timestep.append(line)

		for ht in have_timestep:
			if "${" in ht or "}" in ht or "reset_" in ht or "Performance" in ht or "variable" in ht:
				pass
			else:
				try:
					# print(ht)
					time_step = int(ht.strip().split()[1])
					print("Time step =",time_step)
					return time_step
				except:
					print("Warning: No 'timestep' in Your Logfile...\n\nPlease check it.")
					return None





class Tee:
	def __init__(self, *files):
		self.files = files

	def write(self, obj):
		for f in self.files:
			f.write(obj)

	def flush(self):
		for f in self.files:
			f.flush()

def print_log(log_file_name):
	current_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
	log_file_name = f"{log_file_name}"
	logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
	log_file = open(log_file_name, 'a')
	sys.stdout = Tee(sys.stdout, log_file)
	print("-"*100)
	print("-"*100)
	print(f">>> Date and Time: {current_time}")
	print(f">>> logfile name: {log_file_name}")
	print("-"*100)
	print("-"*100)
	return





if __name__ == '__main__':

	logfile = "1_hydrate_dissociation_log.lammps"
	nf_log = 0 # The number of logs in logfile
	rl = ReadLog(logfile) 
	rl.ReadThermo(nf_log)
	rl.ReadRunTime()
	rl.ReadTimestep()
