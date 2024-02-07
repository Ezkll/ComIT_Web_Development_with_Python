
#### *Lecture Notes:*

>This will contain lecture notes from the ComIT course: Web Development with Python
---

#### *Homework: Creating and Initializing a Repository*
>1. Open your command line application (Terminal).
>2. Create a helloworld.py application (Vim, Vi, Nano)
>3. Recreate the steps required to create your repo on github.com
>4. Setup your helloworld.py app under source control.
>5. Push your app up to your own repo.
#### *1. Open your command line application (Terminal).*
#### *2. Create a helloworld.py application*
1.	Navigate to the ComIT folder
>I did Item 3 of the homework before this.

``echo print(Hello World!) > helloworld.py``
#### *3. Recreate the steps required to create your repo on github.com*

 1. Install GitHub CLI

 > This will be used for creating a repo through the command line

 2. Install Git Bash

 > In my situation, I had to setup my SSH, I wanted it to do everything through the terminal, I can't really remember if I did everything 100% with the keygen and stuff

 3. Launch cmder
 4. Navigate to the directory you want your repository to reside
 ``cd github``
 5. Create Folder
``md ComIT``
 6. Navigate to New Directory
``cd ComIT``
 7. Initialize Git Repository
``git init``
 8. Connect the remote repository
``git remote add origin git@github.com:ezkll/ComIT_Web_Development_with_Python.git``
 9. Create a repository
``gh repo create ComIT_Web_Development_with_Python --private``
 10. Create a markdown file for your lecture notes
``echo "This will contain lecture notes from the ComIT course: Web Development with Python" > Lecture_Notes.md``
 11. Add changes to the staging area
``git add .``
 12. Commit changes
``git commit -m Creating this Repository. Pre-requisite is to create a file first"``
 13. Push to Repository
``git push -u origin master``
#### *4. Setup your helloworld.py app under source control.*
>Homework Item 3 has done this 
#### *5. Push your app up to your own repo.*
>Step 13 of Homework Item 3 has done this 
---
#### *Lessons Learned:*
- There may be some software dependencies
- Use Git Bash for adding ssh its a bit finicky on windows or in cmder *im not sure*
