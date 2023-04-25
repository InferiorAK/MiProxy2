import os
import platform
import requests
import socket
import git
import shutil
from .res.arguments import *
from .res.lin_col import *
from .res.urls import *

if platform.system() == "Linux":
	from .res.lin_col import *
elif platform.system() == "Windows":
	from .res.win_col import *
else:
	from .res.lin_col import *

url_api = url["url_api"]
url2_api = url["url2_api"]


def gen():
	if args.count:
		if args.output:
			outfile = ""
			if os.path.exists(args.output):
				name, ext = os.path.splitext(args.output)
				outa = name + f"({{}})" + ext
				cnot = 1
				while os.path.exists(outa.format(cnot)):
					cnot += 1
				outfile += outa.format(cnot)
			else:
				outfile += args.output
			cnt = 0
			while cnt <= (args.count-1):
				cnt += 1
				ser = str(cnt)+". "
				ip = "{}.{}.{}.{}".format(
					*__import__('random').sample(range(0, 255), 4))
				if not ip.startswith("0.") and not "0.0.0" in ip:
					with open(outfile, "a") as out:
						out.write(ip+"\n")
						out.close()
						print(g+ser+ip)


def scrp():
	if args.output:
		api = args.api
		outfile = ""
		if os.path.exists(args.output):
			name, ext = os.path.splitext(args.output)
			outa = name + f"({{}})" + ext
			cnot = 1
			while os.path.exists(outa.format(cnot)):
				cnot += 1
			outfile += outa.format(cnot)
		else:
			outfile += args.output
		try:
			get_proxies = requests.get(api).text
			proxies = get_proxies.replace("\n", "")
			out = open(outfile, "w")
			out.write(proxies)
			out.close()
			print(g+get_proxies)
			print(g+"Proxy Scraped! Count=> " +
				  str(len(open(args.output, "r").readlines())))
		except KeyboardInterrupt:
			print(f"{y}Process Stopped!")
			os._exit(1)
		except requests.exceptions.ConnectionError:
			print(f"{r}ConnectionError")
		except requests.exceptions.MissingSchema:
			print(f"{r}Use http:// or https://")


def add_port():
	if args.port:
		if args.output:
			ip_file = open(args.file)
			outfile = ""
			if os.path.exists(args.output):
				name, ext = os.path.splitext(args.output)
				outa = name + f"({{}})" + ext
				cnot = 1
				while os.path.exists(outa.format(cnot)):
					cnot += 1
				outfile += outa.format(cnot)
			else:
				outfile += args.output
			port = str(args.port)
			cnt = 0
			for ip in ip_file:
				try:
					socket.inet_aton(ip)
					cnt += 1
					serial = str(cnt)+". "
					ip = ip.split("\n")[0]
					proxy = ip+":"+port
					with open(outfile, "a") as out:
						out.write(proxy+"\n")
					print(f"{g}{serial}{proxy}")
				except socket.error:
					print(r+"Invalid IP")


def upgrade():
	url = "https://github.com/InferiorAK/MiProxy2.git"
	local_dir = "../MiProxy2_new"
	if os.path.exists(local_dir):
		git.rmtree(local_dir)
		try:
			git.Repo.clone_from(url, local_dir)
			print(f"{g}Successfully Upgraded! Check /MiProxy2_new")
		except:
			print(f"{r}Error Upgrading!")
	else:
		try:
			git.Repo.clone_from(url, local_dir)
			print(f"{g}Successfully Upgraded! Check /MiProxy2_new")
		except:
			print(f"{r}Error Upgrading!")


def clean():
	try:
		shutil.rmtree("__pycache__")
	except FileNotFoundError:
		pass
	try:
		shutil.rmtree("core/__pycache__")
	except FileNotFoundError:
		pass
	try:
		shutil.rmtree("core/res/__pycache__")
	except FileNotFoundError:
		pass
