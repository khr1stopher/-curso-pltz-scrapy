# Scrapy

is a frameworks to do webscraping and webscrawling, is an asynchronous framework to scrap

## installation
### MacOs

first of all u need to make a folder for the project, 

```bash
mkdir <folder-name>
xcode-select --install
xcode-select --reset
```

now we need to create a virtual enviroument

```bash
python3 -m venv venv
venv/bin/activate
```

and for the end we're gonna install autopep8 and scrapy
```bash
pip3 install autopep8 scrapy
```

scrapy version

```bash
scrapy version
```

and now is done

### Linux

first of all we need to install this libraries

```bash
sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```
create a folder

```bash
mkdir <folder-name>
```

now we need to create a virtual enviroument

```bash
python3 -m venv venv
venv/bin/activate
```

and for the end we're gonna install autopep8 and scrapy
```bash
pip3 install autopep8 scrapy
```

scrapy version
```bash
scrapy version
```

and now is done

### Windows
1. create a virtual enviroument
```bash
py -m venv venv
alias activate-entorno=source <path>/venv/Scripts/activate
> activate-entorno
```
2. install scrapy and autopep8
```bash
pip3 install autopep8 scrapy
```
3. verificar que se intallo scrapy
```bash
scrapy version
```

## Create a project with scrapy

```bash
scrapy startproject <name-project>
cd <name-project>
```

run the spider

```bash
scrapy crawl <spider-name>
```