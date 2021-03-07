SHOW_AND_TELL = """A uses pacman as a package manager.

Q: List files
A: ls -l
Q: Count files in a directory
A: ls -l | wc -l
Q: Disk space used by home directory
A: du ~
Q: Replace foo with bar in all .py files
A: sed -i .bak -- 's/foo/bar/g' *.py
Q: Delete the models subdirectory
A: rm -rf ./module
Q: Firewall all incoming connections to port 22 on this machine
A: iptables -A INPUT -p tcp --dport 22 -j DROP
Q: Clean up /boot/ from old kernel versions on arch linux
A: pacman -Qo /boot/* | grep linux | awk '{print $2}' | xargs rm -rf
Q: btw install nginx
A: sudo pacman -S nginx"""