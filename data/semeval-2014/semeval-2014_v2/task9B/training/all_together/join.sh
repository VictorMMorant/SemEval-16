cat $1 | awk '{if (NF == 0) print $0; else if ($3=="@") print $1,$3,$3,$4; else print $0;}' > a
cat a | awk '{if (NF == 0) print $0; else if ($3=="#") print $1,$3,$3,$4; else print $0;}' > b
cat b | awk '{if (NF == 0) print $0; else if ($3=="$") print $1,$3,$3,$4; else print $0;}' > c
cat c | awk '{if (NF == 0) print $0; else if ($3=="U") print $1,$3,$3,$4; else print $0;}' > d
cat d | awk '{if (NF == 0) print $0; else if ($3==",") print $1,$3,$3,$4; else print $0;}' > joined_file.txt
rm a
rm b
rm c
rm d
