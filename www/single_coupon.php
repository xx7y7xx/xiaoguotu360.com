<?PHP ob_start();
require_once "lib/clsSocialLikeLocker.php";
 ?>
<?PHP
$oLocker = new clsSocialLikeLocker();
$share_url = clsSocialLikeLocker::getCurrentURL();
$isLiked = $oLocker->isLiked($share_url);
?>
<!DOCTYPE HTML>

<head>

    <title>Theme by CssTemplateHeaven</title>
    <meta name="keywords" content="create from keywords">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
<!-- Google Fonts -->

    <link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>

<!-- CSS Files -->

    <link rel="stylesheet" type="text/css" media="screen" href="style.css">
    <link rel="stylesheet" type="text/css" media="screen" href="menu/css/simple_menu.css">
    <link rel="stylesheet" href="css/prettyPhoto.css" type="text/css" media="screen"/>
    <link rel="stylesheet" href="css/nivo-slider.css" type="text/css" media="screen"/>
    <link rel="stylesheet" type="text/css" href="boxes/css/style6.css" />

<!-- JS Files -->

	<script type="text/javascript" src="js/jquery.min.js"></script>
    <script type="text/javascript" src="http://connect.facebook.net/en_US/all.js#xfbml=1" /></script>
    <script type="text/javascript" src="assets/events.js" /></script>

</head>

<body>

    <div class="header">
    
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


    <div id="container">


<div class="two-third">

        <div class="coupon_content">
        
        
        <img title="" src="img/masonry/4.jpg" alt="" style="float:left; margin-right: 20px" />
        
        <h2 style="margin-top:0; margin-bottom:5px">Coupon Heading</h2>
        <div class="discount_value">15%</div>
        <small>Expiry Date: March 30th 2012</small>
        
        <p><strong>Description:</strong> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ipsum eros, mattis vel iaculis vel, viverra ac augue. Morbi diam nulla, porta in feugiat sed, adipiscing et risus.
        </p>
        
        <p style="font-weight:bold">Price: $ 1000 | Coupon Price: $ 800 </p>
        
        <!-- PHP Coupong Code -->
        
  <input type="hidden" id="url_request" value="unlock_handler.php?url=<?PHP echo urlencode($share_url); ?>" />
           
        
	  <?PHP if($isLiked == true): ?>
      
          <div style="background: #690; color: #FFF; padding: 10px 10px 20px; margin-bottom: 5px; border-radius: 5px; text-align: center; font-weight: bold; float: right; width: 268px">
             <p>Coupon Code: </p> <p style="font-size: 1.8em; padding-bottom: 20px">
             <?php // Generate a random number
			        echo mt_rand(2100, 2200); ?>
             </p>
          </div>
             
          <div style="margin-top: 15px; text-align:right">
          
      <?PHP else: ?>
      
          <div style="background:#F00; color: #FFF; padding: 10px 10px 20px; border-radius: 5px; text-align: center; font-weight: bold; float: right; width: 268px">
             <p><span style="font-style:italic">Hit the Like to get coupon code</span></p>
          
      <?PHP endif; ?>
      
      
       <!-- Share Buttons -->
       
        <div title="Like on Facebook"> 
          <fb:like href="<?PHP echo $share_url; ?>" layout="box_count" action="like" font="arial" show_faces="true" width="48" height="65"></fb:like> 
        </div> 
     
        </div> <!-- END PHP Coupon Code -->
        
       <div style="clear:both"></div>
        </div> <!-- END Coupon content box -->
        
        
        
        <h2>Some general info about the seller</h2>
        
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ipsum eros, mattis vel iaculis vel, viverra ac augue. Morbi diam nulla, porta in feugiat sed, adipiscing et risus.</p>
           
         <h2>Video</h2>
           
        <iframe src="http://player.vimeo.com/video/34904146?title=0&amp;byline=0&amp;portrait=0" width="629" height="354" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
        




</div><!-- close two third -->


      <div class="sidebar_right">
      
      <h3 style="margin-top:0">Seller Information</h3>
      
      <div id="coupon_seller_info">
          <ul>
            <li><strong>Company inc.</strong></li>
            <li>Streetname 36</li>
            <li>4343, Bergen</li>
            <li>Tel: 99 88 88 99</li>
            <li><a href="http://dieter.no" title="website">www.dieter.no</a></li>
<li><a href="http://www.facebook.com/schneiderfoto" title="website">Facebook</a></li>
          </ul>
      </div>
      
      <h3>Map</h3>
      
      <iframe width="300" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.no/maps?f=q&amp;source=s_q&amp;hl=no&amp;geocode=&amp;q=Hafstadvegen+36,+F%C3%B8rde&amp;aq=0&amp;oq=hafstadvegen+,36&amp;sll=61.143235,9.09668&amp;sspn=14.119743,46.538086&amp;ie=UTF8&amp;hq=&amp;hnear=Hafstadvegen+36,+6800+F%C3%B8rde,+Sogn+og+Fjordane&amp;t=m&amp;z=14&amp;ll=61.45023,5.855604&amp;output=embed"></iframe><br /><small><a href="http://maps.google.no/maps?f=q&amp;source=embed&amp;hl=no&amp;geocode=&amp;q=Hafstadvegen+36,+F%C3%B8rde&amp;aq=0&amp;oq=hafstadvegen+,36&amp;sll=61.143235,9.09668&amp;sspn=14.119743,46.538086&amp;ie=UTF8&amp;hq=&amp;hnear=Hafstadvegen+36,+6800+F%C3%B8rde,+Sogn+og+Fjordane&amp;t=m&amp;z=14&amp;ll=61.45023,5.855604" style="color:#0000FF;text-align:left">Large Map</a></small>
      
      
      
      </div><!-- end sidebar right -->
   
      <div style="clear:both; height: 40px"></div>
      
</div><!-- end container -->


    <div id="footer">

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
        Theme by <a href="http://www.csstemplateheaven.com">CssTemplateHeaven</a><br /> Photos © <a href="http://dieterschneider.net" title="Dieter Schneider Photography">Dieter Schneider</a>
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