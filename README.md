This code is in process of creating a cloudfoundry "Autoscale" demonstration

web_tier - this app will have three URL's <server>/fast , <server>/medium , <server>/slow that will create respective load on the server

loadapp - this is a load generater app that is configurable by URL, delay between requests, and number of concurrent threads

monitor - this is a dashboard that will serve pages that will provide visiability as to the load on the webserver and request times for page laods
