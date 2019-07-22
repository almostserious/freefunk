DOMAIN = 'freefunk'
from homeassistant.const import (
    CONF_PASSWORD, CONF_USERNAME)
def setup(hass, config):
    conf = config[DOMAIN]
    username = conf[CONF_USERNAME]
    password = conf[CONF_PASSWORD]
    import funkapi
    from funkapi import FunkAPI
    api = FunkAPI(username, password)
    currentPlan = api.getCurrentPlan()
    hass.states.set('freefunk.status', currentPlan["productServiceInfo"]["label"])
	 
    # paused = hass.states.get("input_boolean.paused").state == "on"
    # if paused:
        # status = api.startPause()
        # hass.states.set('freefunk.error', status["errors"][0]["message"])
    # hass.states.set('freefunk.state', paused)
    return True