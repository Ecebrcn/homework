from selenium.webdriver.common.by import By


#UTM settings on Newsletter design page
UTMSETTINGS_CHECKBOX = (By.CLASS_NAME, 'checkboxDefault checkboxDefault')

#input warning message,for example, on Journey SMS page when we try to save empty title input
WARNING_TEXT = (By.LINK_TEXT, 'The Your Message field is required.')

#on Journey do list filter input
JOURNEY_LIST_FILTER = (By.ID, 'search-value')

#tags list when we select template in created journey campaign and didn't click Use this Template button
JOURNEY_TAG_LIST = (By.CLASS_NAME, 'tag animationHalf')

#on Journey do list how to click exactly needed Statistics button if there is more than 1 campaigns in the list
STATISTICS_BTN = (By.XPATH, '//div[contains(@class, "tooltip-align-right")][8]')

#on Message box design page remove variation cross icon
DELETE_VARIATION = (By.XPATH, '//*[@id="delete"]')

#Remove / Change element buttons on Journey canvas page
CHANGE_ELEMENT = (By.XPATH, '//p[contains(@class, "text")][1]')

# Remove / Change element buttons on Journey canvas page
REMOVE_ELEMENT = (By.XPATH, '//p[contains(@class, "text")][2]')

#Alert toaster on any page of panel
ALERT_TOASTER = (By.CLASS_NAME, 'messageAlertBoxIcon')

#on Api and js (access area) free js body input
ALERT_ACCESS = (By.LINK_TEXT, 'You are not authorized to access this page!')
