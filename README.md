mysecureweb
===========

A sample web application created to demonstrate typical web security vulnerabilities for secure web development training purposes

<h3>Implementation Technologies:</h3>
- Linux (CentOS 6.5), Apache, MySQL 14.14, Python 2.6.7
- Apache Python WSGI module (mod_wsgi 3.4)
- web.py 0.37
- jQuery 1.11.0

<h3>Security Vulnerabilities to illustrate:</h3>
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
