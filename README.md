# ToDo Wallpaper

Why: For some reason theres no way to just bind or stick a todo list to my desktop thats a default Windows 11 app...
     There is one but I need to open and close it, and it also is placed above all my applications. I do not like that
     I dont want to download an app that does that because I dont.
     Its an easy program that shouldnt take too long to make. And its simple...

The main function of this program is to change my computer wallpaper
and add a list to it basically

We want to be able to do these functions:
    * Add to list
    * Remove from list
    * Edit from list
    * Color code lines
    * Clear list
    * Choose which monitor - not sure how possible this is without writing/research too much
    * Do all of these by running app.py <commands>

py app.py <monitor - Default will be #2> <ADD/EDIT/RM/DONE/CLS> <the thing todo!/the thing todo/_/_/_> <index/index!/index!/index!/_> <color/color/_/_/_>

Architecture

In terms of architecture I want to utilize
    * Command Pattern
    * State Pattern?
    * A pattern where it mimics a command line interface.
    * !We dont need a complete UI for this, thats overkill!


# Scripts for ease of use
    * Create a file that opens a command line
    * What I did was create a todo.bat in my desktop so when I click that its opens git bash
    * I then added aliases on my .bashrc file
    * These are shortcuts where I could just type 'todo "The name of todo"' and that creates it instead of typing py app.py
    *   while being in the correct directory every time.
    * see todo_bat.txt and bashrc.txt for simple scripts