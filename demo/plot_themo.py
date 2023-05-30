import readlog as RLog
from pathlib import Path
import matplotlib.pyplot as plt

if __name__ == '__main__':
	path = "./Pristine/"
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
	fig = plt.figure(figsize=(12, 8))
	ax = fig.add_subplot(1,1,1)
	x = pd_thermo["Step"]*1e-3
	y = pd_thermo['PotEng']
	ax.plot(x,y,color='r',label="PotEng")
	plt.legend(loc="best")
	# ax.set_xlim([0,10000])
	# ax.set_ylim([-800,800])
	ax.set_xlabel("Time (ps)",fontweight="bold",fontsize=26)
	ax.set_ylabel("PotEng (kcal/mol)",fontweight="bold",fontsize=26)
	# ax.grid(True)
	
	plt.savefig(path+"imgs/PotEng.png",dpi=300)
	plt.show()	