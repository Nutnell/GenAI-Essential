#Environment Setup

##Create an environment

```bash
conda create --name project1 python=3.13.5 -y
```

##Activate the environment

```bash
conda activate project1
```

##Install the requirements

```bash
conda install -c conda-forge pandas
```

```bash
pip install -r requirements.txt
```

##jupyter notebook necessities

If you get a missing module error trying to run jupyter, try 
```bash
conda install -c conda-forge ipykernel
```

##Install jupyterlab

```bash
conda install -c conda-forge jupyterlab
```

##Install jupyterlab extensions

```bash
conda install -c conda-forge jupyterlab-git
```

```bash
conda install -c conda-forge catppuccin-jupyterlab
```

##Run jupyterlab

```bash
jupyter lab --no-browser --allow-root --ip 0.0.0.0
```