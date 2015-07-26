hallie
===============================

[![Travis branch](https://img.shields.io/travis/joyent/node/v0.6.svg)]()

Like Siri, for the command line. Forgot a command? Tell Hallie and she'll try to help. Inspired by [betty](https://github.com/pickhardt/betty).

Install
--------
```
pip install hallie
```


Or you can build it yourself:
```
git clone "https://github.com/mikemelch/hallie"
cd hallie
python setup.py install
```

Enjoy!

Features
--------

* Many commands including ls, mkdir, man, whoami
* Unarchive most popular file types (including .zip, .tar, .gz, .rar, and many more)
* Copy / Paste
* Install pip packages (other packages managers to be implemented in the future)
* Get local or public IP address
* Open websites in your default browser


Mac Users
--------

* Play a particular song, artist, or album in iTunes
* Pause, resume, or skip the current song in iTunes
* Save a frequented directory with a nickname


Usage
--------
```
File Related

hallie show my files
hallie rename thisFile to thatFile
hallie remove thisFile
hallie create a directory called thisFolder
hallie teach me about ls
hallie extract thisArchive.tar.gz
hallie copy thisFile
hallie paste
hallie what is my name


User Related

hallie what is my public ip
hallie what is my local ip


iTunes Related (Mac Only)

hallie pause
hallie resume
hallie skip
hallie play <song> by <artist>
hallie play the album <album>
hallie play the artist <artist>


Directory Related (Mac Only)

hallie save as downloadFolder
hallie go to downloadFolder


Install Related

hallie install requests


Browser Related
hallie open google
hallie open thisWebSite
hallie open http://thisWebSite.com
```


