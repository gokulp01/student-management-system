import requests
from PIL import Image
import io
from datauri import DataURI
import base64
import pyperclip
url = "https://slcm.manipal.edu/imagereader.aspx"

querystring = {"FileName":"","ImagePath":"E:/PortalDocuments/100000024272.jpg"}

response = requests.request("GET", url, params=querystring)

print(type(response.content))
image = Image.open(io.BytesIO(response.content))
encoded = base64.b64encode(response.content).decode('UTF-8')
finaluri = "data:image/png;base64," + encoded
pyperclip.copy(finaluri)
