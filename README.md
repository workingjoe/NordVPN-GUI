# NordVPN-GUI
NordVPN GUI for Linux

* tried making stand-alone executable, and the pipes don't seem to work right.  There likely is some kind of 'current working directory' that needs to be set, or maybe this binary needs to be in the path.  I dunno.

# NEED TO REVIEW WHOLE PROGRAM listening to these suggestions!!
* [Better ways to shell in Python](https://betterprogramming.pub/the-right-way-to-run-shell-commands-from-python-c05f0b9d6cb7)

---
* The general rule of thumb should be to use native functions instead of directly calling other programs or OS commands. So, first, let’s look at the native Python options:

1. pathlib — If you need to create or delete a file/directory; check if a file exists; change permissions; etc., there's absolutely no reason to run system commands. Just use pathlib, it has everything you need. When you start using pathlib, you will also realise you can forget about other Python modules, such as glob, or os.path.
2. tempfile — Similarly, if you need a temporary file just use tempfile module, don't mess with /tmp manually.
3. shutil — pathlib should satisfy most of your file-related needs in Python, but if you need, for example, to copy, move, chown, which or create an archive, then you should turn to shutil.
4. signal — in case you need to use signal handlers.
5. syslog — for an interface to Unix syslog.

*If none of the above built-in options satisfy your needs, only then it makes sense to start interacting with OS or other programs directly.
---
