import asyncio
import httpx
import os
import platform
from time import perf_counter
from .res.arguments import *
from .res.urls import *
from main_imports import exception

if platform.system() == "Linux":
	from .res.lin_col import *
elif platform.system() == "Windows":
	from .res.win_col import *
else:
	from .res.lin_col import *

url_api = url["url_api"]
url2_api = url["url2_api"]

# failed = []


# http asyncronous check
def HAC_engine():
	async def check_recipe(proxy):
		outfile = ""
		failed = ""
		if os.path.exists(args.output):
			name, ext = os.path.splitext(args.output)
			outa = name + f"({{}})" + ext
			cnot = 1
			while os.path.exists(outa.format(cnot)):
				cnot += 1
			outfile += outa.format(cnot)
		else:
			outfile += args.output

		async with httpx.AsyncClient(proxies={"http:": f"http://{proxy}", "https:": f"http://{proxy}"}, follow_redirects=True) as client:
			try:
				res_http = await client.get(url_api, timeout=args.timeout)
				if res_http.status_code == 200:
					with open(outfile, "a") as out:
						out.write(proxy+"\n")
					print(f"{g}{proxy} success")
				else:
					print(f"{y}{proxy} "+str(res_http.status_code))
			except asyncio.exceptions.CancelledError:
				failed += proxy + "\n"
				print(f"{y}Process Canceled!")
				os._exit(1)
			except KeyboardInterrupt:
				print(f"{y}Process Stopped!")
				os._exit(1)
			except httpx.ConnectTimeout:
				# failed.append(proxy)
				failed += proxy + "\n"
				print(f"{r}ConnectionTimeOut")
			except httpx.ReadTimeout:
				# failed.append(proxy)
				failed += proxy + "\n"
				try:
					print(col(255, 77, 0, "ReadTimeout"))
				except:
					print(f"{lr}ReadTimeout")
			except httpx.ConnectError:
				# failed.append(proxy)
				failed += proxy + "\n"
				print(f"{r}ConnectionError")
			except httpx.ProxyError:
				failed += proxy + "\n"
				print(f"{r}Bad Request")
			except httpx.RemoteProtocolError:
				failed += proxy + "\n"
				try:
					print(col(255, 77, 0, "RemoteProtocolError"))
				except:
					print(f"{lr}RemoteProtocolError")
			except httpx.ReadError:
				failed += proxy + "\n"
				print(f"{r}ReadError")

		if failed != "":
			with open("failed.txt", "a") as f:
				f.write(failed)
		else:
			pass

	async def async_core():
		proxies = []
		with open(args.file) as f:
			for line in f:
				proxy = line.strip()
				proxies.append(proxy)
		tasks = [check_recipe(proxy) for proxy in proxies]
		await asyncio.gather(*tasks)

	s = perf_counter()
	asyncio.run(async_core())
	e = perf_counter()
	n = "{:.2f}".format(e-s)
	print(f"Time taken: {n}s")


def http_check():
	# Checker Function
	if args.file:
		if args.timeout:
			if args.output:
				HAC_engine()
	else:
		print(r+"Input Proxy File")
		print(exception)
