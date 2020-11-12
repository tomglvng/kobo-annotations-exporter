# kobo-annotations-exporter

Export your annotations from your Kobo in a more readeable format.
* Version: 1.0
* Date: 2020-11-11
* Developer: Thomas Galvaing
* License: the MIT License (MIT)

## Install
Make sure you have Python3 and Pip on your machine and:

`pip3 install -r requirements.txt `

Plug you Kobo and localise the **sqlite file** (usually named **KoboReader.sqlite**)

## Usage

```bash
$ # print annotations on stdout
$ python kobo-annotations-exporter.py KoboReader.sqlite

$ # print annotations on text files
$ python kobo-annotations-exporter.py KoboReader.sqlite --text

$ # print annotations on Microsoft Word files
$ python kobo-annotations-exporter.py KoboReader.sqlite --word

$ # change export directory
$ python kobo-annotations-exporter.py KoboReader.sqlite --directory export_directory

$ # print the help
$ python kobo-annotations-exporter.py --help