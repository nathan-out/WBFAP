# WBFAP
Windows browser forensic artifacts parser. Based on SANS poster.

## Forensic Artifacts supported

From the SANS poster, these Chrome artifacts are curently supported (based to the SANS poster) :

### History and Download History 

*History and Download History records websites visited by date and time.*

- XP: `%USERPROFILE%\Local Settings\Application Data\Google\Chrome\User Data\<Profile>\History`
- Win7+: `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\History`
- Win7+: `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\History`

Web browser artifacts are stored for each local user account. Most browsers also record number of times visited (frequency). Look for multiple profiles in Chromium browsers, including “Default”, and “Profile1”, etc.

### Media History

*Media History tracks media usage (audio and video played) on visited websites (Chromium browsers).*

-  `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\Media History`
-  `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\Media History`

Three primary tables: playbackSession, origin, playback. Includes URLs, last play time, watch time duration, and last video position. Not cleared when other history data is cleared.

### HTML5 Web Storage

*HTML5 Web Storage are considered to be “Super Cookies”. Each domain can store up to 10MB of text-based data on the local system.*

- `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\Local Storage`
- `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\Local Storage`

Chrome uses a LevelDB database, Firefox uses SQLite, and IE/EdgeHTML store data within XML files.

### HTML5 FileSystem

*HTML5 FileSystem implements the HTML5 local storage FileSystem API. It is similar to Web Storage, but designed to store larger binary data.*

-  `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\File System`
-  `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\File System`

A LevelDB database in this folder stores visited URLs and assigned subfolders to locate the data. Files are stored temporarily (“t” subfolders) or in permanent (“p” subfolders) storage.

### Auto-Complete Data 

*Many databases store data that a user has typed into the browser.*

- `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\History`
- `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\History`
  *keyword_search_terms – items typed into various search engines*
- `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\Web Data`
- `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\ Web Data`
   *Items typed into web forms*
- `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\Shortcuts`
- `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\ Shortcuts`
  *Items typed in the Chrome URL address bar (Omnibox)*
- `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\Network Action Predictor`
- `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\ Network Action Predictor`
  *Records what was typed, letter by letter*
- `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\<Profile>\Login Data`
- `%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\<Profile>\ Login Data`
  *Stores inputted user credentials*
