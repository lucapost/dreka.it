#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
		<div class="top">
		<div class="container_12 clearfix">
			<div class="grid_6">
				<header class="grid_6 alpha omega">	
					<a href="/" title="home page"><h1>''' + SITE_NAME + '''</h1></a>
					<h2>Immagini panoramiche da Cras e sul Kolovrat</h2>
				</header>
				<div class="grid_2 alpha">	
					<div id="google_translate_element"></div>
					<script type="text/javascript">
						function googleTranslateElementInit() {
  						new google.translate.TranslateElement({pageLanguage: 'it', includedLanguages: 'de,en,sl', layout: google.translate.TranslateElement.InlineLayout.SIMPLE, autoDisplay: false}, 'google_translate_element');
}
					</script>
					<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
				</div>
				<div class="grid_4 omega">
					social
				</div>
			</div>
			<div class="grid_6">
				<div class="grid_4 alpha right">
					<p>Associazione (Drustvo) Kobilja Glava<br/>
						Oznebrida (Ocneberdo), 13<br/>
						33040 Drenchia (Dreka), UD, Italia<br/><br/>
					<p/>
					<p><a href="mailto:kobiljaglava@yahoo.it" title="email">kobiljaglava@yahoo.it<br/>
						<a href="http://www.kobiljaglava.it" title="sito internet della kobilja glava">www.kobiljaglava.it</a>
					</p>
				</div>
				<figure class="grid_2 omega">
      					<img src="/images/kg_small.jpg" alt="kobilja glava" title="kobilja glava" class="logo"/>
				</figure>
			</div>
			<div class="clear"></div>
        	</div>
		</div>
		<div class="container_12 clearfix">
			<section class="grid_12">
				<p class="coordinate">Posizione: Razpotje (Cras), Comune di Dreka (Drenchia), 46 11'02''N - 13 38'11''</p>
			</section>
			<section class="grid_12">
				<a href="http://dreka.it/camera_1.jpg" class="fancybox" rel="gallery" title="In primo piano la canonica di Barnjak (Cras), a sinistra Stoblank (S. Volfango), Srednje, a destra Lombaj (Lombai) ed il monte Hum">
					<figure class="grid_6 alpha">
						<img src="http://dreka.it/camera_1.jpg" alt="webcam su cras" title="immagine verso cras" class="camera"/>
					</figure>
				</a>
				<a href="http://dreka.it/camera_2.jpg" class="fancybox" rel="gallery" title="Da sinistra: Dreka dolenja in gorenja (Drenchia inferiore e superiore), Trinko (Trinco), Cuodar (Zuodar), Kraj (Crai), ai piedi del Kolovrat">
					<figure class="grid_6 omega">
						<img src="http://dreka.it/camera_2.jpg" alt="webcam sul kolovrat" title="immagine verso kolovrat" class="camera"/>
					</figure>
				</a>
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
    		<div class="container_12 clearfix">
			<footer>
				<p><a href="mailto:info@dreka.it">info@dreka.it</a></p>	
			</footer>
		</div>
	</body>
</html>'''
