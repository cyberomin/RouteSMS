## we can use code to define various error codes that can be thrown by route sms
class RouteSMSException(Exception):
  def __init__(self, message, code):
    super(Exception, self).__init__(message)
    self.code = code
