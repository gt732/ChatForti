# ChatForti

This is a quick project that uses FastAPI to create an API endpoint that receives debug output from a Fortigate firewall. The firewall is configured with an automation stitch that triggers when high CPU usage is detected. The stitch runs troubleshooting commands and sends a HTTP post message with the debug output to the FastAPI endpoint. The FastAPI endpoint then forwards the debug output to the ChatGPT API for review.

The response is saved to a Python object, which can then be utilized in various ways, such as forwarding to Slack, Teams, Email, Updating a ticket, and more.

# Demo
![alt text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTY5MzU1M2MwYjQzZTM2NGM2ZmEzMTgzYWFiOGM2ZGEwYTY1ODY1MyZjdD1n/6GnmYGHkmC5PEuZngG/giphy.gif)
## Tools
- FastAPI
- Fortigate Firewall
- ChatGPT API


## How to Use

- Configure the Fortigate firewall to trigger the automation stitch when high CPU usage is detected
- Set the HTTP post message to the FastAPI endpoint URL
- The FastAPI endpoint will forward the debug output to the ChatGPT API for review
![alt text](https://i.imgur.com/TKa2QjF.png)
![alt text](https://i.imgur.com/MosYTMU.png)
![alt text](https://i.imgur.com/QJfm0C4.png)
## License
This project is licensed under the MIT License.