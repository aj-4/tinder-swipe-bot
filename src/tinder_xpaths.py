# Phone Login
PHONE_BUTTON_LOGIN = (
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/button'
)
PHONE_INPUT_NUMBER = '//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input'
PHONE_BUTTON_CONTINUE = '//*[@id="modal-manager"]/div/div/div[2]/button'
PHONE_INPUT_CODE_TEMPLATE = (
    '//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{field_idx}]'
)
POPUP_BUTTON_PERMISSIONS = (
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
)

# Actions
ACTION_BUTTON_LIKE = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
ACTION_BUTTON_SUPER_LIKE = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div/button'
ACTION_BUTTON_DISLIKE = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'

# Profile Info
PROFILE_INFO_FLAIR = (
    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/div/div[2]/div[2]',
)
PROFILE_INFO_NAME = {
    # has_flair
    True: '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/div/div[1]/div/div/span',
    False: '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span',
}
PROFILE_INFO_AGE = {
    # has_flair
    True: '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/div/div[1]/div/span',
    False: '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/span',
}

# Bio
BIO_BUTTON_OPEN = {
    # has_flair
    True: '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/button',
    False: '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button',
}
BIO_FIELD = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div'
BIO_BUTTON_CLOSE = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a[1]'

# Match Popups
POPUP_BUTTON_OFFER = '//*[@id="modal-manager"]/div/div/div[2]/button[2]'
POPUP_BUTTON_MATCH = (
    '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a'
)
