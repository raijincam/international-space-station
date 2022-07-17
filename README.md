24/06/2022

To use the venv_dashboard virtual env I found an error related to the window policies in order to solve it, you should press in the CLI the following commands:

Set-ExecutionPolicy Unrestricted -Scope currentUser Unrestricted
.\project_env\Scripts\activate