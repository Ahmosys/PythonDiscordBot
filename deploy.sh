#!/bin/bash

# Vars
alreadyExist=false
githubLink=""
directoryName=""

# Define color code
NC='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
WHITE='\033[1;37m'
BLINK='\033[5m'


# Function started at the execution of the script
function run() {
	checkIfRepoExist
	cloneOrPull
	# installPythonRequirement
	clear
	python3 main.py
}

# Check if the repository as already cloned.
function checkIfRepoExist() {

	if [[ -d $directoryName ]]; then
		printMessage "success" "The repository has already been cloned."
		alreadyExist=true
	else
		printMessage "wrong" "The repository don't exist."
		alreadyExist=false
	fi
}

# Install the python requirements
function installPythonRequirement() {
	printMessage "success" "Installing python requirements..."
	pip3 install -r requirements.txt
	if [[ $? -eq 0 ]]; then
		printMessage "success" "Requirements has been installed."
	else
		printMessage "error" "Requirements has not been installed."
	fi
}

# Check if package is already installed or not.
function checkIfPackageIsInstalled() {
	if [[ ! -x $(which $1) ]]; then
		printMessage "error" "${1^} is not installed... Installing it."
		apt-get install $1 -y &> /dev/null
		if [[ $? -eq 0 ]]; then
			printMessage "success" "${1^} has been installed."
		else
			printMessage "error" "${1^} has not been installed."
		fi
	else 
		printMessage "success" "${1^} is already installed."
	fi
}

# Clone or pull the repository.
function cloneOrPull() {
	if [[ $alreadyExist == false ]] ; then
		printMessage "success" "Cloning the repository in the current directory..."
		git clone $githubLink &> /dev/null
		cd $directoryName
	else
		cd $directoryName
		printMessage "success" "Pulling the repository..."
		git pull $githubLink &> /dev/null
	fi
}

# Print message.
function printMessage() {
	if [[ $1 == "success" ]]; then
		echo -e "[+] ${GREEN}$2 $NC"
	elif [[ $1 == "error" ]] ; then
		echo -e "[-] ${RED}$2 $NC"
	elif [[ $1 == "wrong" ]] ; then
		echo -e "[!] ${YELLOW}$2 $NC"
	elif [[ $1 == "question" ]] ; then
		echo -e "[?] ${BLUE}$2 $NC"
	fi
}

# Entry point
function main(){
	clear
	checkIfPackageIsInstalled git
	checkIfPackageIsInstalled python3
	checkIfPackageIsInstalled python3-pip
	pattern="^(https|git)(:\/\/|@)([^\/:]+)[\/:]([^\/:]+)\/(.+)(.git)*$"
	read -p "[?] Provide the repository link : " githubLink
	if [[ $githubLink =~ $pattern ]]; then
		printMessage "success" "Correct repository link run the installation..."
		directoryName="$(echo $githubLink | sed -r 's/.+\/([^.]+)(\.git)?/\1/')"
		run
	else
		printMessage "error" "The repository link is not valid!"
	fi
}

# Execution
main