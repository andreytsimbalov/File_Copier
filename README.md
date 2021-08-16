# File_Copier

A program that copies files in accordance with the configuration file.

# User's manual

To start the copier, you need to run **file_copier.py**

The configuration file must be in xml format. 
For each file, the configuration file must contain its name, source path and path where the file is to be copied.

Example 
**config.xml** file:

    <config>
        <file
                source_path="C:\Windows\system32"
                destination_path="C:\Program files"
                file_name="kernel32.dll"
        />
        <file
                source_path="var/log"
                destination_path="etc"
                file_name="server.log"
        />
    </config>



