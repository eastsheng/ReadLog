## ReadLog

- A python code to read thermo info from lammps log file 

### Installation 

```bash
git clone https://github.com/eastsheng/readlog.git
cd readlog
pip install .
# or
pip install readlog
```

### Requirements

- numpy
- pandas
- matplotlib

### Usage 

- run `plot_themo.py` in `demo` folder:

  ```bash
  python plot_thermo.py
  ```

- out:
- ![](./demo/imgs/PotEng.png)



### Fixed

- [x] Adapting to incomplete thermo information.

  

