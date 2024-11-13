Jupyter Notebooks
=================

[![Notebooks badge]][Notebooks URL]
![Python Version Badge]
[![Apache License Badge]][Apache License, Version 2.0]

Setup
-----

### Getting Source Code

```console
https://github.com/QubitPi/jupyter-notebooks.git
```

### Navigating to A Notebook Directory

```console
cd jupyter-notebooks/notebooks
```

Each subdirectory in `notebooks` is a standalone Jupyter notebook. Choose and navigate into one of them. For example

```console
cd housing
```

### Creating an Isolated Environment

It is strongly recommended to work in an isolated environment. Install virtualenv and create an isolated Python
environment by

```console
python3 -m pip install --user -U virtualenv
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
pip3 install -r requirements.txt
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

License
-------

The use and distribution terms for [jupyter-notebooks]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[Notebooks badge]: https://img.shields.io/badge/Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white
[Notebooks URL]: https://jupyter-notebooks.qubitpi.org/

[Python Version Badge]: https://img.shields.io/badge/Python-3.10-FFD845?labelColor=498ABC&style=for-the-badge&logo=python&logoColor=white

