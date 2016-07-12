# Copyright (C) 2016 Stefan Huchler

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/bin/python3


import subprocess
import json
import sys
import os
from string import Template

streaming_url = sys.argv[1]
json_string = subprocess.check_output(["youtube-dl", "--dump-json", streaming_url])
parsed_json = json.loads(json_string.decode(sys.stdout.encoding))

# uploader = "uploader" in parsed_json and parsed_json['uploader'] or "NA"
# uploader = (parsed_json['uploader'], "NA")['uploader' in parsed_json]
# uploader = parsed_json['uploader'] if "uploader" in parsed_json else "NA"

uploader = parsed_json.get('uploader', "NA")

info_file_content = Template( \
"""
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<$type>
  <title>$title</title>
</$type>
""")

tvshow_info = info_file_content.substitute(
  type="tvshow", title=uploader)

show_path = "/mnt/data/youtube/" + uploader
if not os.path.exists(show_path):
  os.makedirs(show_path)

show_file_path = os.path.join(show_path, "tvshow.nfo") 
if not os.path.isfile(show_file_path):
  with open(show_file_path,'w') as f:
    f.write(tvshow_info)

title = parsed_json.get('title', 'no title')
upload_date = parsed_json.get('upload_date', 'no date')

episode_info = info_file_content.substitute(
  type="episodedetails", title=title)


episode_name_unescaped = "{1}_{0}".format(title, upload_date)
episode_name = episode_name_unescaped.replace("/", ":")
episode_file_path = os.path.join(show_path, episode_name)
episode_nfo_file_path = "{}.nfo".format(episode_file_path)
with open(episode_nfo_file_path,'w') as f:
  f.write(episode_info)

episode_video_file_path = "{}.mp4".format(episode_file_path)

json_string = subprocess.check_output(["youtube-dl",
                                       "-o", episode_video_file_path, streaming_url])

# with urllib.request.urlopen(url) as response, open(episode_video_file_path, 'wb') as out_file:
#     shutil.copyfileobj(response, out_file)

