DOMAIN = 'freefunk'
import logging

_LOGGER = logging.getLogger(__name__)

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
    _LOGGER.info(currentPlan)
 
    def pause(call):
        """Handle the pause service call."""
        conf = config[DOMAIN]
        username = conf[CONF_USERNAME]
        password = conf[CONF_PASSWORD]
        import funkapi
        from funkapi import FunkAPI
        api = FunkAPI(username, password)
        status = api.startPause()
        _LOGGER.info(status)
        import time
        time.sleep(10) 
        currentPlan = api.getCurrentPlan()
        hass.states.set('freefunk.status', currentPlan["productServiceInfo"]["label"])
        _LOGGER.info(currentPlan)

    hass.services.register(DOMAIN, 'pause', pause)

    def update(call):
        """Handle the update service call."""
        conf = config[DOMAIN]
        username = conf[CONF_USERNAME]
        password = conf[CONF_PASSWORD]
        import funkapi
        from funkapi import FunkAPI
        api = FunkAPI(username, password)
        currentPlan = api.getCurrentPlan()
        hass.states.set('freefunk.status', currentPlan["productServiceInfo"]["label"])
        _LOGGER.info(currentPlan)


    hass.services.register(DOMAIN, 'update', update)
    
    def book1gb(call):
        """Handle the update service call."""
        conf = config[DOMAIN]
        username = conf[CONF_USERNAME]
        password = conf[CONF_PASSWORD]
        import funkapi
        from funkapi import FunkAPI
        api = FunkAPI(username, password)
        status = api.order1GBPlan()
        _LOGGER.info(status)		
        import time
        time.sleep(10) 
        currentPlan = api.getCurrentPlan()
        hass.states.set('freefunk.status', currentPlan["productServiceInfo"]["label"])
        _LOGGER.info(currentPlan)


    hass.services.register(DOMAIN, 'book1gb', book1gb)
	
    def bookunlimited(call):
        """Handle the update service call."""
        conf = config[DOMAIN]
        username = conf[CONF_USERNAME]
        password = conf[CONF_PASSWORD]
        import funkapi
        from funkapi import FunkAPI
        api = FunkAPI(username, password)
        status = api.orderUnlimitedPlan()
        _LOGGER.info(status)		
        import time
        time.sleep(10) 
        currentPlan = api.getCurrentPlan()
        hass.states.set('freefunk.status', currentPlan["productServiceInfo"]["label"])
        _LOGGER.info(currentPlan)


    hass.services.register(DOMAIN, 'bookunlimited', bookunlimited)
	
	
    return True