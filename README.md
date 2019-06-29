# create / update the development environment

```bash
ceny -ay
```


# create the documentation for a service based on sanicbaseservice

```bash
ceny -ay
conda activate <ENV_NAME>
create_docu
```


# create the conda package
Please ensure to add a git tag (using semantic versioning style) for the
current version of the scwoaservices.
Then create the package using:
```bash
conda build . --python=3.7
```
