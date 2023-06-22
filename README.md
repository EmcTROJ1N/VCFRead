<br />
<div align="center">
  <img src="icon.png" alt="Logo" width="80" height="80">

  <h3 align="center">VCF Reader</h3>

  <p align="center">
    <a href="https://github.com/EmcTROJ1N/VCFRead/">View Demo</a>
    ·
    <a href="https://github.com/EmcTROJ1N/VCFRead/issues">Report Bug</a>
    ·
    <a href="https://github.com/EmcTROJ1N/VCFRead/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a phone book parser written in Python which can extract contacts from VCard-formatted files. The program provides a simple and efficient way to read and organize contact information such as names, phone 
numbers, email addresses, postal addresses, and more.

With this tool, you can quickly parse large phone book files and create a structured data representation of the contacts contained therein. The parsed data can then be easily exported to other formats or used 
directly by your application.

The phone book parser supports various versions of the VCard format, including V2.1, V3.0, and V4.0. It also handles multiple contacts within a single file and can handle different character encodings, 
such as UTF-8 and other.

Overall, this phone book parser is a useful tool for anyone who needs to work with VCard files and wants to extract contact information in a structured and organized manner.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

![Python](https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=python)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Before running this program, please ensure that you have Python 3 installed on your system.

### Debian-like distributions (Debian, Ubuntu, etc.)
```
sudo apt-get update
sudo apt-get install python3
```
### Arch-like distributions (Arch Linux, Manjaro, etc.)
```
sudo pacman -Sy python-pip
```
### Windows
To install Python 3 on Windows, download the installer from the official Python website: https://www.python.org/downloads/windows/
Run the installer and follow the prompts to complete the installation.
Remember to check the option to add Python to the environment variables, otherwise you won't be able to run scripts from the console

### Installation

Clone the repo
   ```sh
   git clone https://github.com/EmcTROJ1N/VCFRead
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Code examples:
/* The repository contains a test file .vcf which will be used to demonstrate the parser's capabilities */

First, you need to connect the imports, as well as create a collection from the file
```
from VCFCollection import *
from VCFContact import *
from formatters import *

if __name__ == "__main__":
    contacts = VCFCollection("contacts.vcf")
```

### Show all fullnames:
```
for name in contacts.GetArrProps("Name"):
  print(name["FirstName"], name["AdditionalName"], name["LastName"], sep=" ")
```
Output:
```
Forrest  Gump
Derik  Stenerson
Anik  Ganguly
Robert  Moskowitz
John  Doe
```

### Display phones
```
for phones in contacts.GetArrProps("PhoneNumbers"):
  print(phones)
```
Output:
```
['(111) 555-1212', '(404) 555-1212']
['+1-425-936-5522', '+1-425-936-7329']
['+1-734-542-5955']
[]
['+1 617 555 1212', '+1 (617) 555-1234', '+1 781 555 1212', '+1 202 555 1212']
```

### Format phone numbers

/* Due to the peculiarities of numbers in each region, to improve the accuracy of the function it is recommended to write 
your own function to standardize the number. An example of such function is given in the file formatters.py, it will be used below */

```
contacts.FormatPhones(formatUkRuNum)
```

Output:
```
['1115551212', '4045551212']
['14259365522', '14259367329']
['17345425955']
[]
['16175551212', '16175551234', '17815551212', '12025551212']
```

### Find match contacts
```
for contact in contacts.FindMatchContacts(contacts):
      print(contact, end="\n\n")
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<ol>
  <li>Fork the Project</li>
  <li>Commit your Changes (`git commit -m 'Add some AmazingFeature'`)</li>
  <li>Push to the Branch (`git push origin feature/AmazingFeature`)</li>
  <li>Open a Pull Request</li>
</ol>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - [@emctroj1n](https://t.me/EmcTROJ1N) - 19et72@mail.ru

[Project Link](https://github.com/EmcTROJ1N/VCFRead)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
