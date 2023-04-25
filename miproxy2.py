# -*- coding: utf-8 -*-
#! /usr/bin/python3

__doc__ = """\n# 1st Release   :      25th April 2023 (GMT+6)
# MiProxy2      :      Proxy Tool Lvl-2
# Version       :      2.0
# Lisence       :      GPL 3.0
# Github		:      github.com/InferiorAK
# facebook		:      fb.com/InferiorAK
# Youtbe		:      youtube.com/@inferiorak
# twitter		:      twitter.com/@inferiorak

-------- Copyright (C) 2022 InferiorAK -------\n"""

import main_imports
from main_imports import *
from core import *


# Generate Random IP
if args.generate:
	others.gen()

# Scrape Proxies
elif args.scrape:
	if args.api:
		others.scrp()
	else:
		print(exception)

# upgrade tool
elif args.upgrade:
	others.upgrade()

# clean Cache
elif args.clean:
	others.clean()

# Check Proxy
elif args.check:
	if args.type == "http":  # check http
		httpck.http_check()
	elif args.type == "socks4":
		# socks4ck.socks4_check()
		print("I am Still Working on This")
	elif args.type == "socks5":
		# socks5sc.socks5_check()
		print("I am Still Working on This")
	else:
		print(exception)

# Add Port
elif args.add:
	if args.file:
		others.add_port()
	else:
		print(exception)

# Print Version
elif args.version:
	print(f"MiProxy2 {main_imports.__version__}")

else:
	print(__doc__)
	parser.print_help()
