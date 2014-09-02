import time
import datetime

SITE_NAME = "Le webcam di Dreka"
SITEMAP = "./dst/sitemap.xml"
URL = "http://dreka.it"
SRC = "/home/lucapost/repo/dreka.it/src/"
TITLE = "Dreka"
SUBTITLE = "Immagini panoramiche sul territorio di Drenchia, sul Kolovrat, nelle Valli del Natisone in provincia di Udine"
DST = "./dst/"
PREFIX = "/"
HOME = "/"
PATH_SEPARATOR = "/"

SRC_EXT = {"markdown": "md", "textile": "textile", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.md"])

current_time = datetime.datetime.now()

def header(node):
    """Build the header and return it to a string."""

    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
       	<meta charset="utf-8" />
       	<meta name="author" content="Luca Postregna" />
	<meta name="description" content="''' + SUBTITLE + ''' - ''' + node.page.name + '''" />
        <meta name="keywords" content="dreka, drenchia, kolovrat, valli del natisone, webcam">
       	<title>''' + SITE_NAME + ''' | ''' + SUBTITLE + ''' | ''' + node.page.name + '''</title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960_12_col.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
		<script src="/js/jquery.min.js"></script>
  		<script src="/js/modernizr.js"></script> 
  		<script src="/js/hashgrid.js"></script> 
		<link rel="stylesheet" href="/owl-carousel/owl.carousel.css">
		<link rel="stylesheet" href="/owl-carousel/owl.theme.css">
		<script src="/owl-carousel/owl.carousel.js"></script>
		<script src="/js/owl.demo.js"></script>
	</head>
	<body>
			<header id="top" class="container_12 clearfix">
				<h1 class="grid_12"><a href="/" title="home page">''' + SITE_NAME + '''</a></h1>
				<h2 class="grid_12">Immagini panoramiche dalla frazione di Cras e sulla catena del Kolovrat, nel comune di Drenchia</h2>
               		</header>
		<div class="boxfigure">
			<figure class="container_12 clearfix">
				<div class="bigfigure grid_12">
      					<img src="http://dreka.it/camera_1.jpg" alt="camera_1" title="la webcam su Cras" id="cras" class="focus">
      					<img src="http://dreka.it/camera_2.jpg" alt="camera_2" title="la webcam sul Kolovrat" id="kolovrat">
				</div>
				<nav>
					<a href="/#cras" class="selfigure grid_2 prefix_4">
      						<img src="http://dreka.it/camera_1.jpg" alt="camera_1" title="la webcam su Cras" class="small">
					</a>
					<a href="/#kolovrat" class="selfigure grid_2 suffix_4">
      						<img src="http://dreka.it/camera_2.jpg" alt="camera_2" title="la webcam sul Kolovrat" class="small">
					</a>
				</nav>

			</figure>
            	</div>
			<div class="clear"></div>
			<div class="container_12 clearfix">
				<div id="owl-example" class="owl-carousel grid_12">
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa Carta</h4>
							<a href="#">sito carla</a>
							<p>indirizzo carla</p>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa Pippo</h4>
							<a href="#">sito Pippo</a>
							<p>indirizzo pippo</p>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa AAAA</h4>
							<a href="http://www.casa-mariza.de">www.casa-mariza.de</a>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa Carta</h4>
							<a href="#">sito carla</a>
							<p>indirizzo carla</p>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa Pippo</h4>
							<a href="#">sito Pippo</a>
							<p>indirizzo pippo</p>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa AAAA</h4>
							<a href="http://www.casa-mariza.de">www.casa-mariza.de</a>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa Carta</h4>
							<a href="#">sito carla</a>
							<p>indirizzo carla</p>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa Pippo</h4>
							<a href="#">sito Pippo</a>
							<p>indirizzo pippo</p>
					</div>
			  		<div>
      						<img src="/images/mariza.jpg" alt="logo casa mariza" title="la tabella di casa mariza" class="smaller">
							<h4>Casa AAAA</h4>
							<a href="http://www.casa-mariza.de">www.casa-mariza.de</a>
					</div>

				</div>
			</div>
			<div class="clear"></div>
    	    		<section class="container_12 clearfix">
            			<div class="grid_12">
			'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
            			</div>
				<div class="clear"></div>
			</section>
</body>
</html>'''
