import time
import datetime

SITE_NAME = "Le webcam di Drenchia (Dreka)"
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
        	<meta name="keywords" content="dreka, drenchia, kolovrat, valli del natisone, webcam" />
		<meta name="google-translate-customization" content="6cf47dec77693085-336ca7420c2badda-g5287f68072eea9cd-8"></meta>
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
		<div class="container_12 clearfix head">
			<header class="grid_12">
				<h2>Immagini panoramiche da Cras e sul Kolovrat</h2>
			</header>
			<div class="clear"></div>
			<div class="grid_6">
				<header class="grid_6 alpha omega">	
					<a href="/" title="home page"><h1>''' + SITE_NAME + '''</h1></a>
				</header>
			</div>
			<div class="grid_6">
				<div class="grid_4 alpha asso">
					<p>Associazione (Drustvo) Kobilja Glava<br/>
						Oznebrida (Ocneberdo), 13<br/>
						33040 Drenchia (Dreka), UD, Italia
					<p/>
					<p>kobiljaglava@yahoo.it</p>
				</div>
				<figure class="grid_2 omega">
      					<img src="/images/kg_small.jpg" alt="kobilja glava" title="kobilja glava" class="logo"/>
				</figure>
			</div>
			<div class="clear"></div>
        	</div>
		<div class="container_12 clearfix">
			<section class="grid_12">
				<a href="http://dreka.it/camera_1.jpg" class="fancybox" rel="gallery" title="In primo piano la canonica di Barnjak (Cras), a sinistra Stoblank (S. Volfango), Srednje, a destra Lombaj (Lombai) ed il monte Hum">
					<figure class="grid_6 alpha camera">
						<img src="http://dreka.it/camera_1.jpg"/>
					</figure>
				</a>
				<a href="http://dreka.it/camera_2.jpg" class="fancybox" rel="gallery" title="Da sinistra: Dreka dolenja in gorenja (Drenchia inferiore e superiore), Trinko (Trinco), Cuodar (Zuodar), Kraj (Crai), ai piedi del Kolovrat">
					<figure class="grid_6 omega camera">
						<img src="http://dreka.it/camera_2.jpg"/>
					</figure>
				</a>
			</section>
			<div class="clear"></div>
			<section class="grid_12">
				<p class="coordinate">Vista da Razpotje (Cras), in comune di Dreka (Drenchia), 46 11'02''N - 13 38'11''</p>
			</section>
			<div class="clear"></div>
		</div>
    		<div class="container_12 clearfix">
       			<div class="grid_12">
			'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
       			</div>
			<div class="clear"></div>
		</div>
		<footer class="container_12 clearfix">
			<p>Associazione (Drustvo) Kobilja Glava - Oznebrida (Ocneberdo), 13 - 33040 Drenchia (Dreka), UD, Italy</p>
			<p><a href="mailto:kobiljaglava@yahoo.it">kobiljaglava@yahoo.it</a></p>
		</footer>
	</body>
</html>'''
