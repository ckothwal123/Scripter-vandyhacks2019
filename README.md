# vandyhacks2019
Repository for Vandyhacks 2019

Scripter

An application to help scriptwriters to write script involving multiple roles and hear playback of the script written.

User logs in and enters the number of roles in the play. Then user is prompted to enter the details of each character in the play such as name, gender etc. User then enters the dialogues in the entire script. Once the script is submitted, the user can view the script or request a playback of the script. When the user selects to view the script, the script is displayed with an option to edit the dialogues. When user requests to hear the playback, the user is sent or streamed an audio file that contains all the dialogues played in their respective gender voices.

Technical Details:

Input the dialogues of the script from the user in a form and then send it to the database once the script is complete. (React.js)

Retrieve the dialogues from the database and send to Google API to convert from text to speech. Save the processed speech and stitch it together. (Django Application)

