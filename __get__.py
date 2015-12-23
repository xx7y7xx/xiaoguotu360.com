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

def write_html(str, filepath):
  Html_file = open(filepath, "w")
  Html_file.write(str)
  Html_file.close()
  
def append_html(str, filepath):
  Html_file = open(filepath, "a")
  Html_file.write(str)
  Html_file.close()

def get_json():
  xlog("start")
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
    
    html_str = """
<html>
<head>
<title>效果图</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, minimum-scale=0.1">
</head>
<body style="margin: 0px;">
<img style="-webkit-user-select: none" src="%s">
</body>
</html>
""" % image_url
    
    # /repo/4951b757-7b4d-4234-bf00-732d2da77717/image.html
    write_html(html_str, resource_dir + "/image.html")
    
    #@TODO check 404 on res["Result"][0]["image"]
    html_str = '<div class="box photo col3"><a href="'
    html_str += html_url
    html_str += '" title="效果图"><img src="'
    html_str += thumbnail_url
    html_str += '" /></div>'
    append_html(html_str, WWWROOT + "/index.html")

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
  
  
  html_str = """
<!DOCTYPE HTML>

<head>

    <title>效果图360全景</title>
    <meta name="keywords" content="效果图 全景效果图 360效果图">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
<!-- Google Fonts -->

    <!--<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>-->

<!-- CSS Files -->

    <link rel="stylesheet" type="text/css" media="screen" href="style.css">
    <link rel="stylesheet" type="text/css" media="screen" href="menu/css/simple_menu.css">
  
<!-- JS Files -->

    <script src="http://libs.baidu.com/jquery/1.10.2/jquery.min.js"></script>

    
    <!-- Masonry -->
    
	<script src="js/jquery.masonry.min.js"></script>
    
    <script>
      $(function(){
    
        var $container = $('#container');
      
        $container.imagesLoaded( function(){
          $container.masonry({
            itemSelector : '.box',
			isFitWidth: true,
			isAnimated: true
          });
        });
      
      });
    </script>
    


</head>

<body>

    <div class="header" style="display: none;">
    
    <div id="site_title"><a href="index.html"><img src="img/logo.png" /></a></div>

    <!-- Main Menu -->
    
    <ol id="menu">
             <li class="active_menu_item"><a href="index.html">Home</a>
        
              <!-- sub menu -->
              <ol> 
                <li><a href="product_viewer.html">Product Viewer</a></li> 
                <li><a href="nivo.html">Nivo Slider</a></li>
                <li><a href="ei_slider.html">EI Slider</a></li>
                <li><a href="fullscreen_gallery.html">Fullscreen Slider</a></li>
                <li><a href="image_frontpage.html">Static Image</a></li>
              </ol>
              </li><!-- END sub menu -->
        
        <li><a href="#">Pages</a>
        
              <!-- sub menu -->
              <ol>    
                <li><a href="single_coupon.php">Coupon</a></li> 
                <li><a href="magazine.html">Magazine</a></li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="full-width.html">Full Width Page</a></li>
                <li><a href="columns.html">Columns</a></li>
              </ol>
        </li><!-- END sub menu -->
        
        <li><a href="elements.html">Elements</a></li>
              
        <li><a href="#">Galleries</a>
        
              <!-- sub menu -->
              <ol>     
                <li><a href="gallery-simple.html">Simple</a></li>
                <li><a href="portfolio.html">Filterable</a></li>
                <li><a href="gallery_fader.html">Fade Scroll</a></li>
                <li><a href="video.html">Video</a></li>
                <li class="last"><a href="photogrid.html">PhotoGrid</a></li>
              </ol>
        </li><!-- END sub menu -->
        
               <li><a href="contact.html">Contact</a></li>
    </ol>
    
    
    </div><!-- END header -->

    <div id="container" style="background-color: rgba(0,0,0,0.2);">

    <!--<div class="box photo col3">
    <div class="discount_value">15%</div>
      <a href="single_coupon.php" title="Photo by Dieter Schneider"><img src="img/masonry/4.jpg" alt="Stanley" /></a>
      <h3>Studio Photography</h3>
    </div>-->
"""
  write_html(html_str, WWWROOT + "/index.html")
  
  get_json()
  
  html_str = """


    <div style="clear:both; height: 40px"></div>
    </div>

    <!-- END container -->
    
    
    <div id="footer" style="display: none;">

    <!-- First Column -->

    <div class="one-fourth">
        <h3>Useful Links</h3>
            <ul class="footer_links">
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Ellem Ciet</a></li>
                <li><a href="#">Currivitas</a></li>
                <li><a href="#">Salim Aritu</a></li>
            </ul>
    </div>
    
    <!-- Second Column -->
    
    <div class="one-fourth">
        <h3>Terms</h3>
            <ul class="footer_links">
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Ellem Ciet</a></li>
                <li><a href="#">Currivitas</a></li>
                <li><a href="#">Salim Aritu</a></li>
            </ul>
    </div>
    
    <!-- Third Column -->
    
    <div class="one-fourth">
        <h3>Information</h3>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet enim id dui tincidunt vestibulum rhoncus a felis.
        
        <div id="social_icons">
        Copyright &copy; 2014.Company name All rights reserved.<a target="_blank" href="http://sc.chinaz.com/moban/">&#x7F51;&#x9875;&#x6A21;&#x677F;</a>
        </div>
        
    </div>
    
    <!-- Fourth Column -->
    
    <div class="one-fourth last">
        <h3>Socialize</h3>
            <img src="img/icon_fb.png" alt="Facebook">
            <img src="img/icon_twitter.png" alt="Facebook">
            <img src="img/icon_in.png" alt="Facebook">
    </div>

    <div style="clear:both"></div>
    
    </div> <!-- END footer -->




</body>
</html>
"""
  append_html(html_str, WWWROOT + "/index.html")
  
  

if __name__ == '__main__':
  main()

# end
