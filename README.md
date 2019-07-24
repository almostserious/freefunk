# freefunk
This is a custom component for Home Assistant enabling the use of the Freenet-Funk-API 

Currently this will update the current state of your Freenet Funk Contract in the entity: freefunk.status
There are 4 Service Calls available:

freefunk.update --> Update the current status
freefunk.pause --> Pause the current Tariff
freefunk.book1gb --> Book the 1GB Tariff
freefunk.bookunlimited --> Book the Unlimited Tariff

The component will log the output on an INFO level.

The component is meant to enable you to: "Pause & Forget" via automations. Meaning whenever the auto reactivation (every 14days) happens, the pause can be triggered automatically if previously set by the user.



## Installation
Copy all files from custom_components/freefunk/ to custom_components/freefunk/ inside your config Home Assistant directory.

### Configuration
Add the following to your config
```
freefunk:
  username: !secret freefunk_username
  password: !secret freefunk_password
```
