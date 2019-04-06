Utility Functions
--------------------------
I have listed the following as utility functions:
1) url_validation
2) https_url_validation
3) create_basic_recipient
4) typing_on
5) marked_seen
6) whitelist_domain

I have marked them as Utility functions because either they are just to mimic humans or boost internal functionality.
Let me explain the functions you might actually need first.

###### Typing on
Typing on shows the typing on icons on recipients end.

    typing_on(self, user_id: str, waiting_period: float = 1.5)
        private function, turns on typing function, sleep 3s before doing anything else.
        :param waiting_period: how long the icon will keep floating
        :param user_id: facebook users ID
        :return: returns the payload for typing_on function
        
By default, typing_on icon will stay popped for 20 seconds max. Or if bot sends message before that, the icon will automatically 
stop waving.

__PS:__ you will actually need to send the returned payload to Facebook's end to make it work.


###### Marked Seen
Same as Typing on, Mark seen marked the users (bot's end user) message as seen.  