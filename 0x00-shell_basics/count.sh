#!/usr/bin/env bash
count=1

while [ $count -le 5 ]
do
	echo "Iteration $count"
	count=$((count + 1))
done

echo "Loop Finished"