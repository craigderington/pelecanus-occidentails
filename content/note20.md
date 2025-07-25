Title: Don't at me, Bro!
Date: 2025-06-28 04:30
Modified: 2025-06-28 04:30
Category: Linux
Tags: automation, cron, at, linux, scheduled tasks
Slug: the-one-hit-wonder-of-scheduled-automation
Authors: Craig Derington
Summary: Do this thing, then disappear.


#### Linux at Command: The One-Hit Wonder of Automation
Linux’s cron is the king of recurring tasks, but what about those one-time jobs you need to fire off at a specific moment? Enter at, the unsung hero of one-shot scheduling. It’s like setting a single alarm clock for your scripts, perfect for your Python apps, Docker cleanup, or PostgreSQL maintenance. While cron’s your daily driver, at is the sneaky sidekick for tasks you only need once. Here’s a quirky guide to using at for your Notes site, with examples to automate your craigderington Docker Hub workflows.



#### Why at?
at schedules a command to run once at a specified time, then disappears like a ninja. It’s lightweight, built into most Linux distros, and ideal for one-off tasks like backups, container restarts, or sending yourself a reminder to take a break. Unlike cron, no crontab editing—just a quick command and you’re done.
Installing at
Most distros have at pre-installed. If not:

```
sudo apt install at  # Debian/Ubuntu
sudo dnf install at  # Fedora/RHEL
sudo pacman -S at    # Arch
```

Start the atd daemon:

```
sudo systemctl enable --now atd
```


#### Basic Usage

Run a command at a specific time:

```
at 3:30pm
```

This opens an interactive prompt. Type your command, then press Ctrl+D:


```
/bin/bash /scripts/backup.sh >> /logs/backup.log 2>&1
```

Ascertain the time:

```
at now + 5 minutes 
```

at executes five minutes from now. You can use natural language like 3:30pm or tomorrow or midnight.


Example 1: One-Time Docker Cleanup

Schedule a Docker cleanup for tonight:

```
at 11pm
```

Then enter:

```
docker run --rm craigderington/docker-python /app/cleanup.py >> /logs/cleanup.log 2>&1
```

This runs your craigderington/docker-python cleanup script once at 11:00 PM, removing unused images or containers.


Example 2: Delayed Python Report
Generate a report at 6 AM tomorrow:

```
at 6am tomorrow
```

Then enter:

```
python3 /scripts/report.py >> /logs/report.log 2>&1
```


Your Python script (maybe from craigderington/docker-python) runs once, logging output for review.


Example 3: One-Off Nginx Restart


Restart your craigderington/docker-nginx container at 2 AM:

```
at 2am
```


Enter:

```
docker restart nginx-container >> /logs/nginx_restart.log 2>&1
```

Perfect for applying a config change without cron’s overhead.

Managing at Jobs

List jobs: 

```
atq
```
<small>Shows queued jobs with IDs.</small>

Remove job: 

```
atrm <job-id>
```
<small>Cancels a job.</small>

View job details: 

```
at -c <job-id>
```
<small>Displays a job’s commands.</small>

Logging Output

Like cron, pipe output to logs for debugging:

```
at 8pm
```


Enter:

```
/usr/bin/java -jar /apps/healthcheck.jar >> /logs/healthcheck.log 2>&1
```

This logs your Java app’s health check, keeping your app's nice &amp; tidy.


#### Why at is Obscure
Cron hogs the spotlight for recurring tasks, but at is perfect for one-time jobs like post-meeting scripts or temporary reminders. It’s simple, flexible, and doesn’t clutter your crontab. Use it to automate quick tasks with your craigderington Docker images without overthinking.



#### Pro Tips

- Queue multiple commands: Add multiple lines in the at prompt before Ctrl+D.

- Email notifications: Set MAILTO=admin@example.com in /etc/sysconfig/atd for job output emails.

- Check status: Use systemctl status atd to ensure the daemon’s running.

- at is your one-hit wonder for Linux automation—simple, stealthy, and perfect for your Notes site’s quirky toolkit.
