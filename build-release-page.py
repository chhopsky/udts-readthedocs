from os import walk
import os
import requests

token = os.environ.get('DEPLOYMENT')
if token:
    foldername = "website/builds/development"
else:
    foldername = "../chhopsky.github.io/builds/development"

try:
    response = requests.get("https://api.github.com/repos/chhopsky/updatethestream/releases")
    data = response.json()
except:
    pass

results = {}

for release in data:
    if release["tag_name"] != "v0.1-alpha":
        results[release["tag_name"]] = {}
        assets = release.get("assets")
        for asset in assets:
            results[release["tag_name"]][asset["name"]] = asset["browser_download_url"]

output = """
Release Downloads
=================

Public releases have been tested and approved for release. Development builds are the latest check-ins from our development branch; use at your own risk.

Public Releases
-----------------\n"""

for key, value in results.items():
    output += f"**{key}**\n\n"
    for key2, value2 in value.items():
        output += f"- `{key2} <{value2}>`_\n"
    output += f"\n\n"

output += """
Development Builds (unstable/testing)
-------------------------------------
"""
files = set()
for (dirpath, dirnames, filenames) in walk(foldername):
    for filename in filenames:
        if filename.endswith(".zip"):
            files.add(filename)

files = sorted(files, reverse=True)

last_file = "udts-0000000-ffffff-blah"
for file in files:
    f_s = file.split("-")
    l_s = last_file.split("-")
    if f_s[1] != l_s[1]:
        output += "\n"
        output += f"**{f_s[1][0:4]}-{f_s[1][4:6]}-{f_s[1][6:8]}**\n"
    if f_s[2] != l_s[2]:
        output += f"\n*{f_s[2]}*\n\n"
    output += f"- {f_s[3].capitalize()}: `{file} <http://updatethestream.com/builds/development/{file}>`_\n"
    last_file = file


with open("docs/source/releases.rst","w") as f:
    f.write(output)