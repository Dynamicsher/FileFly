# FileFly
• A lightweight, self-hosted HTTP file server developed using Python and Flask to enable high-speed file transfers across a Local Area Network (LAN).  
• Built a responsive web dashboard allowing multiple concurrent client devices (mobiles/PCs) to upload bulk binary streams via multipart/form-data payloads.   
• Implemented server-side security controls utilizing path-traversal sanitization (secure_filename) to protect the host machine's directory architecture.

# Installation
To make this application work, you first need to install Python and Flask
on your computer system:
1. Install python from https://python.org if not already installed
2. Open a terminal in python and run `pip install flask` to install Flask

# Usage
After the required apps/dependencies have been installed, follow these
instructions to deploy your web server:
1. Clone this repo in your project folder using git clone
2. Navigate to the FileFly directory and open a terminal or command prompt inside it
3. Run `python app.py` on Windows or `python3 app.py` on Mac/Linux to start the server
4. Clients can now connect to the server by opening http://`<device_ip>`:`<port_number>` inside a browser, replacing `<device_ip>` with
the IP address of your PC and replacing `<port_number>` with the port number mentioned in the terminal. (e.g. http://192.168.56.20:5000)

You are now ready to make your files fly over your network! Enjoy :D
