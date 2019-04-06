Echo Back
-----------------------------
Echo back reply is simply replying with text messages or attachments. Since developers can replace text with other template 
types of Facebook's. 

```__Attachment__ sending is not available right now. Right now, it only supports text message.```

Code example:

    from bizarro.utility.util import Utility
    echo_text = bizarro_utility().basic_text_reply_payload(fb_user_id, message="Hello") 
    

##### Function parameters:

basic_text_reply_payload(self, user_id: str, message: str)
    
    This function generates the payload for basic text reply
      :param user_id: user_id of a particular user_id
      :param message: message user going to see. 
             length of message has to be less than 2000 characters (Also not None)
      :return: payload
    
##### Error messages:

If error occurs, function will return None instead of the original payload
on success, payload structure is

    {
        Tags.TAG_RECIPIENT: {
            Tags.TAG_ID: user_id
        },
        Tags.TAG_MESSAGE: {
            Tags.TAG_TEXT: message
        }
    }

##### What next?
Send this payload as a POST request to Facebook Graph Api url with appropriate Page Access Token.
