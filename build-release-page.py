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

**Stable releases** are for public use, and though still in alpha, should be stable.

**Development builds** are the latest check-ins from our development branch and may have bugs; use at your own risk.

***************
Stable Releases
***************\n"""

# main releases generated here. results.items is a dict of release tags and the value is a dict of files
for key, value in results.items():
    # release name is key, value is a dict of files. underline amount calculated off key length
    output += f"{key}\n"
    for i in range(len(key)):
        output += "="
    output += "\n"
    for key2, value2 in value.items():
        # key2 is the filename, value2 is the url
        output += f"`{key2} <{value2}>`_\n"
    output += f"\n\n"

output += """
*************************************
Development Builds (unstable/testing)
*************************************
*All times are in UTC.*
"""
files = set()
for (dirpath, dirnames, filenames) in walk(foldername):
    for filename in filenames:
        if filename.endswith(".zip"):
            files.add(filename)

files = sorted(files, reverse=True)

last_file = "udts-0000000-ffffff-blah"
if len(files):
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

        # if the build tinme is different
        # make a block for a new build
        if f_s[2] != l_s[2]:
            hours = int(f_s[2][0:2])
            minutes = f_s[2][2:4]
            suffix = "AM"
            if hours > 12:
                hours = hours - 12
                suffix = "PM"
            timestring = f"{hours}:{minutes} {suffix}"
            output += f"\n{timestring}\n"
            for i in range(len(timestring)):
                output += "-"
            output += "\n"

        # print the file link
        output += f"* {f_s[3].capitalize()}: `{file} <https://updatethestream.com/builds/development/{file}>`_ \n"
        last_file = file
else:
    output += "\nThere are currently no available development builds."

with open("docs/source/releases.rst","w") as f:
    f.write(output)
