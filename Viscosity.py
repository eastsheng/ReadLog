
import ReadLog as RLog
from pathlib import Path
import matplotlib.pyplot as plt
atm2mPa = 0.101325
if __name__ == '__main__':
	path = "./"
	logfile = "log_quenching_heavyoil.lammps"
	# logfile = "output.txt"

	Path(path+"fig/").mkdir(parents=True,exist_ok=True)
	rl = RLog.ReadLog(path+logfile) 
	thermou_list,thermod_list = rl.ReadUD(path+logfile)
	pd_thermo = rl.ReadThermo(path+logfile,thermou_list,thermod_list,2)

	# pd_thermo["Step"] = pd_thermo["Step"]*1e-3
	# print(pd_thermo)
	pd_thermo["Step"] = pd_thermo.apply(lambda x: rl.timeunit(x))
	print(pd_thermo)
	# print(pd_thermo["Step"])
	average_viscosity = abs(pd_thermo["v_v11"]+pd_thermo["v_v22"]+pd_thermo["v_v33"])/3
	plt.rc('font', family='Times New Roman', size=22)
	fig = plt.figure(figsize=(12, 8))
	ax0 = fig.add_subplot(1,1,1)
	ax0.plot(pd_thermo["Step"],average_viscosity*1e3,color='tab:blue',label="Viscosity",linewidth=2)
	plt.legend(loc="best")
	ax0.set_xlim(0,)
	ax0.set_ylim(0,)
	ax0.set_xlabel("Time(ps)")
	ax0.set_ylabel("Viscosity(mPa.s)")
	ax0.grid(True)
	# plt.savefig(path+"fig/PressTemp.png",dpi=300)
	plt.show()