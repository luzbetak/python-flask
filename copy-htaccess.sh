#!/bin/bash
#---------------------------------------------------#
#for OUTPUT in $(find . -name page.html)
# for OUTPUT in $(find . -mtime 0 -type d)
#---------------------------------------------------#
for OUTPUT in $(find . -type d )
do
    echo "cp -f .htaccess $OUTPUT"
    cp -f .htaccess $OUTPUT
done

#---------------------------------------------------#
# Allow Google to access Caltech files
#---------------------------------------------------#
# rm .htaccess
# cd Caltech/
# find . -name ".htaccess" -exec rm -rf {} \;
#---------------------------------------------------#
