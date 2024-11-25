# Beat Maker

Beat Maker is a web-based application that allows users to create and play drum beats using a simple and intuitive interface.
![Beats](https://github.com/user-attachments/assets/0eb55cdd-0ebd-4e09-908c-e23c530ba89b)


## Features

- Create beats using various instruments like snare, hi-hat, bass, tom, and cowbell.
- Adjust the volume of each instrument.
- Control the tempo of the beat.
- Play and stop the beat.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/jeffreywangdev/beatmaker.git
    cd beatmaker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask server:
    ```sh
    python main.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the Beat Maker application.

## Docker

You can also run the application using Docker:

1. Build the Docker image:
    ```sh
    docker build -t beatmaker .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 80:80 beatmaker
    ```

3. Open your web browser and go to `http://localhost` to access the Beat Maker application.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
