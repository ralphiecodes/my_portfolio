#! /bin/bash
echo "What do you want to do?"
read command


if [[ $command == "branch" ]]; then

    echo "which branch do you want to work on?"
    read branch
    echo $(git checkout $branch)

elif [[ $command == "commit" ]]; then

    echo "What would you like your commit message to be?"
    read message
    echo  $(git add .)
    echo  $(git commit -m "$message ") 
    echo  $(git push origin $branch) 

else
    echo "That's not a valid command"
fi




