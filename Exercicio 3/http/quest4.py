def main():
    user_url = input('Digite a url (ex: https://github.com):\n');
    if(user_url.startswith('https://')): print('Site seguro.');
    else: print('Site inseguro.');
main()