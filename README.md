# Automate repetitive keyboard and mouse tasks with python3

### William Lamb 09/22/18

For Mac using python3
On Mac the keylogger portion needs sudo privileges to capture non-special characters.

##### Dependencies:
- pyautogui
- pynput

### Disclaimer
This project is not intended for use in any illegal or nefarious way, rather only to provide a simple method of automating recurring, identical tasks.

### Notes:
- for an alphanumeric key, the `key` variable returns the key in single quotation marks, like `'a'`. For an alphanumeric key using `key.char` the key returns just as is, like `a`.

#### TODO:
- Write a timer class
- Writing characters with combinations like option-c (which outputs ç) and then letting go of option before c doesn't clear the ç character. Should letting go of the option key clear the entire keysPressed list? Should there be a track of how many keypresses before a key is released, and return an array with that many items cut from the end?
- Encapsulate key and mouse loggers into single class
- send log to text file with each new action on a new line
- interpret text file back into actions
- implement saving logs to file to store for later recall
- encrypt saved logs based on read-in buffer file sizes? Add (random) filler to end of file/end of line to hit buffer size? Would there ever be a file large enough that the program can't read the whole thing in at once to unencrypt? Does the program need the whole file to unencrypt a section?  Ask for password to encrypt and decrypt
- add data compression option on mouse moves

### Future possibilities:
- add gui/create desktop program to allow users to edit each step individually
