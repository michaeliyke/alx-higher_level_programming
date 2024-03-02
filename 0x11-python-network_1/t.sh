#!/usr/bin/env bash
aliases=(
	"cls=clear"
	"where=which"
	"md=mkdir"
)

# Check if a query has a match within the user bashrc file
function in_bashrc()
{
	query=$1
	grep -q "$query" ~/.bashrc # -q for quiet so no outputs
	return $?
}

# Reload the userbashrc file
function reload()
{
	source ~/.bashrc
	echo "Reload successful!"
}

rc=~/.bashrc # The bashrc file to be modified

echo "INSTALL REGULAR ALIAS COMMANDS"
for e in "${aliases[@]}";
do
	# check if it exists in .bashrx
	alias_nm="${e%%=*}"
	if in_bashrc "^alias $alias_nm=";
	then
		echo "Already set: $alias_nm"
	else
		echo "Setting: alias $alias_nm"
		echo "alias $e" >> $rc;
	fi
done
echo

echo "INSTALL THE ~/BIN USER PATH"
bn=$(realpath ~/bin)
if in_bashrc "export PATH=$bn:";
	then
		echo "PATH already set: $bn"
	else
		echo "Setting path: $bn"
		echo "export PATH=$bn:$PATH" >> $rc
	fi
echo
