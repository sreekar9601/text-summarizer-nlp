import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

#CI/CD will install local package - which will require the init file - core components for an end to end project
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
#to handle different OS file directory formats
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)# splits file directory and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")


    if(not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):#create file if not existing
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"file already exists:{filename}")


