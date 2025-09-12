                                       *** Custom Python Scripts ***

# Custom Scripts in Python

**Custom scripts** are Python programs written to solve specific problems or automate tasks.  
They bring together functions, methods, and classes into standalone files that can be run directly.

### Structure
A custom script typically includes:
- **Imports**: any external modules or libraries required.  
- **Functions/Classes**: reusable logic to keep the code organized.  
- **Main execution block**: the part of the code that runs when the script is executed.  

### Example
```python
import datetime

def greet_user(name):
    """Return a time-based greeting."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        return f"Good morning, {name}!"
    elif hour < 18:
        return f"Good afternoon, {name}!"
    else:
        return f"Good evening, {name}!"

if __name__ == "__main__":
    print(greet_user("Alice"))
```

### Instructions & Examples for the custom scripts located in this directory.

- PortScaner.py, Scans a single Host/Network (TCP or UDP) for open ports.
> python3 PortScanner.py <IP address> <start port> <end port> [-u|-n]
> python3 PortScanner.py 192.168.1.10 1 65535
> python3 PortScanner.py 192.168.1 1 65535 -n
> python3 PortScanner.py 192.168.1 1 100 -n (Network Only Ports 1-100)
> python3 PortScanner.py 192.168.1 1 65535 -n
> python3 PortScanner.py 192.168.1.10 1 65535 -u

- FileServer.py, Runs a simple http server for downloading files from the current directory, on set port 8000 or chosen port.
> python3 FileServer.py 
> python3 Fileserver.py 4000

- QueryIPaddress.py, Run the Script then Enter the IP address to query, Results will be returned.
> QueryIPaddress.py

- BarcodeGenerator.py, This Script Creates Barcodes 12 digits long, Also Creates a .svg file of the barcode.
> BarcodeGenerator.py

- PublicOrPrivateIPchecker.py, This Script Checks if a give IP address is public or private.
> PublicOrPrivateIPchecker.py 192.168.0.1

- XssAttacker.py, This script will generate a malicious .js file. When this is used in an XSS attack, 
 it will cause the victim to navigate to the target directory and send the content to the attacker. 
> XssAttacker.py -d <directory> -i <IP>

- CeaserCipherEncryptor.py, This Script will ceaser cipher encode alpha numeric input,
with the options to choose key and shift left or right for the encryption.
> CeaserCipherEncryptor.py (Follow the Commands on the Teminal)

- EmailFileSearcher.py, This Script Will Search Through A Given File For Email Addresses,
Enter A File In The Input, Include File Path If The File Is Not
In The Current Directory. It Will Print Any Found Addresses.
> EmailFileSearcher.py file.txt
> EmailFileSearcher.py ~/Downloads/file.txt

- IpDefang.py, This Script Will Defang IP addresses.
> IpDefang.py

