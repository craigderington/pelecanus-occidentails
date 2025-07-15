Title: 50 Linux Commands I Use Regularly
Date: 2025-07-10 19:55
Modified: 2025-07-10 19:55
Category: Linux
Tags: linux, command line, useful commands, shell, terminal
Slug: 50-linux-commands-i-use-on-the-regular
Authors: Craig Derington
Summary: The top 50 Linux commands I use regularly.


## 50 Linux Commands


1. Terminal Commands To Check System Memory.

1.1. The Free Command.
It’s the most frequently used command to track memory usage on Linux.

```
| 123456 | $ free -m              total       used       free     shared    buffers     cachedMem:           993        922         71          0         61        216-/+ buffers/cache:        644        349Swap:         1023          0       1023 |
```
The “-m” option returns the usage data in MB format.



1.2. The </Proc/Meminfo> Command.
Another way to quickly check the memory consumption is by printing the command. You need root or access to run this command.

```
$ sudo cat /proc/meminfo MemTotal:        1017536 kBMemFree:           72092 kBBuffers:           63160 kBCached:           221464 kBSwapCached:          576 kB... |
```




1.3. The <Vmstat> Command.
It reverts with the memory usage in the same way as the command does. But you need not be a root user to run this command.

The VMSTAT command example.Shell
| click me | click me |
| 1234567 | $ vmstat -s      1017536 K total memory       944492 K used memory       406372 K active memory       239000 K inactive memory        73044 K free memory        ... |





1.4. The Top Command.
If you are in a situation, where the memory usage is between 90-100%. Then, you should use top command to determine the process responsible. Most of the time, you can verify the process consuming resources by looking at the <%CPU> or the <%MEM> columns in the top output.

Running the TOP command.Shell
| click me | click me |
| 1 | $ top |


Running Top Command in Terminal
It also allows sorting on the columns. Press (Shift+O) to select a column via field letter. For example, press “a” letter to sort process with PID (Process ID).
Sort Top Command Output
TOC

1.5. The <Htop> Command.
It’s an extension to the top command. And it provides several other options and details along with displaying the memory usage.

Executing HTOP command.Shell
| click me | click me |
| 1 | $ htop |


The top header in its output shows the CPU usage, RAM and swap statistics.
Running HTOP Command in Terminal.
TOC

1.6. Additional Linux Commands To Isolate Memory Issues.
1. Print the top 10 processes consuming a lot of memory.

Print processes consuming a lot of memory.Shell
| click me | click me |
| 123456 | $ ps aux --sort=-resident|head -11USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMANDroot       983  0.3 11.3 286388 115944 tty7    Ss+  14:22   1:11 /usr/bin/X :0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch -background nonetest       1524  0.9  6.4 1073492 65804 ?       Sl   14:22   2:49 compiztest       1550  0.0  2.8 745372 28700 ?        Sl   14:22   0:00 nautilus -ntest       1892  1.2  2.3 526612 24372 ?        Sl   14:22   3:45 /usr/lib/unity/unity-panel-service |


2. Kill a process while running the top command.
Run top and press “k”. It’ll prompt you for the process ID and ask for the signal to kill. You can enter the PID of your choice and provide 15 as the signal value.
Using Top Command to Kill a Process.
3. Modify top command to print the absolute path in its output.
After running top, press “c” to display the processes with full path and arguments.
4. Sort “ps” output by memory usage, from high to low.

SortShell
| click me | click me |
| 1 | $ ps aux --sort -rss |


TOC

2. Terminal Commands To Check Disk/File Usage.

2.1. The Du Command.
It’s one of the standard Linux commands to retrieve the disk usage of files and folders.
1. If you wish to check the disk usage of a folder and its subfolder, then run the following command.

DU command to report disk usage.Shell
| click me | click me |
| 123456789 | $ sudo du /home/techbeamers/4       /home/techbeamers/.X11-unix4       /home/techbeamers/VBoxOGL/system8       /home/techbeamers/VBoxOGL4       /home/techbeamers/ssh-oWoYdKmZ11624       /home/techbeamers/.ICE-unix4       /home/techbeamers/keyring-z6fUcL8       /home/techbeamers/pulse-H52d267kpZZH40      /home/techbeamers/ |


It displays the output in the form of disk blocks. To print in bytes, kilo bytes, mega or Gigabytes, use the “-h” option with du command.
2. To check the total space occupied by a directory, use the “-s” option with the du command.

Another DU command example.Shell
| click me | click me |
| 12 | $ sudo du -sh /home/techbeamers40K     /home/techbeamers |


3. Using “-c” switch will get the total size of the directory including the subdirectories printed at the last line. There is also an “-a” flag to display the usage of all files and folders.
4. With the “–exclude” switch, you can specify a file pattern. Then, the du command will filter the files matching the given pattern.

Exclude files from the DU report.Shell
| click me | click me |
| 1 | $ du -ah --exclude="*.txt" /home/techbeamers |


5. Locate the biggest files in the current directory and sub-directories.

Linux command to find the largest file.Shell
| click me | click me |
| 1 | $ ls -lSrh |


6. Look out for the largest directories.

Using DU command to search for largest directories.Shell
| click me | click me |
| 1 | $ du -kx | egrep -v "\./.+/" | sort -n |


TOC

2.2. The Df Command.
Another Linux command to monitor disk space is df (disk free). Now, let’s see what can we do with it.
1. Print the disk usage of all the file systems.

DF command to print disk usage.Shell
| click me | click me |
| 12345 | $ df -aFilesystem                   1K-blocks    Used Available Use% Mounted on/dev/mapper/vagrant--vg-root 129664620 6684216 116370692   6% /proc                                 0       0         0    - /procsysfs                                0       0         0    - /sys |


2. Use a fixed memory block size.
By default, it prints memory blocks of 1K. But with the “-B” option, we can alter the default memory size.

DF command to print disk usage in 100B blocks.Shell
| click me | click me |
| 12345 | $ df -B 100Filesystem                   100B-blocks     Used  Available Use% Mounted on/dev/mapper/vagrant--vg-root  1327765709 68446372 1191635887   6% /udev                             5099439       41    5099398   1% /devtmpfs                            1041982     7578    1034404   1% /run |


3. Style output to human readable format.
Use “-h” option, it makes the display memory in the form of gigabytes, megabytes, etc.
4. Check the type of available file systems.
You can run the df command with “-T” option to show the type of all file systems.

DF command to show types of all file systems.Shell
| click me | click me |
| 12345 | $ df -TFilesystem                   Type     1K-blocks    Used Available Use% Mounted on/dev/mapper/vagrant--vg-root ext4     129664620 6684216 116370692   6% /udev                         devtmpfs    497992       4    497988   1% /devtmpfs                        tmpfs       101756     740    101016   1% /run |


You can even exclude a file system with -x option. Or provide a type with -t option, it’ll result in displaying the same kind of file systems.

DF command to exclude a file system using its type.Shell
| click me | click me |
| 123 | $ df -t ext2#OR$ df -x ext2 |


TOC

2.3. Additional Terminal Commands For File Management.
There are some other useful tips that you can use to optimizing your disk management tasks.
1. Delete files marked for deletion but not yet deleted.

Delete files marked for deletion.Shell
| click me | click me |
| 1 | $ lsof | grep delete |


2. Search for files more than 100 MB.

Find files occupying more than 100 MB.Shell
| click me | click me |
| 1 | $ find . -size +100M |


3. Check files created within the last one week.

Check files created within the last one week.Shell
| click me | click me |
| 1 | $ find . -mtime -7 |


4. Remove files older than two weeks.

Remove files older than two weeks.Shell
| click me | click me |
| 1 | $ find *.gz -mtime +14 -type f -exec rm {} \; |


5. Monitor a log file for errors or some text.

Monitor a log file for errors.Shell
| click me | click me |
| 1 | $ tail -f file.log | grep -i "error" |


TOC

3. Terminal Commands To Check On Running Processes.

3.1. The Ps Command.
It’s one of the most used Linux commands which returns a preview of the running processes along with their PID, CPU/RAM usage, and other details.
1. Check the Shell you are using.

To known the Shell you are using.Shell
| click me | click me |
| 123 | $ ps -p $$  PID TTY          TIME CMD 2480 pts/1    00:00:00 bash |


2. Check the processes not owned by you.

Check the processes not own by you.Shell
| click me | click me |
| 1 | $ ps aux | grep -v `whoami` |


grep -v option inverts the selection.
3. Remove grep command while filtering the process list.

Find a process while excludingShell
| click me | click me |
| 123 | $ ps aux | grep '[b]ash'#Or$ ps aux | grep bash | grep -v grep |


4. Display all process including params and hierarchy.

Display all process including params and hierarchy.Shell
| click me | click me |
| 1 | $ ps auxww -H |


5. List the files opened by a process.

List the files opened by a process.Shell
| click me | click me |
| 1 | $ lsof -p $PID |


6. Print the process running time since it started.

Print the process running time, since it started.Shell
| click me | click me |
| 123 | # ps -p -o <PID>,etime= $ ps -p 1,2233 -o pid,etime= |


7. Check all threads of a running process.

Check all threads of a running process.Shell
| click me | click me |
| 1234567 | $ ps -C firefox -L -o pid,tid,pcpu,state,nlwp,args  PID   TID %CPU S NLWP COMMAND 3415  3415  5.1 S   29 /usr/lib/firefox/firefox 3415  3421  0.0 S   29 /usr/lib/firefox/firefox 3415  3422  0.0 S   29 /usr/lib/firefox/firefox 3415  3423  0.0 S   29 /usr/lib/firefox/firefox 3415  3424  0.0 S   29 /usr/lib/firefox/firefox |


TOC

3.2. The Kill Command.
Use case – When you’ve to stop a process behaving intermittently and which refuses to close itself. So the kill command comes for rescue in such conditions. Its syntax is as follows.

KILL command syntax.Shell
| click me | click me |
| 1 | $ kill [signal or option] PID(s) |


1. Terminate a process by ID.

Terminate a process by ID.Shell
| click me | click me |
| 1 | $ kill -9 PID or kill -KILL PID |


The “-9” flag refers to KILL signal. Some of the other signals are HUP (-1), SIGINT (-2) and TERM (15).
TOC

3.2. The Killall Command.
Another Linux command which kills a process by name is as follows.

Linux command which kills a process by name.Shell
| click me | click me |
| 1 | $ killall firefox |


You can even kill multiple processes using the single command.

Kill multiple processes using the single command.Shell
| click me | click me |
| 1 | $ killall firefox soffice.bin |


TOC

3.3. The STRACE Command.
It is one of the Linux commands which allows watching a process execution. It intercepts the system calls and signals that a program exercises while running.
1. Trace a program using its PID.

Trace a program using its PID.Shell
| click me | click me |
| 1 | $ strace -f -p $PID |


2. Monitor a process for any specific system call.

Monitor a process for any specific system call.Shell
| click me | click me |
| 1234567 | $ strace -e open touch test.txtopen("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3open("/lib/x86_64-linux-gnu/librt.so.1", O_RDONLY|O_CLOEXEC) = 3open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3open("/lib/x86_64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3open("/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3open("test.txt", O_WRONLY|O_CREAT|O_NOCTTY|O_NONBLOCK, 0666) = 3 |


TOC

3.4. The Watch Command.
Sometimes, we need to monitor a process at regular intervals. For example, tracking the progress of copying a large release build or folder. That’s where the watch command is useful.
1. Run ls command after every 1 second.

Run LS command after every 1 second.Shell
| click me | click me |
| 1 | $ watch -n 1 ls -l |


2. See the differences between previous and present output.

WATCH to differentiate between previous and present output.Shell
| click me | click me |
| 1 | $ watch -d -n 1 free |


You can anytime press CTRL+z to take control back from the watch command.
TOC

4. Terminal Commands To Monitor & Manage Network.

4.1. The IFCONFIG And Related Commands.
The most common usage of command is to return the IP address of the system you are using. But you can also use it to initialize an interface, assign a new IP address and enable/disable the interface.
1. The below command will print the IP address of the current machine.

Print the IP address of the current machine.Shell
| click me | click me |
| 1234567891011121314151617 | $ ifconfigeth0      Link encap:Ethernet  HWaddr 08:00:27:4d:2e:ff          inet6 addr: fe80::a00:27ff:fe4d:2eff/64 Scope:Link          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1          RX packets:0 errors:0 dropped:0 overruns:0 frame:0          TX packets:1999 errors:0 dropped:0 overruns:0 carrier:0          collisions:0 txqueuelen:1000          RX bytes:0 (0.0 B)  TX bytes:400055 (400.0 KB) eth1      Link encap:Ethernet  HWaddr 08:00:27:d8:13:46          inet addr:192.168.1.6  Bcast:192.168.1.255  Mask:255.255.255.0          inet6 addr: fe80::a00:27ff:fed8:1346/64 Scope:Link          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1          RX packets:16660 errors:0 dropped:0 overruns:0 frame:0          TX packets:16506 errors:0 dropped:0 overruns:0 carrier:0          collisions:0 txqueuelen:1000          RX bytes:10200264 (10.2 MB)  TX bytes:2778520 (2.7 MB) |


2. To print the information related to a particular interface, run the following.

Print the information related to a particular interfaceShell
| click me | click me |
| 1 | $ ifconfig eth0 |


3. Assign IP address and set gateway.

Assign IP address and set gateway.Shell
| click me | click me |
| 1 | $ ifconfig eth0 192.168.1.1 netmask 255.255.255.0 |


4. Enable/disable an interface.

Enable/disable an interface.Shell
| click me | click me |
| 12 | $ ifup eth0$ ifdown eth0 |


TOC

4.2. Some Nice Ping Command Examples.
It’s basically to find out whether a machine on the network or the gateway is reachable. Here are some good examples.
1. Increase/decrease ping time interval.

Increase/decrease ping time interval.Shell
| click me | click me |
| 12 | $ ping -i 2 target$ ping -i 0.1 target |


2. Check if local I/F is active.

Check if local I/F is active.Shell
| click me | click me |
| 12 | $ ping 0$ ping localhost |


3. Update the size of the ping packet.

Update the size of the ping packet.Shell
| click me | click me |
| 1 | $ ping -s 112 localhost |


The above command changes the default packet size from 56 to 112.
4. Timeout a ping request.

Timeout a ping request.Shell
| click me | click me |
| 1 | $ ping -w 5 localhost |


5. Send X no. of packets and stop.

Send X no. of packets and stop.Shell
| click me | click me |
| 1 | $ ping -c X IP_ADDRESS |


TOC

4.3. The TRACEROUTE Command.
It’s for troubleshooting the network issues. It prints the no. of hops taken to reach the target.

TRACEROUTE Command example.Shell
| click me | click me |
| 12345 | $ traceroute ubuntu.comtraceroute to ubuntu.com (91.189.94.40), 30 hops max, 60 byte packets 1  D-Link.Home (192.168.1.1)  4.566 ms  4.960 ms  5.038 ms 2  abts-north-static-236.220.160.122.airtelbroadband.in (122.160.220.236)  36.117 ms  37.111 ms  38.686 ms 3  abts-north-static-181.130.160.122.airtelbroadband.in (122.160.130.181)  39.867 ms  41.269 ms * |


TOC

4.4. The NETSTAT Command.
This command allows a user to monitor both incoming and outgoing network connections. Most of the operating systems support this command. Let’s see some of its real-time applications.
1. Listing all TCP and UDP connections opened at a time.

Listing all TCP and UDP connections.Shell
| click me | click me |
| 1 | $ netstat -a | more |


2. List connections without resolving host, port and user name.

List connections without resolving host, port and user name.Shell
| click me | click me |
| 1 | $ netstat -an |


3. Listing only TCP connections.

Listing only TCP connections.Shell
| click me | click me |
| 1 | $ netstat -at |


4. Listing only UDP connections.

Listing only UDP connections.Shell
| click me | click me |
| 1 | $ netstat -au |


5. Display TCP connections in Listen state.

Display TCP connections in Listen state.Shell
| click me | click me |
| 1 | $ netstat -lt |


6. Display UDP connections in Listen state.

Display UDP connections in Listen state.Shell
| click me | click me |
| 1 | $ netstat -lu |


7. Display service names with PID.

Display service names with PID.Shell
| click me | click me |
| 1 | $ netstat -tp |


8. Print routing table summary.

Print routing table summary.Shell
| click me | click me |
| 1 | $ netstat -r |


9. Retrieve IP address statistics.

Retrieve IP address statistics.Shell
| click me | click me |
| 1 | $ netstat -g |


10. Locate all programs in Listen state.

Locate all programs in Listen state.Shell
| click me | click me |
| 1 | $ netstat -ap | grep http |


11. Find the port of a program is using.

Find the port of a program is using.Shell
| click me | click me |
| 1 | $ netstat -ap | grep ssh |


12. Show all ports listening with process PID.

Show all ports listening with process PID.Shell
| click me | click me |
| 1 | $ netstat -tlnp |


TOC

4.5. The Dig Command.
The full form of DIG command is domain information groper. It retrieves the DNS details like A record, CNAME, and MX records.

The DIG command example.Shell
| click me | click me |
| 12345678910111213141516 | $ dig www.google.com; <<>> DiG 9.8.1-P1 <<>> www.google.com;; global options: +cmd;; Got answer:;; ->>HEADER< ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0 ;; QUESTION SECTION:;www.google.com. IN A ;; ANSWER SECTION:www.google.com. 261 IN A 216.58.196.68 ;; Query time: 35 msec;; SERVER: 127.0.0.1#53(127.0.0.1);; WHEN: Thu Sep 8 16:55:01 2016;; MSG SIZE rcvd: 48 |


1. Display only MX Records.

Display only MX Records.Shell
| click me | click me |
| 12345 | $ dig -t MX ubuntu.com +noall +answer ; <<>> DiG 9.8.1-P1 <<>> -t MX ubuntu.com +noall +answer;; global options: +cmdubuntu.com. 2845 IN MX 10 mx.canonical.com. |


2. Display only NS Records.

Display only NS Records.Shell
| click me | click me |
| 12345678 | $ dig -t NS ubuntu.com +noall +answer ; <<>> DiG 9.8.1-P1 <<>> -t NS ubuntu.com +noall +answer;; global options: +cmdubuntu.com. 1328 IN NS ns3.p27.dynect.net.ubuntu.com. 1328 IN NS ns2.p27.dynect.net.ubuntu.com. 1328 IN NS ns4.p27.dynect.net.ubuntu.com. 1328 IN NS ns1.p27.dynect.net. |


TOC

4.6. Miscellaneous Network Linux Commands.
1. Display all TCP sockets in use.

Display all TCP sockets in use.Shell
| click me | click me |
| 123 | $ lsof -nPi tcpCOMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAMEubuntu-ge 1957 vagrant 11u IPv4 12280 0t0 TCP 192.168.1.6:42056->91.189.94.25:80 (CLOSE_WAIT) |


2. Resolve IP address from the hostname.

Resolve IP address from the hostname.Shell
| click me | click me |
| 1 | $ host ubuntu.com |


3. MTR – Top like traceroute command.
It combines the functionality of traceroute and ping tools. It examines the connectivity between the host and the given target system.

Top like traceroute command.Shell
| click me | click me |
| 1 | $ mtr google.com |


TOC

5. Linux Commands To Configure Terminal & Screen.

5.1. The Screen Command.
It might now be available on your system by default. So, to install it either use apt or yum as per the distribution you are using.
1. Start a screen session as the current user.

Start a screen session.Shell
| click me | click me |
| 1 | $ screen -x |


2. Reattach to a screen session.

Reattach to a screen session.Shell
| click me | click me |
| 1 | $ screen -r |


3. Record a terminal session.

Record a terminal session.Shell
| click me | click me |
| 1 | $ script file.out 2> file.rec |


4. Play back a recorded terminal session.

Play back a recorded terminal session.Shell
| click me | click me |
| 1 | $ scriptreplay file.rec file.out |


TOC

5.2. Some Useful Terminal Command Shortcuts.
1. Open a new terminal.

Open a new terminal.Shell
| click me | click me |
| 1 | Press CTRL+ALT+t |


2. Open a new tab in the existing terminal window.

Open a new tab.Shell
| click me | click me |
| 1 | Press CTRL+SHIFT+t |


3. Clear the screen.

Clear the screen.Shell
| click me | click me |
| 1 | Press CTRL+l or type clear and enter. |


4. Cache console output.

Cache console output.Shell
| click me | click me |
| 1 | $ script my.terminal.session |


TOC

6. Some Important Terminal Commands For Quick Reference.
1. How to run a previous command as root?

Run Previous command as root.Shell
| click me | click me |
| 1 | $ sudo !! |


2. How to find differences between two directories?

Find differences between two directories.Shell
| click me | click me |
| 1 | $ diff -y <(ls -l ${DIR1}) <(ls -l ${DIR2}) |


3. How to lock a directory.

Lock a directory.Shell
| click me | click me |
| 1 | $ chmod 0000 /test |


The root user will still have access. To restore the permission, run the below command.

To restore the normal permissions.Shell
| click me | click me |
| 1 | $ chmod 0755 /test |


4. Smart cd commands.

Smart CD commands.Shell
| click me | click me |
| 12345 | #To change to last working directory.$ cd - #To return to your home directory.$ cd |


5. How to replace same text in multiple files.
To replace the text Apple with Linux in all text files in current directory and down you can run this.

Replacing same text in multiple files.Shell
| click me | click me |
| 1 | $ find . -name '*.txt' -print | xargs perl -pi -e's/Apple/Linux/ig' *.txt |


6. Listing files changed today.
Sometimes, we create a file during the day and forget what name we gave it. So here is the command to locate such files.

Listing files changed today.Shell
| click me | click me |
| 1 | $ ls -al --time-style=+%D | grep `date +%D` |


7. Shorten long commands.
Not all of us has the ability to memorize the long Linux commands. With the below command, we can assign user-friendly names in such cases.

Shorten long commands.Shell
| click me | click me |
| 1 | $ alias ls="ls -al" |


8. Copy a file into multiple directories.

Copy a file into multiple directories.Shell
| click me | click me |
| 1 | $ echo /home/dir1 /test/dir2 /prod/dir3 | xargs -n 1 cp -v /path/to/file |


9. Disable incoming ping requests.
To block a flood of incoming pings, do the following.

Block a flood of incoming pings.Shell
| click me | click me |
| 1 | $ sysctl -w net.ipv4.icmp_echo_ignore_all=1 |


To turn the above setting back, run the below command.

Turn the above setting back.Shell
| click me | click me |
| 1 | $ sysctl -w net.ipv4.icmp_echo_ignore_all=0 |


10. Some cool Nautilus tricks.
• Press CTRL+l to open a location.
• Use CTRL+up to open the parent directory.
• Press arrow keys to navigate through folders.


