# Interview exercise
1. Create a feature branch named `feature/interview`.
2. Implement `print_directory_contents` in `main.py`
3. Complete the Dockerfile such that the resulting image runs `main.py`
4. Implement `build_and_run.sh`
5. Implement `check_password_strength` in `main.py` using the python module `requests`
You can use the following commands to create a virtual environment so that modules can be installed and `main.py` can be run locally:
```
virtualenv --python="$(which python)" venv
source venv/bin/activate
# Use pip, etc.
python main.py
```
6. Enhance the Dockerfile so that it installs the module `requests`