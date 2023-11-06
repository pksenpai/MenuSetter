class Message_except():
    
    def missed_argument(missed_number, message, missed_title):
        error="ERROR: missing {} required positional argument --> ('{}', <!MISSED HERE!>={})".format(
            missed_number,
            message,
            missed_title
        )
        
        return error

class Core_except:
    
    def wrong_act_type(act):
        error=f"'{act}' is not a dict!\n'{act}' must be in dict! XO"
        return error