# Diary-Encryptor
A Personal journal 

===============================================
               Encryptor v1.17
-----------------------------------------------
                Python Package
===============================================
-----------------------------------------------
Description:
   
   This Project Aims to show light on the hashing and encryption modules
   and its real life applications. The Program Opens up a Main Window from
   where the user can login or register a new "account" which uses the 
   hashing methods to store the password of the user safely in a file using
   File Handling and the hashlib module

   Once the User Logs in they are presented with a text box which is unique for
   Every User(basically a personal diary with a password for privacy). The user 
   can store any string in the text box and then click on
   the Proceed Button. This Encrypts the Data on the text box and stores it
   in a file.These files are unique for each user.The Encryption is done using
   a module called Fernet under the cryptography module.

   When the same user logs back in his/her data will be displayed in the same
   text box for them to use or read


-----------------------------------------------

Modules Used:

+-----------------+------------------+------------------+
|                 |                  |                  |
|   Module Name   |   Description    |  Use in Program  |
|                 |                  |                  |
+-----------------+------------------+------------------+
|                 | Used for making  | For making       |
|    tkinter      | Interactable GUIs|       Windows    |
+-----------------+------------------+------------------+
|                 | Used for         | For hashing      |
|    hashlib      |      Hashing     |       passwords  |
+-----------------+------------------+------------------+
|                 | Used for making  | For Generating   |
|     uuid        | random UUIDs     | Salt for Hashing |
+-----------------+------------------+------------------+
|                 | Used for         | For Deleting  &  |
|      os         |  various things  |  Adding Files    |
+-----------------+------------------+------------------+
|                 | Part of          | Used for         |
|    Fernet       |    cryptography  |    Encryption    |
+-----------------+------------------+------------------+
|                 |  Storing Binary  | Used for storing |
|    pickle       |       Data       | Encryption key   |
+-----------------+------------------+------------------+

Credits:

 - Nanda Pranesh S
 - Varun S

-----------------------------------------------

Contacts:
 - 21pc19@psgtech.ac.in
 - 21pc25@psgtech.ac.in

----------------------------------------------
===============================================
                  Thank You!
===============================================
