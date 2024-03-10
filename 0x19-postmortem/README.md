Postmortem
Upon the release of the System Engineering & DevOps project 0x19, approximately 4:00 GMT + 1, an Error occurred on the Ubuntu 14.04 container running an Apache web server. GET requests on the server gave as output 500 Internal Server Error's, when the expected response was an HTML file defining a simple Holberton WordPress site.

Debugging Process
Oumate (I) encountered the issue upon opening the project and being, well, instructed to address it. He promptly proceeded to undergo solving the problem.

Checked running processes using ps aux. Two apache2 processes - root and www-data - were properly running.

Looked in the sites-available folder of the /etc/apache2/ directory. Found that the web server was serving content located in /var/www/html/.

In one terminal, ran strace on the PID of the root Apache process. In another, curled the server. strace gave no useful information.

Repeated step 3, except on the PID of the www-data process.strace displayed an -1 ENOENT (No such file or directory) error occurring upon an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp.

Looked through files in the /var/www/html/ directory one-by-one, using Vi pattern matching to trying to locate the erroneous .phpp file extension. Located it in the wp-settings.php file. (Line 137, require_once( ABSPATH . WPINC . '/class-wp-locale.php' );).

Removed the trailing p from the line.

Tested another curl on the server. 200 A-ok!

Wrote a Puppet manifest to automate fixing of the error.

Summation
It was all about a typo. the WordPress app was encountering an error in wp-settings.php when tyring to load the file class-wp-locale.phpp. The correct file name, located in the wp-content directory of the application folder, was class-wp-locale.php.

Patch involved a simple fix on the typo, removing the trailing p.

Prevention
This outage was not a web server error, but an application error. To prevent such outages, adopt the following strategies

Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.

Status monitoring. Enable some uptime-monitoring service such as PagerDuty to alert instantly upon outage of the website.
