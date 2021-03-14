import webbrowser

#below defines all my variables which are going to be the URLs i want to naviagate to
url1 = 'mail.uc.edu'
url2 = 'https://login.uc.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1'
url3 = 'portal.office.com'


chrome_path = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'  #here i am defining a variable that points to my firefox.exe file location
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))#below function "register" registers the browser type name according to https://docs.python.org/3/libary/webbrowser.html
webbrowser.get('chrome').open_new_tab(url1) #Found this command at https://docs.python.org/3/libary/webbrowser.html
webbrowser.get('chrome').open_new_tab(url2) #Found this command at https://docs.python.org/3/libary/webbrowser.html
webbrowser.get('chrome').open_new_tab(url3) #Found this command at https://docs.python.org/3/libary/webbrowser.html

#below im commenting my file path so i dont forget it.
#C:\it30380c-scripts\Labs\webBrowserCode.py