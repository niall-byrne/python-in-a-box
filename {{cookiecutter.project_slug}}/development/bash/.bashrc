# Bash Environment For Dev Environment

PS1='${git_branch}${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Load The Development CLI and Bash Git Support
source scripts/dev
source /home/user/.bash_git_support

# Customize Your Path Here
export PATH="${PATH}"
