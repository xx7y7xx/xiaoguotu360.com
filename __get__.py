#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import json
import urllib2
from urllib2 import urlopen
import socket

import logging
import sys
import random

import os, errno
import time

from jinja2 import Environment, loaders

reload(sys)
sys.setdefaultencoding('utf8')

KEY = "crziu5s9omlqiqxaqyyn"
DOMAIN = "http://www.xuanran001.com/api"
URL = "%s/getdesignlist.html?key=%s&size=big" %(DOMAIN, KEY)

WWWROOT = "/var/www/html"
REPO = WWWROOT + "/repo"

def xlog(str):
  logger = logging.getLogger("getdesignlist")
  #logger.debug( str )

# get json object from url
def getjson(url):
  try:
    response = urlopen(url, timeout = 120)
  except urllib2.HTTPError as e:
    msg = "URL : %s\n" % url
    msg += 'Server return code : %s' % e.code
    xlog(msg)
  except urllib2.URLError as e:
    xlog(('Unexpected exception thrown:', e.args))
  except socket.timeout as e:
    xlog(('Server timeout:', e.args))
      
  raw_data = response.read().decode('utf-8')
  return json.loads(raw_data)

# check resource 404
def check404(url):
  try:
    urlopen(url, timeout = 120)
  except urllib2.HTTPError as e:
    msg = "URL : %s\n" % url
    msg += 'Server return code : %s' % e.code
    if e.code == 404:
      return True
  #except urllib2.URLError as e:
  #  print(('Unexpected exception thrown:', e.args))
  #except socket.timeout as e:
  #  print(('Server timeout:', e.args))
  return False

def mkdir_p(path):
  try:
    os.makedirs(path)
  except OSError as exc: # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(path):
      pass
    else: raise

def write_html(template_name, render_data, html_path):
  env = Environment(loader=loaders.FileSystemLoader("/root/xiaoguotu360.com/res/templates"))
  tmpl = env.get_template(template_name)
  output = tmpl.render(data = render_data).encode('utf8')
  with open(html_path, "wb") as fh:
    fh.write(output)

def get_json():
  xlog("start")
  image_list = []
  for offset in range(0, 1000):
    #http://www.xuanran001.com/api/getdesignlist.html?key=crziu5s9omlqiqxaqyyn&offset=0&limit=10
    url = URL + "&limit=1&offset=" + str(offset)
    xlog("url: " + url)
    res = getjson(url)
    #with open("/var/www/html/data/" + str(offset) + '.json', 'w') as outfile:
    #  json.dump(res, outfile)
    
    uuid = res["Result"][0]["id"]
    image_url = res["Result"][0]["image"]
    thumbnail_url = res["Result"][0]["thumbnail"]
    
    if check404(image_url):
      continue
    if check404(thumbnail_url):
      continue
    
    resource_dir = REPO + "/" + uuid
    html_path = resource_dir + "/image.html"
    html_url = "repo/" + uuid + "/image.html"
    mkdir_p(resource_dir)
    
    image_data = {
      "image_url": image_url
    }
    
    # /repo/4951b757-7b4d-4234-bf00-732d2da77717/image.html
    write_html("image.html", image_data, os.path.join(resource_dir, "image.html"))
    
    #@TODO check 404 on res["Result"][0]["image"]
    image_list.append({
      "html_url": html_url,
      "thumbnail_url": thumbnail_url
    })
  return image_list

def main():

  # create logger
  logger = logging.getLogger('getdesignlist')
  logger.setLevel(logging.DEBUG)

  # create console handler and set level to debug
  ch = logging.StreamHandler( sys.__stdout__ ) # Add this
  ch.setLevel(logging.DEBUG)

  # create formatter
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  # add formatter to ch
  ch.setFormatter(formatter)

  # add ch to logger
  logger.addHandler(ch)

  # 'application' code
  #logger.debug('debug message')
  #logger.info('info message')
  #logger.warn('warn message')
  #logger.error('error message')
  #logger.critical('critical message')
  
  write_html("index.html", get_json(), os.path.join(WWWROOT, "index.html"))

if __name__ == '__main__':
  main()

# end
