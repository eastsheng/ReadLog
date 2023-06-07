## ReadLog

- A python code to read thermo info from the log file of lammps output

### Installation 

```bash
git clone https://github.com/eastsheng/readlog.git
cd readlog
pip install .
# or
pip install readlog
pip install readlog -i https://pypi.org/simple
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

- [x] Fixed a read error in the complete message frame under incomplete message



