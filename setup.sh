#Step 1: Update the path in toad.sh to be the location of the toad.py file

#Step 2: open a terminal window and navigate to the TOAD directory

#Step 3: create a symbolic link to the shell script
ln -s toad.sh /usr/local/bin/toad

#Step 4: make the shell script executable
chmod +x toad.sh

#Step 5: Add the directory containing the shell script to your PATH
echo 'export PATH="toad.sh:$PATH"' >> ~/.bashrc
source ~/.bashrc
