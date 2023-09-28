for file in *
do
	echo "File: $file"
done
for file in $(ls /etc)
do
	echo "File in /etc: $file"
done
