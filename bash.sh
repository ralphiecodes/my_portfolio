#! /bin/bash
echo "What would you like your commit message to be?"
read message
echo  $(git add .)
echo  $(git commit -m "$message ") 
echo  $(git push origin main) 





