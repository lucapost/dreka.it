import time
import datetime

SITE_NAME = "Le webcam di Dreka"
SITEMAP = "./dst/sitemap.xml"
URL = "http://dreka.it"
SRC = "/home/lucapost/repo/dreka.it/src/"
TITLE = "Dreka"
SUBTITLE = "Immagini panoramiche dal territorio di Drenchia, sul Kolovrat, nelle Valli del Natisone in provincia di Udine"
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
       		<title>''' + SITE_NAME + ''' | ''' + SUBTITLE + '''</title>
		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960_12_col.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/owl.carousel.min.css">
		<link rel="stylesheet" type="text/css" media="all" href="/fancybox/source/jquery.fancybox.css"/>
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
  		<script src="/js/modernizr.js"></script> 
  		<script src="/js/hashgrid.js"></script> 
		<script src="/fancybox/source/jquery.fancybox.pack.js"></script>
  		<script src="/js/fancy.js"></script> 
	</head>
	<body id="home">
			<div id="top" class="container_12 clearfix head">
				<header class="grid_8">	
					<a href="/" title="home page">
						<h1>''' + SITE_NAME + '''<h1/>
					</a>
					<h2>Immagini panoramiche dal territorio di Drenchia: da Cras e sul Kolovrat</h2>
				</header>
				<figure>
      					<img src="/images/DKGb.png" alt="kobilja glava" title="kobilja glava" class="grid_4 logo">
				</figure>
               		</div>
			<div class="container_12 clearfix">
				<section>
					<a href="http://dreka.it/camera_1.jpg" class="fancybox" rel="gallery" title="Da Cras in direzione San Volfango e Lombai">
						<figure class="grid_6 camera">
							<img src="http://dreka.it/camera_1.jpg"/>
							<figcaption>La piazza e la canonica di Cras; sullo sfondo la chiesa di San Volfango, Rucchin e Lombai; l'altopiano della Baisizza ed il Monte Cum</figcaption>
						</figure>
					</a>
					<a href="http://dreka.it/camera_2.jpg" class="fancybox" rel="gallery" title="Da Cras in direzione Kolovrat: Drenchia, Trinco, Zuodar e Crai">
						<figure class="grid_6 camera">
							<img src="http://dreka.it/camera_2.jpg"/>
							<figcaption>La catena montuosa del Colovrat; le frazioni di Drenchia Superiore ed Inferiore, Trinco, Zuodar e Crai; Passo Casoni Solarie</figcaption>
						</figure>
					</a>
				</section>
				<section class="grid_12">
					<p>sponsor</p>
				</section>

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
