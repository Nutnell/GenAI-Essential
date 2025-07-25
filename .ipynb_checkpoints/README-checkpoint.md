#Environment Setup

```bash
conda create --name project1 python=3.13.5 -y
```

```bash
conda activate project1
```

```bash
conda install -c conda-forge pandas
```

```bash
pip install -r requirements.txt
```

If you get a missing module error trying to run jupyter, try 
```bash
conda install -c conda-forge ipykernel
```

```bash
conda install -c conda-forge jupyterlab
```

```bash
jupyter lab --no-browser --allow-root --ip 0.0.0.0
```