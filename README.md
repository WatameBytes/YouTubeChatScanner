
# July Project - YouTube Chat Scanner/Chat Compute/Video Downloader/Clipper

I got a job as an Integration Engineer and want to keep my programming skills sharp. I plan to work on a big project every month.

While I was clipping some VTuber as a hobby. I thought "Could I automate this?"


## Documentation

[Documentation](https://linktodocumentation)


## Features

- Scan an archived YouTube livestream chat to get frequency of comments
- Download YouTube videos
- Compute chat data
- Clip your video based off chat data


## Requirements

To run this project, you will need:

`FFMPEG` You will need to edit environment variables and edit Path under System variables to point to FFMPEG

C:\Users\<User>\AppData\Local\Programs\Python\Python39\Scripts

`Install modules from the requirements.txt` pip install -r requirements.txt



## Run Locally

Clone the project

```bash
  git clone https://github.com/ArisaBonsaiTree/YouTubeChatScannerJulyProject.git
```

Go to the project directory

```bash
  cd YouTubeChatScannerJulyProject
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the program

```bash
  python MainProgram.py 
```


## FAQ

#### Question 1: FFMPEG Errors?

Make sure to download [FFMPEG](https://ffmpeg.org/) and add it to your environment variables

#### Module issues?

pip install -r requirements.txt

#### How to pin the Python file to my taskbar 

https://www.tenforums.com/tutorials/96525-pin-file-taskbar-windows-10-a.html

#### "Python" is not a recognized command

Do you have [Python](https://www.python.org/downloads/) installed?

#### What Operating Systems does this program run in?

Developed this using PyCharm on Windows 10

#### Does PyInstaller Work?

I used PyInstaller. File > Tools > External Tools

![image](https://user-images.githubusercontent.com/64375555/179183895-de1b1d5e-0bae-45c6-a86f-40e8687bdcca.png)

## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
