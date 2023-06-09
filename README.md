# MiProxy2
<b>Python Asyncronous Proxy Checker</b>

<p>
  <img src="https://user-images.githubusercontent.com/114951279/234237457-27830948-e939-45bb-9a51-0d27ef57df59.jpg">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-green?style=for-the-badge">
  <img src="https://img.shields.io/github/license/inferiorak/MiProxy2?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/inferiorak/MiProxy2?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/inferiorak/MiProxy2?color=red&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/inferiorak/MiProxy2?color=teal&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-InferiorAK-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python3.11.1-darkcyan?style=flat-square">
  <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Finferiorak%2FMiProxy2&title=Visitors&edge_flat=false"/></a>
</p>

<br>

## Tutorial
<a href="https://youtu.be/ihSmcZDU_x0" target=_blank>**click here**</a>

## Features

- Proxy Scraper
- IP Generator
- Proxy Validator
- Add Port to IP file
## New Features Added (LVL-2)
- Asyncronous HTTP Check
- Upgrade Tool
- Clean Cache


<br>

## Support on

- Termux
- Linux
- Windows

<br>

<br>

## Contact Me
<a href="https://github.com/InferiorAK"><img align="left" title="Github" alt="Github" width="30px" src="assets/github.png" /></a>
<a href="https://fb.com/InferiorAK"><img align="left" title="Facebook" alt="Facebook" width="30px" src="assets/facebook.png" /></a>
<a href="https://m.me/InferiorAK"><img align="left" title="Messenger" alt="Messenger" width="30px" src="assets/messenger.png" /></a>
<a href="https://youtube.com/@InferiorAK"><img align="left" title="Youtube" alt="Youtube" width="43px" src="assets/youtube.png" /></a>
<a href="https://twitter.com/InferiorAK"><img align="left" title="Twitter" alt="Twitter" width="40px" src="assets/twitter.png" /></a>

<br>

## Installation

- Clone this repository -
  ```
  git clone https://github.com/inferiorak/MiProxy2
  ```

- Now go to cloned directory -
  ```
  $ cd MiProxy2
  $ pip3 install -r requirements.txt
  $ clear
  $ python3 miproxy2.py
  ```
  
 ## Overview
 
 ```
 root@kali:~$ python3 miproxy.py -h
usage: miproxy2.py [options]

Proxy Tool by InferiorAK

options:
  -h, --help            show this help message and exit
  -f [FILE], --file [FILE]
                        Proxy File
  -o [OUTPUT], --output [OUTPUT]
                        Output File
  -p [PORT], --port [PORT]
                        Set Port/Target Port
  --type [http/socks4/socks5]
                        Set Proxy Type
  -t [TIMEOUT], --timeout [TIMEOUT]
                        Set Timeout
  --upgrade             Upgrade Tool
  --clean               Clean pycache
  -v, --version         Print Version

Generate Random IP:
  Usage: python miproxy2.py --generate --count [LOOP_COUNT] -o [out.ext]

  -g, --generate        Generate IP (Mode)
  -c [LOOP_COUNT], --count [LOOP_COUNT]
                        Amount of IP

Scrape Proxies:
  Usage: python miproxy2.py --scrape -api [API_LINK] -o [out.ext]

  -sc, --scrape         Scrape Proxies with API (Mode)
  -api [API_LINK]       Paste your api

Check Proxies:
  Usage: python miproxy2.py --check -f [proxies.txt] --type [http/socks4/socks5] -t [second] -o [out.ext] --all

  --check               Check Proxies (Mode)

Add Port:
  Usage: python miproxy2.py --add -f [ip_file.txt] -p [port] -o [out.ext]

  --add                 Add Port to IP (Mode)
```

