#pip install pywin32 pyperclip
import win32api,time,win32con,win32clipboard

last="""hello world, this is a test content"""

def click_key(value):
    print(value)
    win32api.keybd_event(value, 0, 0, 0)
    win32api.keybd_event(value, 0, win32con.KEYEVENTF_KEYUP, 0)

def input_str(s):
    s=s.upper()
    A=ord('A')
    Z=ord('Z')
    k0=ord('0')
    k9=ord('9')
    space=ord(' ')
    nl=ord('\n')
    for i in s:
        i=ord(i)
        if (i<=Z and i>=A):
            click_key(i)
        elif i>=k0 and i<=k9:
            click_key(i+48)
        elif i==nl:
            click_key(13)
        else:
            click_key(space)
def clear_clipboard():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText('')
    win32clipboard.CloseClipboard()

def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def get_key():
    q=win32api.GetAsyncKeyState(ord('Q')) 
    F2=win32api.GetAsyncKeyState(113) 
    esc=win32api.GetAsyncKeyState(27) 
    global last
    if esc!=0:
        data=get_clipboard()
        if data!=last:
            input_str(data)
            last=data
    else:
        last=""
    if F2!=0:
        clear_clipboard()

while(True):
    time.sleep(0.3)
    get_key()