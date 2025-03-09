# Installation / Setup

If you plan to contribute to this repo, set up your environment by running the following command:

```bash
pip install pre-commit
make setup
```

To simply install and use this repo, run the following command:
```bash
make install
```

# Helpful commands

| Bash command | Description |
|     :---:      | :---         |
| `make install` | Install/update the local library and associated dependencies |
| `make setup` | Install/update the pre-commit hooks for local development<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>(pre-commit must be installed already)</i> |
| `make lint`   |  Lint python source files  |
| `make format`   | Auto-format python source files<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>(applies changes `make lint` described in)</i> |
| `make test`	| Run all testing code	|
| `make clean`   | Clear local caches and build artifacts    |
| `make .pre-commit` | Check that pre-commit is installed |
| `make .pytest` | Check that pytest is installed |
| `make .ruff`   |  Check that ruff is installed  |
| `make .yapf`   | Check that yapf is installed |
| `make clean`   | Clear local caches and build artifacts    |
| `make help` | Display this table<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>(sorted A-Z)</i> |
