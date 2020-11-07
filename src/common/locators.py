from selenium.webdriver.common.by import By


class Locators:

    # Contacts page locators
    CONTACT_FORM = (By.CSS_SELECTOR, "section.has_ae_slider.ob-is-breaking-bad[data-settings*='{\"backgr']")
    FIRSTNAME_TEXT_BOX = (By.CSS_SELECTOR, "input.hs-input[name=\"firstname\"]")
    LASTNAME_TEXT_BOX = (By.CSS_SELECTOR, "input.hs-input[name=\"lastname\"]")
    SEND_REQUEST_BUTTON = (By.CSS_SELECTOR, "input.hs-button.primary.large")
    AGREEMENT_BOX = (By.CSS_SELECTOR, "input.hs-input[name='lopd']")
    SUBMITED_MSG = (By.CSS_SELECTOR, "div.submitted-message.hs-main-font-element")
    EMAIL_TEXT_BOX = (By.CSS_SELECTOR, "input.hs-input[name='email']")
    COMPANY_TEXT_BOX = (By.CSS_SELECTOR, "input.hs-input[name='company']")
    PHONE_TEXT_BOX = (By.CSS_SELECTOR, "input.hs-input[name='phone']")
    MESSAGE_TEXT_BOX = (By.CSS_SELECTOR, "textarea.hs-input[name='message']")
    CONTACT_TEXT_BOX = (By.CSS_SELECTOR, "input.hs-input[name='NAME']")
