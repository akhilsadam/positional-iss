pytest
wsl -d Ubuntu-20.04 << EOF
echo $PWD
make kill
make clean
make build
make test
make run
EOF