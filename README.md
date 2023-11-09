# Project Name: gutenberg-botany-spider
Scrapy spider that scrapes project gutenberg for ebooks from the search term [botany](https://www.gutenberg.org/ebooks/search/?query=botany&submit_search=Go%21). 


## Setting Up

This project uses Python 3.7+ Follow these steps to setup your Python environment.

### Creating a Virtual Environment

Python3 comes with built-in support for virtual environments (via the venv module). You can create a virtual environment using the following command:

```bash
python3 -m venv env
```

### Activating the Virtual Environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific `python` and `pip` executables into your shell’s `PATH`.

On macOS and Linux:

```bash
source env/bin/activate
```

On Windows:

```bash
.\env\Scripts\activate
```

You’ll know your virtual environment is activated once the name of it shows up on the left side of the terminal line (e.g. `(env)`).

### Installing Dependencies

Once you've activated your virtual environment, you can install the project dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Running the Project
You can modify this to suite your needs, however this worked for me.

```bash
scrapy crawl gutenberg-botany-spider -o gutenberg-botany-spider.csv -L DEBUG
```
I'm using [icecream](https://github.com/gruns/icecream) for simple debugging. 

# License 
No license, whatever python and scrapy is. 