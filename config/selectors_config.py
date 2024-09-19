LOGIN_PAGE = {
    "username_input": "input[name='username']",
    "password_input": "input[name='password']",
    "submit_button": "button[type='submit']",
}

DASHBOARD_PAGE = {
    "my_info_button": "span:has-text('My Info')",
}

PERSONAL_PAGE = {
    "first_name_input": "input[name='firstName']",
    "last_name_input": "input[name='lastName']",
    "middle_name_input": "input[name='middleName']",
    "employee_id_input": "(//input[contains(@class, 'oxd-input oxd-input--active')])[1]",
    "other_id_input": "(//input[contains(@class, 'oxd-input oxd-input--active')])[2]",
    "drivers_license_number_input": "(//input[contains(@class, 'oxd-input oxd-input--active')])[3]",
    "license_expiry_date_icon": "//i[contains(@class, 'bi-calendar') and contains(@class, 'oxd-date-input-icon')]",
    "nationality_icon": "(//div[contains(@class, 'oxd-select-text--arrow')])[1]",
    "marital_status_icon": "(//div[contains(@class, 'oxd-select-text--arrow')])[2]",
    "date_of_birth_icon": "//i[contains(@class, 'bi-calendar') and contains(@class, 'oxd-date-input-icon')]",
    "gender_radio": "//input[contains(@class, 'oxd-radio-input oxd-radio-input--active')]",
    "save_button": "(//button[@type='submit'])[1]",
    "loading_spinner": ".oxd-loading-spinner",
}
