Title: Supervisord
Date: 2025-07-13 19:55
Modified: 2025-07-13 19:55
Category: Linux
Tags: linux, command line, useful commands, automation, systemd, supervisord
Slug: orchestrate-your-system-services-with-supervisor-d
Authors: Craig Derington
Summary: Orchestrate your Linux services with supervisord &amp; systemd-monitor



#### Supervisor

```
sudo apt-get install -y supervisor
service supervisor restart

sudo supervisorctl start <daemon_name>
sudo supervisorctl stop <daemon_name>
sudo supervisorctl reread
sudo supervisorctl update
```

##### start on boot

```
sudo systemctl enable supervisor
sudo systemctl start supervisor
```

##### lanternv2 celery worker supervisor conf file

```
; the name of the program for supervisord
[program:lanternv2celery]

; set the full path to celery program if using virtualenv
command=/var/www/html/LanternV2/.env/bin/celery worker -A config --loglevel=INFO

; the directory to your Django project
directory=/var/www/html/LanternV2/wsnowebv2

; if supervisord is run as the root user, switch users to this unix user account before processing
user=root

; supervisord will start as many instances oof this program as named by numprocs
numprocs=1

; put the process stdout outut in this file
stdout_logfile=/var/log/celery/lanternv2_worker.log

; put process stderr output in this file
stderr_logfile=/var/log/celery/lanternv2_worker.log

; if true, this program will start automatically when supervisord is started
autostart=true

; if the program exits without a standard exit code, then set autorestart to true
autorestart=true

; the total number of seconds which the program needs to stay running after a startup to
; consider successful
startsecs=10

; need to wait for currently executing tasks to finish at shutdown, increase this for long running tasks
stopwaitsecs=600

; when resorting to sending a SIGKILL to the program to terminate it, send SIGKILL to its entire process
; taking care of it's children priocesses as well
killasgroup=true

; if your broker is supervised, set it's priority higher so it starts first
priority=998
```

##### lanternv2 celery beat supervisor conf file

```
; the name of the supervisord program
[program:lanternv2celerybeat]

; set the full path to celery program if using virtualenv
command=/var/www/html/LanternV2/.env/bin/celery beat -A config --loglevel=INFO

; the directory for the django project
directory=/var/www/html/LanternV2/wsnowebv2

; if supervisord us run as the root user, switch user accounts
user=root

; supervisord will start as many instances of this program as named by numprocs
numprocs=1

; put the process stdout in this log file
stdout_logfile=/var/log/celery/lanternv2_beat.log

; put the process stderr in this log file
stderr_logfile=/var/log/celery/lanternv2_beat.log

; if true, this program will start automatically when supervisord is started
autostart=true

; if the program exits without a valid exit code, auto restart the program
autorestart=true

; the total number of seconds in which the program needs to stay running after
; a startup to consider the start successful
startsecs=10

; if your broker is supervised, set it's priority higher so it starts first
priority=999
```
