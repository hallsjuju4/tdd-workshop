# tdd-workshop
Test-Driven Development (TDD) Workshop materials

Welcome to the Test-Driven Development (TDD) Workshop! We will spend a couple 
hours together learning about TDD and applying it to simple Python programs.

This course assumes basic knowledge of programming in Python, but not much else!

# Environment Setup
## System Requirements
Some prerequisites for your system:
*   No longer requires Linux, see https://github.com/supernaut11/tdd-workshop.git for the Linux version
*   Python 3 (samples in course use Python 3.8)
*   IDE of your choosing (e.g., PyCharm, VS Code, Sublime, Atom)

## Pre-Workshop Setup
1.  Download this repository to your local system. Here are a couple ways you 
    can do that:

    Using git:

        git clone https://github.com/hallsjuju4/tdd-workshop.git
    
2.  Create python venv folder for this project

        cd tdd-workshop
        python -m venv venv
      
3.  Make sure the Python virtual environment is behaving as expected

        .\venv\Scripts\activate.bat

    This should result in a string (venv) appearing before your shell prompt.
    Make sure that the Python modules we need are installed:

4.  Install pytest and pytest coverage

        pip install pytest
        pip install pytest-cov
        python -m pytest --version
    
    Should report something like:

        This is pytest version 5.4.3, imported from <some path>
        setuptools registered plugins:
          pytest-cov-2.10.0 at <some path>

5.  Setup your IDE to use this new venv for this project.