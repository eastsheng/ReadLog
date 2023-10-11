## readlog

- A python code to read thermo info from the log file of LAMMPS output

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

- 2023-10-11: v1.2.2
  - [x] a great modification
- 2023-09-16: v1.2.1
  - [x] Fixed `UnicodeDecodeError: 'utf-8' codec can't decode` problem.
- 2023-06-20: v1.2.0

  - [x] Fixed a read error in the complete message frame under incomplete message;

  - [x] add `print_readlog` function;

  - [x] add `ReadRunTime`function.



