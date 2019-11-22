#!/bin/sh

file=
num_episode=300
num_iter=5
problem=

while [ "$1" != "" ]; do
	case $1 in
		-inp )
			shift
			file=$1
			;;
		-ne )
			shift
			num_episode=$1
			;;
		-rs )
			shift
			num_iter=$1
			;;
		-tp )
			shift
			problem=$1
			;;
	esac
	shift
done

python3 main.py $file $num_episode $num_iter $problem