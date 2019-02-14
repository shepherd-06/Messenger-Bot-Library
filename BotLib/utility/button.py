from ZathuraProject.zathura import Zathura
from ZathuraProject.utility import Utility as zathura_utility
from BotLib.utility.util import Utility
from BotLib.utility.tag import Tags


class Button:

    def __init__(self):
        self.zathura = Zathura()
        self.z_util = zathura_utility()
        self.utility = Utility()

    def create_url_button(self, title: str, url: str, webview_height_ratio: str = "full", messenger_extensions: bool = False, fallback_url: str = '', webview_share_button: str = 'hide'):
        """
        Reference: https://developers.facebook.com/docs/messenger-platform/reference/buttons/url
        Supported usage:
            Persistent menu
            Generic template
            List template
            Button template
            Media template 
            Open graph template
        :title :str Button title. 20 character limit.
        :url :str This URL is opened in a mobile browser when the button is tapped. Must use HTTPS protocol if messenger_extensions is true.
        :webview_height_ratio :str Optional. Height of the Webview. Valid values: compact, tall, full. Defaults to full.
        :messenger_extensions :bool Optional. Must be true if using Messenger Extensions.
        :fallback_url :str The URL to use on clients that don't support Messenger Extensions. If this is not defined, the url will be used as the fallback. It may only be specified if messenger_extensions is true.
        :webview_share_button: str Optional. Set to hide to disable the share button in the Webview (for sensitive info). This does not affect any shares initiated by the developer using Extensions. 
        :returns a dictionary in the format for web_url button template
        """
        user = "create_url_button"
        if title is None or len(title) <= 0:
            self.zathura.insert_error_log(user, "title", "title is None or len is zero. Title: {}".format(
                title), self.z_util.Tag_Log_ERROR)
            return

        if len(title) > 20:
            # Error / Warning
            self.zathura.insert_error_log(user, "title", "title len is more than 20. Title: {}".format(
                title), self.z_util.Tag_Log_WARNING)
            pass

        if url is None or len(url) <= 0:
            # Error
            self.zathura.insert_error_log(
                user, "url", "url is None or len is zero. Url: {}".format(url), self.z_util.Tag_Log_ERROR)
            return
        if not self.utility.url_validation(url):
            # Error
            self.zathura.insert_error_log(
                user, "url", "url did not validate itself as web_url. Url: {}".format(url), self.z_util.Tag_Log_ERROR)
            return

        if webview_height_ratio not in (Tags.TAG_WEBVIEW_HEIGHT_RATIO_COMAPCT, Tags.TAG_WEBVIEW_HEIGHT_RATIO_FULL, Tags.TAG_WEBVIEW_HEIGHT_RATIO_TALL):
            # error
            self.zathura.insert_error_log(
                user, "webview_height_ratio", "webview_height_ratio did not match the 3 choices. webview_height_ratio: {}".format(webview_height_ratio), self.z_util.Tag_Log_ERROR)
            return

        if messenger_extensions:
            if not self.utility.https_url_validation(url):
                # ERROR
                self.zathura.insert_error_log(
                    user, "url", "url has to be HTTPS if messenger_extensions is True. Url: {}".format(url), self.z_util.Tag_Log_ERROR)

                return
            if fallback_url is None or len(fallback_url) == 0:
                # Error
                self.zathura.insert_error_log(
                    user, "fallback_url", "Fallback url has to be present if messenger_extension is True. fallback_url: {}".format(fallback_url), self.z_util.Tag_Log_ERROR)

                return
            if not self.utility.https_url_validation(fallback_url):
                # Error
                self.zathura.insert_error_log(
                    user
        , "fallback_url", "Fallback url has to be HTTPS if messenger_extensions is True. fallback_url: {}".format(fallback_url), self.z_util.Tag_Log_ERROR)

                return

        if webview_share_button in (Tags.TAG_SHARE_HIDE, Tags.TAG_SHARE_SHOW):
            # Error
            self.zathura.insert_error_log(
                user, "webview_share_button", "webview_share_button value did not match the values required. Its either hide | show. webview_share_button: {}".format(webview_share_button), self.z_util.Tag_Log_ERROR)
            return

        return {
            Tags.TAG_TYPE: Tags.TAG_WEB_URL,
            Tags.TAG_URL: url,
            Tags.TAG_TITLE: title,
            Tags.TAG_WEBVIEW_HEIGHT_RATIO: webview_height_ratio,
            Tags.TAG_MESSENGER_EXTENSION: messenger_extensions,
            Tags.TAG_FALLBACK_URL: fallback_url,
            Tags.TAG_WEBVIEW_SHARE_BUTTON: webview_share_button,
        }

