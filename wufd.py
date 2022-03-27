# WUFD.py
# WGET clone in python for windows

import sys
import cgi
import requests
from tqdm import tqdm

url = sys.argv[1]
buf_size = 1024
response = requests.get(url, stream=True)
file_size = int(response.headers.get("Content-Length", 0))
default_name = url.split("/")[-1]
content_disp = response.headers.get("Content-Disposition")

if content_disp:
	value, params = cgi.parse_header(content_disp)
	filename = params.get("filename", default_name)
	
else:
	filename = default_name
	
progress = tqdm(response.iter_content(buf_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as content:
	for data in progress.iterable:
		content.write(data)
		progress.update(len(data))
