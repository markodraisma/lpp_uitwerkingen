CURSUS=/usr/atcomp/cursus; export CURSUS

FCEDIT=/bin/vi ; export FCEDIT
EDITOR=/bin/vi ; export EDITOR
PATH=::$CURSUS/pythone/Python/bin:$STANDARD_PATH; export PATH

ulimit -c 0

echo Welcome to the course Learn to program in Python

stty intr ^C
PS1='[\W]$ ' # prompt with basename of current dir. bash-only
