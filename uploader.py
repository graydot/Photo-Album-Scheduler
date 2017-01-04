# This should be setup as a cron job

# get list of services
# get last uploaded photo for each service
# check frequency for service and check if next post time is now
# If now, check if any photos exist to be uploaded
# If so, mark as uploading and upload
# after upload mark as uploaded for that service

# Tables
# Images: File Name
# Services: Service Name, API Key/Secret, Enabled (in case of repeated errors), Frequency
# File Upload Info: File ID, Service ID
# File Archive: File ID, File Name, Service ID, Service Name, Time of Upload

# Basic, start with one image per day and with service credentials in a file (not committed). Files ordered by suffixed numbers

config_file = '~/.photo_album_scheduler'
image_folder = '~/images'

# Read config file

import ConfigParser
import os

config = ConfigParser.RawConfigParser()
config.readfp(open(os.path.expanduser(config_file)))

# fail if file does not exist

if config.has_section('credentials') == False:
	raise Exception("Credentials section not present")
if (config.has_option('credentials', 'access_token') == False) or (config.has_option('credentials', 'secret_key') == False):
	raise Exception("Access token or secret key not present")

# list files in directory
full_image_path = os.path.expanduser(image_folder)
images = [f for f in os.listdir(full_image_path)
    if os.path.isfile(os.path.join(full_image_path, f)) and
    os.path.splitext(f)[1] in ['.jpg', '.jpeg']]

if len(images) == 0:
	raise Exception("No new images, nothing to do")

image = images[0]

# try to upload to facebook
