sudo apt install apache2
sudo a2enmod headers

cp ./000-default.conf /etc/apache2/sites-enabled/
systemctl restart apache2.service
