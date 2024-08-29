from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class BasePage(UIHelper, metaclass=MetaLocator):
    ...
