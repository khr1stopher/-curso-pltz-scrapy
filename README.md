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

## Generadores e iteradores
note: `cuando no entiendas como funciona algo o siemplemente no encuentras la forma de que ese concepto pueda servirte busca ejemplos de aplicacion del mismo`
[When to use yield instead of return in Python?](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/)

## Scrapy Shell

```bash
scrapy shell "http://quotes.toscrape.com"

>>> response
<200 http://quotes.toscrape.com>

>>> response.xpath('//h1/a/text()') 
[<Selector query='//h1/a/text()' data='Quotes to Scrape'>]

>>> response.xpath('//h1/a/text()').get()
'Quotes to Scrape'

>>> response.xpath('//span[@class="text" and @itemprop="text"]/text()') 
[<Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“The world as we have created it is a...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“It is our choices, Harry, that show ...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“There are only two ways to live your...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“The person, be it gentleman or lady,...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“Imperfection is beauty, madness is g...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“Try not to become a man of success. ...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“It is better to be hated for what yo...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data="“I have not failed. I've just found 1...">, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“A woman is like a tea bag; you never...'>, <Selector query='//span[@class="text" and @itemprop="text"]/text()' data='“A day without sunshine is like, you ...'>]

>>> response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', '“It is our choices, Harry, that show what we 
truly are, far more than our abilities.”', '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a 
miracle.”', '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", '“Try not to become a man of success. Rather become a man of value.”', '“It is better to be hated for what you are than to be loved for what you are not.”', "“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", '“A day without sunshine is like, you know, night.”']

>>> request.encoding  
'utf-8'

>>> request.method  
'GET'

>>> request.headers
{b'Accept': [b'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'], b'Accept-Language': [b'en'], b'User-Agent': [b'Scrapy/2.9.0 (+https://scrapy.org)'], b'Accept-Encoding': [b'gzip, deflate']}

>>> request.body
[<all the html>]
```

## Estructura de carpetas Scrapy

- pipelines.py: permite modificar los datos desde que entran al spider (scripts que extraen información) hasta el final.
- middlewares.py: trabaja con un concepto denominado señales: controla eventos que suceden entre los requests y la captura de información.
- items.py: transforma los datos que se reciben del requests.
- _ init _.py: define que todos los archivos en la carpeta son un módulo de python.
- Folder spiders: en donde se crearan los scripts.
- settings.py: archivo con configuraciones del uso de Scrapy.

## Que es spiders?

Spider es una clase de python a la cual le decimos que informacion queremos, que informacion no queremos y como guardar esa informacion.