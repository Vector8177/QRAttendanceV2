# QR Code Attendance V2

This project is a QR-based attendance system that utilitizes JSON data storage and allows for exports to CSV files

## Installation and Usage

Simply install the latest release (Only Windows supported as of now), unzip the zip file, and run the main.exe file. 
In order to use the app, you will have to input the member data into the left textbox under the Manage Members tab. Each member should have their own line, and each line should look like this 

<id>  <name> 
(ensure that the number and name are separated by a TAB, the decoder will not work otherwise)

After you've done this, simply restart the app, and you should see the updated member list on the main tab. By default, the app is intended to fit 40 members on the screen without scrolling, however, if there are more members, you will need to scroll down to view them. 

## Documentation
The app is broken down into two main tabs: Member Dashboard and Member Management.

### Member Dashboard

This is the centralized hub for all things directly related to attendance tracking, including the attendance overview, manual sign in entry, and QR Scanner launch. 

The attendance overview, by default, is setup to display all stored members in rows of 4. When a member is not signed in (such as on startup), their name will show up as red, and when they sign in, it will turn green. Each member's name is a button that can be clicked to toggle whether or not they are signed in. 

In the upper right hand corner of this tab, you can find a textbox for manual signing that users can enter their ID number into to sign themselves in (but not sign themselves out). Under this, you will see a button for launching the QR scanner. Once you hit this button, the QR scanner will launch and a camera preview will be visible on the screen (if you are using an external camera, this may take up 25-30 seconds). Then, each user can scan a QR code (that contains their ID number) to sign in AND sign out.

<h3>IMPORTANT NOTE:</h3> When logging the attendance for each member, the system will only take the most recent session into account, so ensure that you are only signing in and out once!

Lastly, there is also a "Sign Out All" button that will sign everyone out and log attendance.


### Member Management

This is the place for managing the member data or viewing individual member attendance. Member data can also be exported in CSV format for easy input into Google Sheets

On the left side, you will see a large textbox, this is where you will enter member info to be added to the JSON file. **DO NOT add existing members as this will wipe out their attendance data**. Data is to be entered in this format

<id>  <member>
<id>  <member>

The separator between id and member _must_ be a tab character. If you are directly copy-pasting from Google Sheets or Excel, this is the default way that the data will be pasted so you do not need to worry about this.

After you have entered the member data, simply hit the "Generate JSON" button and new entries will be generated for the members. 

You will also see a "Export JSON" button, which will export the attendance data into your downloads folder in a directory called "Attendance Data - <year>-<year>" where <year>-<year> represents the current academic year, i.e. July 2023 - June 2024, it will say 'Attendance Records - 2023-2024. Each individual csv file will be named according to the date of its creation in its respective directory.

There is also a "Clear JSON" button that will completely wipe the JSON file after asking for a password confirmation. In order to edit the password, however, you will have to alter the source code and then rebuild the project using cxFreeze.

Moving on, on the right side of the Member Management tab, there is a lookup section that will pull individual attendance data for each member using an ID inputted into the text box at the top of the section.
