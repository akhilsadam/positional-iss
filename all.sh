pytest
(
wsl -d Ubuntu-20.04 << EOF
echo $PWD
make kill

EOF
)