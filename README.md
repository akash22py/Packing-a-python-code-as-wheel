# Packing-a-python-code-as-wheel
1. requirement--> pip, python in your system
2. pip install setuptools, wheel
3. make a folder python_wheel_file
4. Inside this folder create another folder my_package
5. Inside my_package create file __init__.py and code file calculations.py
5. Inside python_wheel_file create setup.py
8. Open terminal at my_package and run $ python setup.py bdist_wheel
9. Install the whl file created in the dist folder by running command $ pip install dist\my_package-0.0.1-py3-none-any.whl   
10. Now you can import this package by importing my_package and any functions inside it in any .py files in your system.
