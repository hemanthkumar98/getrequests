# getrequests
Python code and binary executable that makes a get request to domain/IP address. 


For building, make sure you've installed requests.

pip install requests
pyinstaller --onefile web_probe.py


Complie and build with python3

Run: 

web_probe.exe google.com
web_probe.exe 1.1.1.1


Example:

C:\Users\Admin\Desktop\dist>web_probe.exe google.com
Trying http://google.com

[+] GET http://google.com -> Status Code: 200
Headers:
  Date: Tue, 24 Jun 2025 05:42:01 GMT
  Expires: -1
  Cache-Control: private, max-age=0
  Content-Type: text/html; charset=ISO-8859-1
  Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-QYUNltVcZBrv6kXE0AQ9Sg' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
  P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
  Content-Encoding: gzip
  Server: gws
  X-XSS-Protection: 0
  X-Frame-Options: SAMEORIGIN
  Transfer-Encoding: chunked
  Set-Cookie: AEC=AVh_V2hQvcjv7uY8zpwRr-BWf8cLl5LaxcBJKC43BFw-HBQVH8I-gOLhbLo; expires=Sun, 21-Dec-2025 05:42:01 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax, NID=524=a8Lv9p74hZWj38eKqDjKGg8Jh1m4ihVl8fSXlk7x0AMwBVew11e3DcdYbTs2SrTiGvtOslu7ztQhOFoKj4DTjTF2VKOUdRh_4LzFacLUNY9wDr91fR1CMOQDaMtNs78BWtmJpcke4vLk_baaOKGVwsLiu4J7C8d9v8QNxNGqkbl1FO3aorIpXR9F4x_mX7kH1cqQ_5bytm8nkD_V7A; expires=Wed, 24-Dec-2025 05:42:01 GMT; path=/; domain=.google.com; HttpOnly

Response Body (truncated):
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="QYUNltVcZBrv6kXE0AQ9Sg">(function(){var _g={kEI:'qTpaaI2qE4jF5OUPtpSmsA8',kEXPI:'0,202791,63,2,610014,2887471,608,435,538661,78813,16105,344796,228119,19200,23156,19569,11106,4558,5214617,11401,32768932,4043710,25...
