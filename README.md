# freefunk
This is a custom component for Home Assistant enabling the use of the Freenet-Funk-API 

Currently this will only show the current state of your Freenet Funk Contract in the entity: freefunk.status
The Goal is to have a system that enables you to: "Pause & Forget". Meaning whenever the autoreactivation (every 14days) happens, the pause will be triggered automatically if previously set by the user.

Also I'd like to enable the booking of both options via this component so it can be used by various triggers of Home Assistant (i.e.: If fixedline Internet is down, book the LTE FLAT)

## Installation
Copy all files from custom_components/freefunk/ to custom_components/freefunk/ inside your config Home Assistant directory.

### Configuration
Add the following to your config
```
freefunk:
  username: !secret freefunk_username
  password: !secret freefunk_password
```
