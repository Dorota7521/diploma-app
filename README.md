# Analyzing Container Performance through Algorithms 
## Project Goal and Scope 

The project aims to assess whether containers hosting applications exhibit better performance compared to virtual machines running the same applications or a laptop. The tools used for this evaluation include:

* Python
* Flask library
* Crypography library
* Docker
* HTML5
* CSS
* JavaScript

The encryption applications and I/O operations are implemented in Python. Subsequently, using the Flask library and front-end tools, the CPU, memory, and disk consumption results are displayed on a web page. The application retrieves the process ID (PID) of the running application, ensuring that the results are not affected by other processes.


## Launching Applications 
### Local PC
To begin, you need to install Python version 3.12. Next, update pip. In the terminal, navigate to the "inz-app" directory and execute the command: 
`$ py -m pip install requirements.txt`

Afterwards, modify the file size of secret_message.txt in the file.py script (default is 100MB).

In the next step, run the file.py application using the command:
`$ py .\file.py`

Then, choose the appropriate line in the start_another_app function in app.py. This line corresponds to the algorithm you want to use. Comment out the rest of the algorithm functions.

The next step is to run the app.py application using the command: 
`$ py .\app.py`

Then, navigate to the website http://localhost:8080.

On the webpage, you will see the results of CPU, Memory, and Disk usage, along with information on the percentage increase.

### Virtual Machines
ewentualnie ansible, ale raczej wątpię xD

### Docker and docker-compose
tutaj coś o puszczeniu tym jak są zbudowane Dockerfaile i co się dzieje w pliku .yml, jakie boblioteki są instalowane (requirments.txt)


## Application Functionality
The application operates in several steps. Firstly, the file.py application is used to generate a text file of a specified size. Subsequently, the app.py application retrieves the IP of the process it is using. This process ID (PID) is then passed to the variables cpubar.n, rambar.n, and diskbar.n. These variables gather information on the CPU, Memory, and Disk usage of that specific process. Data is collected approximately every second.

Next, using the Flask library, the index.html template, and the static.js and styles.css files, three charts depicting the CPU, Memory, and Disk usage over time are displayed on the website http://localhost:8080. Following this, within the start_another_app() function, one of the six algorithm applications is executed after a 5-second delay. While the algorithm is running, changes appear on the charts, and the percentage increase in CPU, Memory, and Disk usage is calculated on the website.

The applications can be run for different file sizes, allowing for the verification of container performance.
