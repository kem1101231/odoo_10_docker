FROM ubuntu:16.04

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
						python-dateutil \
						python-docutils \
						python-feedparser \
						python-jinja2 \
						python-ldap \
						python-libxslt1 \
						python-lxml \
						python-mako \
						python-mock \
						python-openid \
						python-psycopg2 \
						python-psutil \
						python-pybabel \
						python-pychart \
						python-pydot \
						python-pyparsing \
						python-reportlab \
						python-simplejson \
						python-tz \
						python-unittest2 \
						python-vatnumber \
						python-vobject \
						python-webdav \
						python-werkzeug \
						python-xlwt \
						python-yaml \
						python-zsi \
						poppler-utils \
						python-pip \
						python-pypdf \
						python-passlib \
						python-decorator \
						gcc \
						python-dev \
						mc \
						bzr \
						python-setuptools \
						python-markupsafe \
						python-reportlab-accel \
						python-zsi \
						python-yaml \
						python-argparse \
						python-openssl \
						python-egenix-mxdatetime \
						python-usb \
						python-serial \
						lptools make \
						python-pydot \
						python-psutil \
						python-paramiko \
						poppler-utils \
						python-pdftools \
						antiword \
						python-requests \
						python-xlsxwriter \
						python-suds \
						python-psycogreen \
						python-ofxparse \
						python-gevent \
						python-pillow \
						nodejs \
						npm \
						wget \
						dpkg \
						zip \
						unzip \
						tar \
	&& ln -s /usr/bin/nodejs /usr/bin/node \
	&& npm install -g less@3.0.4 less-plugin-clean-css \
	&& adduser --system --home=/opt/odoo --group odoo \
	&& mkdir /var/log/odoo \
	&& chown -R odoo:root /var/log/odoo \
	&& mkdir /etc/odoo \
	&& wget https://pypi.python.org/packages/a8/70/bd554151443fe9e89d9a934a7891aaffc63b9cb5c7d608972919a002c03c/gdata-2.0.18.tar.gz \
	&& tar zxvf gdata-2.0.18.tar.gz \
	&& chown -R odoo: gdata-2.0.18 \
	&& cd gdata-2.0.18/ \
	&& python setup.py install \
	&& cd /opt/odoo \
	&& wget https://github.com/odoo/odoo/archive/10.0.zip \
	&& unzip 10.0.zip \
	&& chown -R odoo: odoo-10.0 \
	&& pip install Pillow==3.4.0 \
	&& wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb \
	&& dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb \
	&& cp /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage \
	&& cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf 

COPY ./odoo-server.conf /etc/odoo/
COPY ./odoo-server.service /lib/systemd/system/

RUN chmod 755 /lib/systemd/system/odoo-server.service \
    	&& chown root: /lib/systemd/system/odoo-server.service \
    	&& chown -R odoo: /opt/odoo/ \
    	&& chown odoo:root /var/log/odoo \
    	&& chown odoo: /etc/odoo/odoo-server.conf \
    	&& chmod 640 /etc/odoo/odoo-server.conf


CMD ["python /opt/odoo/odoo-10.0/odoo-bin -c /etc/odoo/odoo-server.conf"]

WORKDIR /opt/odoo
