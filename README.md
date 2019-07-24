# freefunk
This is a custom component for Home Assistant enabling the use of the Freenet-Funk-API 

Currently this will update the current state of your Freenet Funk Contract in the entity: freefunk.status
There are 4 Service Calls available:
```
freefunk.update --> Update the current status
freefunk.pause --> Pause the current Tariff
freefunk.book1gb --> Book the 1GB Tariff
freefunk.bookunlimited --> Book the Unlimited Tariff
```
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

## EXAMPLE CONFIG FOR HOME ASSISTANT

![Example Node Red](https://community-home-assistant-assets.s3.dualstack.us-west-2.amazonaws.com/original/3X/7/e/7ebc38b14b2f9b56f7a24cd3fb03783bf85a8ab3.png)

![Example HA Lovelace](https://community-home-assistant-assets.s3.dualstack.us-west-2.amazonaws.com/original/3X/2/a/2a2572047229b7d2a64566b6f1bc17e2f4204520.png)




```
1x input_boolean --> represents Pause.
1x input_select --> to choose what Tariff i wish to book
```


```
input_boolean:
  paused:
    name: Freenet Funk Pause  
    
input_select:
############## Tariffs ###############
  tariff:
    name: 'Tariff:'
    options:
      - Select
      - 1 GB
      - Unlimited
    initial: Select
    icon: mdi:sim
```


Nodered Code:

```
[
    {
        "id": "b12cec59.fadeb",
        "type": "inject",
        "z": "5f5aa1ed.42ac5",
        "name": "",
        "topic": "",
        "payload": "true",
        "payloadType": "bool",
        "repeat": "28800",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 110,
        "y": 80,
        "wires": [
            [
                "20b7f754.7d96c8"
            ]
        ]
    },
    {
        "id": "20b7f754.7d96c8",
        "type": "api-call-service",
        "z": "5f5aa1ed.42ac5",
        "name": "Update",
        "server": "2fba4297.e4145e",
        "service_domain": "freefunk",
        "service": "update",
        "data": "",
        "mergecontext": "",
        "output_location": "",
        "output_location_type": "none",
        "mustacheAltTags": false,
        "x": 500,
        "y": 80,
        "wires": [
            []
        ]
    },
    {
        "id": "a4e6db37.136d48",
        "type": "server-state-changed",
        "z": "5f5aa1ed.42ac5",
        "name": "Status?",
        "server": "2fba4297.e4145e",
        "version": 1,
        "entityidfilter": "freefunk.status",
        "entityidfiltertype": "exact",
        "outputinitially": false,
        "state_type": "str",
        "haltifstate": "Pause",
        "halt_if_type": "str",
        "halt_if_compare": "is",
        "outputs": 2,
        "output_only_on_state_change": false,
        "x": 90,
        "y": 180,
        "wires": [
            [],
            [
                "37306f68.243e4"
            ]
        ]
    },
    {
        "id": "9cb72a4c.aa3178",
        "type": "comment",
        "z": "5f5aa1ed.42ac5",
        "name": "Update every 8h",
        "info": "",
        "x": 80,
        "y": 40,
        "wires": []
    },
    {
        "id": "e1bbe024.1a88",
        "type": "api-call-service",
        "z": "5f5aa1ed.42ac5",
        "name": "Pause",
        "server": "2fba4297.e4145e",
        "service_domain": "freefunk",
        "service": "pause",
        "data": "",
        "mergecontext": "",
        "output_location": "",
        "output_location_type": "none",
        "mustacheAltTags": false,
        "x": 490,
        "y": 180,
        "wires": [
            [
                "f920b3.48a50f5"
            ]
        ]
    },
    {
        "id": "37306f68.243e4",
        "type": "api-current-state",
        "z": "5f5aa1ed.42ac5",
        "name": "Paused On?",
        "server": "2fba4297.e4145e",
        "version": 1,
        "outputs": 2,
        "halt_if": "on",
        "halt_if_type": "str",
        "halt_if_compare": "is",
        "override_topic": false,
        "entity_id": "input_boolean.paused",
        "state_type": "str",
        "state_location": "payload",
        "override_payload": "msg",
        "entity_location": "data",
        "override_data": "msg",
        "blockInputOverrides": false,
        "x": 250,
        "y": 180,
        "wires": [
            [
                "e1bbe024.1a88"
            ],
            []
        ]
    },
    {
        "id": "42b4b041.d94c1",
        "type": "comment",
        "z": "5f5aa1ed.42ac5",
        "name": "Pause when automatic activated, or triggered manually",
        "info": "",
        "x": 200,
        "y": 140,
        "wires": []
    },
    {
        "id": "122877d3.440378",
        "type": "server-state-changed",
        "z": "5f5aa1ed.42ac5",
        "name": "Status?",
        "server": "2fba4297.e4145e",
        "version": 1,
        "entityidfilter": "input_select.tariff",
        "entityidfiltertype": "exact",
        "outputinitially": false,
        "state_type": "str",
        "haltifstate": "",
        "halt_if_type": "str",
        "halt_if_compare": "is",
        "outputs": 1,
        "output_only_on_state_change": true,
        "x": 90,
        "y": 340,
        "wires": [
            [
                "83344da8.3af07"
            ]
        ]
    },
    {
        "id": "b0312e4d.eeb12",
        "type": "comment",
        "z": "5f5aa1ed.42ac5",
        "name": "Book Tariffs and turn off Pause",
        "info": "",
        "x": 130,
        "y": 300,
        "wires": []
    },
    {
        "id": "83344da8.3af07",
        "type": "switch",
        "z": "5f5aa1ed.42ac5",
        "name": "",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1 GB",
                "vt": "str"
            },
            {
                "t": "eq",
                "v": "Unlimited",
                "vt": "str"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 290,
        "y": 340,
        "wires": [
            [
                "c863ecfd.0f821"
            ],
            [
                "7a2cba4c.1566e4"
            ]
        ]
    },
    {
        "id": "a446c8e9.b8e338",
        "type": "api-call-service",
        "z": "5f5aa1ed.42ac5",
        "name": "Turn Off Paused",
        "server": "2fba4297.e4145e",
        "service_domain": "input_boolean",
        "service": "turn_off",
        "data": "{\"entity_id\":\"input_boolean.paused\"}",
        "mergecontext": "",
        "output_location": "",
        "output_location_type": "none",
        "mustacheAltTags": false,
        "x": 700,
        "y": 340,
        "wires": [
            []
        ]
    },
    {
        "id": "c863ecfd.0f821",
        "type": "api-call-service",
        "z": "5f5aa1ed.42ac5",
        "name": "1 GB",
        "server": "2fba4297.e4145e",
        "service_domain": "freefunk",
        "service": "book1gb",
        "data": "",
        "mergecontext": "",
        "output_location": "",
        "output_location_type": "none",
        "mustacheAltTags": false,
        "x": 490,
        "y": 340,
        "wires": [
            [
                "a446c8e9.b8e338"
            ]
        ]
    },
    {
        "id": "7a2cba4c.1566e4",
        "type": "api-call-service",
        "z": "5f5aa1ed.42ac5",
        "name": "Unlimited",
        "server": "2fba4297.e4145e",
        "service_domain": "freefunk",
        "service": "bookunlimited",
        "data": "",
        "mergecontext": "",
        "output_location": "",
        "output_location_type": "none",
        "mustacheAltTags": false,
        "x": 500,
        "y": 420,
        "wires": [
            [
                "a446c8e9.b8e338"
            ]
        ]
    },
    {
        "id": "74e15236.79407c",
        "type": "server-state-changed",
        "z": "5f5aa1ed.42ac5",
        "name": "Paused?",
        "server": "2fba4297.e4145e",
        "version": 1,
        "entityidfilter": "input_boolean.paused",
        "entityidfiltertype": "exact",
        "outputinitially": false,
        "state_type": "str",
        "haltifstate": "",
        "halt_if_type": "str",
        "halt_if_compare": "is",
        "outputs": 1,
        "output_only_on_state_change": true,
        "x": 100,
        "y": 240,
        "wires": [
            [
                "e1bbe024.1a88"
            ]
        ]
    },
    {
        "id": "f920b3.48a50f5",
        "type": "api-call-service",
        "z": "5f5aa1ed.42ac5",
        "name": "Select No Tariff",
        "server": "2fba4297.e4145e",
        "service_domain": "input_select",
        "service": "select_option",
        "data": "{\"entity_id\":\"input_select.tariff\",\"option\":\"Select\"}",
        "mergecontext": "",
        "output_location": "",
        "output_location_type": "none",
        "mustacheAltTags": false,
        "x": 700,
        "y": 180,
        "wires": [
            []
        ]
    },
    {
        "id": "2fba4297.e4145e",
        "type": "server",
        "z": "",
        "name": "Home Assistant",
        "legacy": false,
        "hassio": true,
        "rejectUnauthorizedCerts": true,
        "ha_boolean": "y|yes|true|on|home|open",
        "connectionDelay": true
    }
]
```
