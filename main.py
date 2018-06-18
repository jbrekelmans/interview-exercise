def print_directory_contents(dir):
  '''
  This function prints all files in the directory dir (including files in subdirectories of dir).

  TODO: implement this function without using os.walk
  '''

def check_password_strength(password):
  '''
  This function returns the strength of the supplied password by using the following API.

  TODO: use the requests Python module to rate the strength of password by performing the following HTTP request:
  POST https://www.google.com/accounts/RatePassword?Passwd=<password>
  No special headers have to be sent and the response body is a simple integer ([0-9]+).
  '''

if __name__ == '__main__':
    print_directory_contents('.')
    print(check_password_strength('asdf'))
    print(check_password_strength('Admin123'))