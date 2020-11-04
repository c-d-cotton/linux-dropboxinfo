# Introduction
Generate popup messages if Dropbox has not synced for a while. (I sometimes find that it stops working for some reason.)

# Installation
Uses Python. Also need to be able to run `dropbox status`.

<!---INSTALLATION_STANDARD_START.-->
I found standard methods for managing submodules to be a little complicated so I use my own method for managing my submodules. I use the mysubmodules project to quickly install these. To install the project, it's therefore sensible to download the mysubmodules project and then use a script in the mysubmodules project to install the submodules for this project.

If you are in the directory where you wish to download linux-dropboxinfo i.e. if you wish to install the project at /home/files/linux-dropboxinfo/ and you are at /home/files/, and you have not already cloned the directory to /home/files/linux-dropboxinfo/, you can run the following commands to download the directory:

```
git clone https://github.com/c-d-cotton/mysubmodules.git getmysubmodules
python3 getmysubmodules/singlegitmodule.py linux-dropboxinfo --downloadmodule --deletegetsubmodules
```

The option --downloadmodule downloads the actual module before installing the submodules. The option --deletegetsubmodules deletes the getsubmodules project after the submodules are installed.

If you have already downloaded projectdir to the folder /home/files/linux-dropboxinfo/, you can add the submodules by running the following commands from the directory /home/files/:
```
git clone https://github.com/c-d-cotton/mysubmodules.git getmysubmodules
python3 getmysubmodules/singlegitmodule.py linux-dropboxinfo --deletegetsubmodules
```
<!---INSTALLATION_STANDARD_END.-->


