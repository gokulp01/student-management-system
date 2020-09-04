import requests 

test_image = "https://www-nass.nhtsa.dot.gov/nass/cds/CaseForm.aspx?ViewText&CaseID=149006673&xsl=textonly.xsl&websrc=true"
pull_image = requests.get(test_image)

with open("test_image.jpg", "wb+") as myfile:
    myfile.write(pull_image.content)
pull_image = requests.get(test_image, stream=True)
with open("test_image.jpg", "wb+") as myfile:
    myfile.write(pull_image.raw.read())