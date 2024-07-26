California Median Housing Price Prediction
==========================================

![Python Version Badge][Python Version Badge]

Setup
-----

### Getting Source Code

```console
https://github.com/QubitPi/jupyter-notebooks.git
```

### Creating an Isolated Environment

It is strongly recommended to work in an isolated environment. Install virtualenv and create an isolated Python
environment by

```console
python3 -m pip install --user -U virtualenv
cd jupyter-notebooks
python3 -m virtualenv .venv
```

To activate this environment:

```console
source .venv/bin/activate
```

or, on Windows

```console
./venv\Scripts\activate
```

> [!TIP]
> 
> To deactivate this environment, use
> 
> ```console
> deactivate
> ```

### Installing Dependencies

```console
python3 -m pip install -U jupyter matplotlib numpy pandas scipy scikit-learn
```

If we created a virtualenv, we need to register it to Jupyter and give it a name:

```console
python3 -m ipykernel install --user --name=python3
```

### Starting Jupyter Server

Now we can fire up Jupyter by typing the following command:

```console
jupyter notebook
```

A Jupyter server is now running in our terminal, listening to port 8888. We can visit this server by opening our web
browser to http://localhost:8888/

Open up one of the [notebooks](./notebooks)

[Python Version Badge]: https://img.shields.io/badge/Python-3.10-brightgreen?style=for-the-badge&logo=python&logoColor=white
