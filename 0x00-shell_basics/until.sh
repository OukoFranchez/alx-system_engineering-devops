#!/usr/bin/env bash

count=1

until [ $count -gt 5 ]
do
	echo "Iteration $count"
	count=$((count + 1))
done

echo "Loop finished"
