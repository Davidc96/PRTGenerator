# PRT Token Generator

This tool is used to create PRT tokens using browsercore.exe
via web application to perform PASS-THE-PRT attacks

## Usage

1. Create python3 environment in current folder 
```python3 -m venv .\venv```
2. Activate environment with 
```.\venv\Scripts\activate.bat```
3. Install flask using command
```pip install Flask```
4. Set FLASK_APP environment with ```set FLASK_APP=main.py```
5. Run the tool ```flask run --host 0.0.0.0```
6. Go to URL ```http://127.0.0.1:5000```
7. Follow the tool's steps

## First steps

To properly generate the token, you need to provide a
dummy URL, you need to do this once. To create a Dummy token follow the steps:

1. On the computer you want to generate the token go to
```https://outlook.office365.com``` on a Chrome incognito window

2. While in Microsoft sign in page, copy the URL and paste it
in variable DUMMY_URI in main.py file

3. Save and run the tool

## Troubleshoots
- On microsoft Teams, sometimes it will show an error saying:
Ops something goes wrong
To solve this, click on Sign out and try to sign in again.
Don't worry when you sign out because when you login again it will use the PRT you already generated.

- On Microsoft Teams, sometimes it will loop the requests, to solve this just type on the URL browser 
``https://teams.microsoft.com`` and it will solve the problem.
## Credits

- <a href="https://github.com/dirkjanm">@Dirkjanm</a> for the pass-the-prt script
- My <a href="https://davidc96.github.io/2021/07/30/Ataques-Laterales-Cloud-Pass-PRT.html"> blog post </a> about the PASS-THE-PRT attack (Spanish only)