# CDSW Starter

A bare bones starter kit for data science projects in python using CDSW, with a minimal testing setup.

Directory structure:

```bash
cdsw-starter
├── .gitignore
├── Makefile
├── requirements.txt
├── README.md
├── experiments
│   └── README.md
├── jobs
│   └── README.md
├── models
│   └── README.md
└── module
    ├── __init__.py
    ├── code.py
    └── tests
        ├── __init__.py
        └── test_code.py
```

The requirements.txt file includes only `pytest`.
Run tests with `make test`.

The `module` directory and contents should be renamed to something appropriate to the work being done.