<h1> Webex Automation </h1>

- This is python selenium Webex automation script.
- It can automatically joins the meeting , send messaeges in the chat and exit the meeting.

* It provides a simple command line interface to control the automation.
* It also provides a server which can be used as a backend to any apps.

<h2>Tools Used </h2>

- Web automation is done using <b>python-selenium</b>.
- To communicate with it i have created a simple Api using <b>Flask</b>.

<h2>Prequesties</h2>

- You need python installed on your computer.
- You need to Install flask and selenium.
- You need to install chromedriver (Note:Both the chrome browser and chrome driver should be at same version) .<br>
  If all set then we can automate webex

<h2>How to use</h2>

- You can use it by cloning the repo ,first step is to start the server by running the following command in terminal/cmd<br><br>
  In Windows type :<br>
  <b>python server.py</b><br><br>
  In Linux type :<br>
  <b> python3 server.py</b>.

- Then open another terminal or cmd and type the following command :<br><br>
In Windows type :<br>
<b>python client.py -name your_name_here -email your_email_id </b> <br><br>
In Linux type :<br>
<b> python3 client.py -name <your name> -email <email id></b>.
<br><br>
<img src="output1.png" placeholder="Sample output">
<h2> Upcoming updates </h2>

* Planning to add automatic exit from meeting after a particular time .
