class Message_except(Exception):
    def missed_argument(self, missed_number, message, missed_title):
        error="ERROR: missing {} required positional argument --> ('{}', <!MISSED HERE!>={})".format(
            missed_number,
            message,
            missed_title
        )
        
        return error

class Core_except(Exception):
    def wrong_act_type(self, act):
        error=f"'{act}' is not a dict!\n'{act}' must be in dict! XO"
        return error
    