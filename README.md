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
1. To begin, you need to install Python version 3.12. Next, update pip. In the terminal, navigate to the "diploma-app" directory and execute the command: 
    ```bash
    py -m pip install requirements.txt
    ```

2. Modify the file size of secret_message.txt in the file.py script. The default size is 100MB.

3. Run the file.py application using the command:
    ```bash
    py .\file.py
    ```

4. Choose the appropriate line in the start_another_app function in app.py. Comment out the rest of the algorithm functions based on your preference.

5. Run the app.py application using the command:: 
    ```bash
    py .\app.py
    ```

6. Open your web browser and navigate to the website: [http://localhost:8080](http://localhost:8080) .

On the webpage, you will see the results of CPU, Memory, and Disk usage, along with information on the percentage increase.

### Docker and docker-compose
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Dorota7521/in-test.git
    ```

2. Navigate to the project directory:

    ```bash
    cd inz-test
    ```

3. Build the Docker image:

    ```bash
    docker-compose up --build
    ```

This command will build the Docker image and start the application in a container.

4. Access the application:

    Open your web browser and go to [http://localhost:8080](http://localhost:8080) to view the application.


5. To stop the running Docker container, use the following command:

```bash
docker-compose down
```

This will stop and remove the containers.

If you need to customize any configuration or settings, you can modify the docker-compose.yml file or adjust environment variables in the Dockerfile.

### Virtual Machines
ewentualnie ansible, ale raczej wątpię xD

## Application Functionality
The application operates in several steps. Firstly, the file.py application is used to generate a text file of a specified size. Subsequently, the app.py application retrieves the IP of the process it is using. This process ID (PID) is then passed to the variables cpubar.n, rambar.n, and diskbar.n. These variables gather information on the CPU, Memory, and Disk usage of that specific process. Data is collected approximately every second.

Next, using the Flask library, the index.html template, and the static.js and styles.css files, three charts depicting the CPU, Memory, and Disk usage over time are displayed on the website [http://localhost:8080](http://localhost:8080). Following this, within the start_another_app() function, one of the six algorithm applications is executed after a 5-second delay. While the algorithm is running, changes appear on the charts, and the percentage increase in CPU, Memory, and Disk usage is calculated on the website.

The applications can be run for different file sizes, allowing for the verification of container performance.
