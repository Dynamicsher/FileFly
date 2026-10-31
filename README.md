# FileFly
• A lightweight, self-hosted HTTP file server developed using Python and Flask to enable high-speed file transfers across a Local Area Network (LAN).
• Built a responsive web dashboard allowing multiple concurrent client devices (mobiles/PCs) to upload bulk binary streams via multipart/form-data payloads.
• Implemented server-side security controls utilizing path-traversal sanitization (secure_filename) to protect the host machine's directory architecture.

# Dependencies/Packages
To make this application work, you need to install Python and Flask
on your computer system:
1. Install python from python.org if not already installed
2. Open a terminal in python and run: pip install flask to successfully install Flask

# Usage
After the above apps/modules are installed, follow these
instruction to deploy your web application:
1. Clone this repo in your project folder using git clone
2. Navigate to the FileFly directory and open a terminal or command prompt inside it
3. Run python app.py on Windows and python3 app.py on Mac/Linux
4. The server will start and clients can now connect to your server using the port number stated in the terminal
5. Open http://<device_ip>:<port_number> in the client's browser (for example your phone), replacing <device_ip> with
the IP address of your PC and replacing <port_number> with the port number mentioned in the terminal.

Make your files fly over your Wifi and enjoy :D
