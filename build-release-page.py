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

# Change release header here
output = """

#################
Release Downloads
#################

**Stable releases** have been tested and approved for public use. 

**Development builds** are the latest check-ins from our development branch; use at your own risk.

***************
Stable Releases
***************\n"""

# main releases generated here. results.items is a dict of release tags and the value is a dict of files
for key, value in results.items():
    # release name is key, value is a dict of files
    output += f"{key}\n"
    output += "==========\n"
    for key2, value2 in value.items():
        # key2 is the filename, value2 is the url
        output += f"`{key2} <{value2}>`_\n"
    output += f"\n\n"

output += """
*************************************
Development Builds (unstable/testing)
*************************************
"""
files = set()
for (dirpath, dirnames, filenames) in walk(foldername):
    for filename in filenames:
        if filename.endswith(".zip"):
            files.add(filename)

files = sorted(files, reverse=True)

last_file = "udts-0000000-ffffff-blah"
for file in files:
    # f_s is the current file name
    # l_s is the last file name
    # we will do different stuff based on what changes in these file names
    # the file name is like "udts-0000000-ffffff-blah"
    # so splitting on - makes a list ['udts','000000','ffffff','blah']
    # f[0]: udts
    # f[1]: the date
    # f[2]: the build SHA code (uniqueish)
    # f[3]: platform, either windows or macos
    # there is a junk one so that it shows everything the first time

    f_s = file.split("-")
    l_s = last_file.split("-")

    # compares the date portion of the file name.
    # if the date has changed, show a new date header
    if f_s[1] != l_s[1]:
        output += "\n"
        date_string = f"{f_s[1][0:4]}-{f_s[1][4:6]}-{f_s[1][6:8]}"
        output += f"{date_string}\n"
        output += "==========\n"

    # if the build SHA code (e.g. e8eb1e3) is different
    # make a block for a new build
    if f_s[2] != l_s[2]:
        output += f"\n{f_s[2]}\n"
        output += "-------\n"

    # print the file link
    output += f"* {f_s[3].capitalize()}: `{file} <https://updatethestream.com/builds/development/{file}>`_ \n"
    last_file = file


with open("docs/source/releases.rst","w") as f:
    f.write(output)