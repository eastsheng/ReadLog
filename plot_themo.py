import ReadLog as RLog
from pathlib import Path
import matplotlib.pyplot as plt

if __name__ == '__main__':
	path = "./"
	logfile = "1_hydrate_dissociation_log.lammps"
	atm2mPa = 0.101325
	nf_log = 3 # The number of logs in logfile

	Path(path+"imgs/").mkdir(parents=True,exist_ok=True)
	rl = RLog.ReadLog(path+logfile) 
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
	plt.show()	