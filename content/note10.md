Title: Configure Apache as a Reverse Proxy
Date: 2025-07-15 19:00
Modified: 2025-07-15 19:00
Category: Linux
Tags: linux, apache2, web server, reverse proxy, configuration
Slug: configure-apache-as-reverse-proxy-with-ssl
Authors: Craig Derington
Summary: Configure Apache as a Reverse Proxy


#### Configure Apache as a Reverse Proxy with SSL

I like to use Apache as a reverse proxy especially for my Java Spring Boot &amp; Python apps.  The configuration syntax is familiar and I prefer Apache over Nginx.  Fire up your application running on localhost and whatever port you have defined.  Next, create this Apache reverse proxy site configuration file, enable the site:

```
$ sudo a2ensite your-site-name
```

and then restart Apache.  

```
$ sudo systemctl reload apache2
-or-
$sudo service restart apache2

```

Here is the contents of your-site-name.conf.

```
<VirtualHost *:80> 
    ServerName domain-name.tld 
    ServerAlias domain-name.tld

    # Redirect HTTP to HTTPS
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{SERVER_NAME}$1 [R=301,L]

    # Proxy settings for local app
    # ProxyPreserveHost On
    # ProxyPass / http://localhost:8000/
    # ProxyPassReverse / http://localhost:8000/

    ErrorLog ${APACHE_LOG_DIR}/application-name-error.log
    CustomLog ${APACHE_LOG_DIR}/application-name-access.log combined

</VirtualHost>

<VirtualHost *:443> 

    ServerName domain-name.tld
    ServerAlias domain-name.tld
    ServerAdmin user@domain-name.tld

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/certificate.crt
    SSLCertificateKeyFile /etc/ssl/certs/private.key
    SSLCertificateChainFile /etc/ssl/certs/ca_bundle.crt

    # Proxy settings for your application running locally
    ProxyPreserveHost On
    ProxyPass / http://localhost:8000/
    ProxyPassReverse / http://localhost:8000/

    ErrorLog ${APACHE_LOG_DIR}/application-name-ssl-error.log
    CustomLog ${APACHE_LOG_DIR}/application-name-ssl-access.log combined

</VirtualHost>

```