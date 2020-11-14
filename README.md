# kobo-annotations-exporter

Export your annotations from your Kobo device into files.
* Developer: Thomas Galvaing
* License: the MIT License (MIT)

## Install
Make sure you have Python3 and Pip on your machine then:

`pip install -r requirements.txt `

Plug you Kobo and localise the **sqlite file** (usually named **KoboReader.sqlite**)

## Usage

```bash
$ # print annotations in stdout
$ python kobo-annotations-exporter.py KoboReader.sqlite

$ # print annotations in docx files
$ python kobo-annotations-exporter.py KoboReader.sqlite --format word

$ # print annotations in text files
$ python kobo-annotations-exporter.py KoboReader.sqlite --format text

$ # change export directory
$ python kobo-annotations-exporter.py KoboReader.sqlite --directory export_directory

$ # print help
$ python kobo-annotations-exporter.py --help
````

## Contributions
This project is currently under development, feel free to contribute, report bugs or propose suggestions : any help is welcome ! 
I assume that the database structure is the same for all Kobo devices. Maybe it is not true, but I can't check. If your device is different from mine (Kobo Libra H2O), feel free to send me your **KoboReader.sqlite**. I would adapt my code if needed.
