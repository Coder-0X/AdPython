# AdPython - Advanced Python Laboratory

Welcome to the **AdPython** repository! This project contains a comprehensive collection of Jupyter notebooks, scripts, and data files designed to help you master advanced Python concepts.

##  Project Structure

The course is organized into chapters, covering everything from environment setup to data handling and web scraping.

### **Chapter 1: Python Fundamentals & Advanced Concepts**
- **1.1 Setup**: Setting up Virtual Environments (env)
- **1.2 Lists**: Deep dive into Python lists
- **1.3 Advanced Data Structures**: Dictionaries, Sets, Tuples, and more
- **1.4 Functions**: Advanced function usage, decorators, and lambdas
- **1.5 Modules & Packages**: Creating and managing custom modules
- **1.6 Object-Oriented Programming (OOP)**: Classes, Inheritance, Polymorphism, and Advanced OOP (Magic Methods, Properties)
- **1.7 Exceptions & Debugging**: Error handling best practices
- **1.8 Advanced Concepts**: 
  - **Iterators & Generators**: Lazy evaluation and custom iteration
  - **Decorators**: Modifying functions, closures, and wrappers
  - **Context Managers**: Resource management with `with` statements

### **Chapter 2: Data Handling & External Integrations**
- **2.1 Structured & Unstructured Data**: Dealing with JSON, CSV, and Text files
- **2.2 Databases**: Relational vs. Non-Relational database interactions
- **2.3 Data from API**:
  - REST APIs (
equests library)
  - SOAP APIs (zeep library)
  - Authentication & Processing JSON/XML responses
- **2.4 Web Scraping**: Extracting data from websites with BeautifulSoup

##  Getting Started

### 1. Prerequisites
Ensure you have Python installed (3.8+ recommended). It is best practice to use a virtual environment.

### 2. Setup
First, clone the repository.

`ash
# Initialize and activate virtual environment

# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pandas requests zeep beautifulsoup4 lxml jupyter
`

### 3. Running the Notebooks
Launch Jupyter Notebook or use VS Code to open the .ipynb files in the class/ directory.

`ash
jupyter notebook
`

##  Key Libraries Used
- **pandas**: Data manipulation and analysis
- **requests**: HTTP library for API calls
- **zeep**: SOAP client for Python
- **beautifulsoup4**: Web scraping library
- **lxml**: XML/HTML processing

##  Notes
- **API Keys**: Some notebooks (e.g., etch_api.ipynb) require API keys (like OpenWeatherMap). You will need to sign up for free keys and replace the placeholders in the code.
- **Generated Files**: Some notebooks generate output files (e.g., 	odos.csv, ll_quotes.csv) during execution. These are ignored by git to keep the repository clean.
