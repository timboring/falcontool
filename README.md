Falcontool is an attempt to provide tooling for quickly and easily starting a Falcon-based project.
 
It is inspired by Django's `django-admin` and Flask's ` flask`.

# Requirements
The tool must do the following tasks:
- Create a project repository given a `project_name`
- Set up the basic project scaffolding, including:
  - Creating a skeleton `tox.ini` file
  - Creating a `tests` subdirectory
  - Creating a `src` subdirectory
  - Inside the `src` subdirectory, create:
    - An empty `api.py` file
  - Create a basic `requirements.txt` file in the root directory
  - Create an empty `README.md` file in the root directory
  - Create an empty `CODEOWNERS` file in the root directory
- Allow for the creation of additional resources if specified by flags:
  - `--dockerfile` creates an empty `Dockerfile` in the root directory
  - `--modelsfile` creates an empty `models.py` in `src/api` directory
  - `--dbfile` creates an empty `db.py` in `src/api` directory
  - `--resourcesfile` creates an empty `resources.py` in `src/api` directory
  
In addition to the above tasks, the tool should provide the following conveniences:
- Provide a command to startup a Python console where a user can experiment with the project
- Provide a command to run the projects test suite(s)