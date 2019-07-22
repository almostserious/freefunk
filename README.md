# freefunk
This is a custom component for Home Assistant enabling the use of the Freenet-Funk-API 

## Installation
Copy all files from custom_components/freefunk/ to custom_components/freefunk/ inside your config Home Assistant directory.

### Configuration
Add the following to your config
```
freefunk:
  username: !secret freefunk_username
  password: !secret freefunk_password
```
