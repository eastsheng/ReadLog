
import ReadLog as RLog
from pathlib import Path
import matplotlib.pyplot as plt
atm2mPa = 0.101325
if __name__ == '__main__':
	path = "./"
	logfile = "log_quenching_heavyoil.lammps"

	nf_log = 0 # The number of logs in logfile

	Path(path+"fig/").mkdir(parents=True,exist_ok=True)
	rl = RLog.ReadLog(path+logfile) 
	thermou_list,thermod_list = rl.ReadUD(path+logfile)
	print(thermou_list,thermod_list)
	pd_thermo = rl.ReadThermo(path+logfile,thermou_list,thermod_list,nf_log)

	average_p = sum(pd_thermo["Press"])/len(pd_thermo["Press"])
	p_txt = "Average Pressure="+str(round(average_p*atm2mPa,2))+" MPa"
	print(p_txt)

	average_t = sum(pd_thermo["Temp"])/len(pd_thermo["Temp"])
	t_txt = "Average Temperature="+str(round(average_t,2))+" K"
	print(t_txt)
	
	plt.rc('font', family='Times New Roman', size=22)
	fig = plt.figure(figsize=(12, 10))
	ax0 = fig.add_subplot(2,1,1)
	ax0.plot(pd_thermo["Step"],pd_thermo['Press']*atm2mPa,color='tab:blue',label="Pressure")
	plt.legend(loc="best")
	# ax0.set_xlim([0,10000])
	# ax0.set_ylim([-800,800])
	ax0.set_xlabel("Time(ps)")
	ax0.set_ylabel("Pressure(MPa)")
	ax0.grid(True)
	ax0.text(25, 550, p_txt, fontsize=20, va='bottom')

	ax1 = fig.add_subplot(2,1,2)
	ax1.plot(pd_thermo["Step"],pd_thermo['Temp'],color='tab:red',label="Temperature")
	plt.legend(loc="best")
	# ax1.set_xlim([0,10000])
	ax1.set_ylim([200,400])
	ax1.set_xlabel("Time(ps)")
	ax1.set_ylabel("Temperature(K)")
	ax1.grid(True)
	ax1.text(25, 350, t_txt, fontsize=20, va='bottom')
	
	# plt.savefig(path+"fig/PressTemp.png",dpi=300)
	plt.show()		