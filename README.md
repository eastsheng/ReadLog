## ReadLog

- A python code to read thermo info from lammps log file 

### Installation 

```bash
git clone https://github.com/eastsheng/ReadLog.git
cd ReadLog
python setup.py sdist
pip install .
```

### Requirements

- numpy
- pandas
- matplotlib

### Usage 

```python
import readlog as RLog
rl = RLog.ReadLog(logfile)
thermou_list,thermod_list = rl.ReadUD(path+logfile)
pd_thermo = rl.ReadThermo(path+logfile,thermou_list,thermod_list,nf_log)
step = pd_thermo["Step"]
P = pd_thermo["Press"]
T = pd_thermo["Temp"]
```

