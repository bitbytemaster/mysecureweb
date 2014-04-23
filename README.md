mysecureweb
===========

A sample web application created to demonstrate typical web security vulnerabilities for secure web development training purposes

Implementation Technologies:
- Linux (CentOS 6.5), Apache, MySQL 14.14, Python 2.6.7
- Apache Python WSGI module (mod_wsgi 3.4)
- web.py 0.37
- Ext JS 4.2.1

Security Vulnerabilities to illustrate:
- Sensitive Data Exposure 
  - not fail intelligently
- Injection (lack proper input validation)
  - sql injection
  - XML injection (XML parser)
- directory traversal
- Cross-site scripting (XSS)
- Cross-site request forgery (csrf)
- Insecure Direct Object Reference
- clickjacking
