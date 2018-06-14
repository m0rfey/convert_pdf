# Программа для конверирование отсканированых PDF файлов
Python version >= 3
```sh
$ git clone https://github.com/maximchuk/convert_pdf.git
```

### Ubuntu:
```sh
$ sudo apt install python3-venv
$ cd conver_pdf/
$ pyvenv .venv
$ source .venv/bin/activate
$ (.venv)/ pip install -r requirements.txt
$ sudo cp -r teseractTestdata/* /usr/share/tesseract-ocr/tessdata
```


### Windows:

https://github.com/tesseract-ocr/tesseract/wiki/Downloads

### MacOs:

https://github.com/tesseract-ocr/tesseract/wiki
