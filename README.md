# house_price_prediction_end-2-end
This project aims to predict house prices in Boston using machine learning techniques. The project includes data collection, exploratory data analysis (EDA), data preprocessing, training different regression models, building a Streamlit web app for predictions, containerizing the app using Docker, and testing the Docker container.

## Table of Contents
 - [Overview](#overview)
 - [AI Algorithm Training](#ai-algorithm-training)
 - [Creation of Web App](#creation-of-web-app)
 - [Containerization of App](#containerization-of-app)
 - [License](#license)

## Overview
This project is structured into three key phases, each playing a vital role in delivering a robust solution for Boston house price prediction:

- AI Algorithm Training
- Creation of Web App
- Containerization of App

## AI Algorithm Training

- **Dataset Collection:**
The dataset used in this project is the Boston House Price dataset, which is included in the `sklearn.datasets` module.

- **Exploratory Data Analysis (EDA):**
Exploratory Data Analysis was performed to understand the structure and characteristics of the dataset. This included checking for missing values, data distribution, correlation analysis, checking constant features, checking highly collinear features, checking features with low collinearity with output etc.

- **Data Preprocessing:** 
Data preprocessing involved handling missing values, feature scaling, and splitting the data into training and testing sets.

- **Model Training:**
Linear Regression, Lasso Regression, and Ridge Regression models were trained using the preprocessed data.

- **Model Evaluation:**
Trained models were judge using following assumptions: 
    - The scatter plot comparing the true values (y-true) with the predicted values (y-predict) should exhibit a linear relationship.
    - The residuals should follow a normal distribution with a mean approximately equal to zero.
    - There should be uniform distributions observed between the scatter plot of predictions and residuals.

    The performance of the trained models was evaluated using following evaluation metrics : 

    - Mean Absolute Error (MAE) 
    - Mean Squared Error (MSE) 
    - Root Mean Squared Error (RMSE) 
    - R Squared 
    
    You can access AI Algorithm Training source code from [here]().


## Creation of Web App
- The project progresses to the creation of an interactive web application using Streamlit. This user-friendly interface prompts users to input relevant features, facilitating instant predictions of house prices based on the trained model.

- User has to input following field for house price prediction: 
    - **CRIM**     per capita crime rate by town
    - **ZN**      proportion of residential land zoned for lots over 25,000 sq.ft.
    - **INDUS**    proportion of non-retail business acres per town
    - **CHAS**    Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    - **NOX**      nitric oxides concentration (parts per 10 million)
    - **RM**      average number of rooms per dwelling
    - **AGE**      proportion of owner-occupied units built prior to 1940
    - **DIS**      weighted distances to five Boston employment centres
    - **RAD**     index of accessibility to radial highways
    - **TAX**     full-value property-tax rate per $10,000
    - **PTRATIO** pupil-teacher ratio by town
    - **B**        1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
    - **LSTAT**    % lower status of the population

    You can access App source code from [here]().

- **App Test on Local Host:**
    1. Clone the repository:

        ```
        git clone https://github.com/umairsiddique3171/house_price_prediction_end-2-end.git
        cd docker/app
        ```

    2. Create and activate a virtual environment:

        ```
        python -m venv env
        .\env\Scripts\activate
        ```

    3. Install dependencies:

        ```
        pip install -r requirements.txt
        ```

    4. Run the Streamlit app:

        ```
        streamlit run app.py
        ```

    5. Access the app in your browser at returned local host (e.g. `http://localhost:80`).

## Containerization of App
- **Docker Installation:**
    * For Docker Desktop installation, please visit [here](https://www.docker.com/products/docker-desktop/).
    * To see system requirements, please visit official Docker Documentation [here](https://docs.docker.com/desktop/).

- **Docker Setup:**

    To check docker installation in your system, run following command in your terminal : 
    ```
    PS C:\Users\US593> docker
    ```
    Terminal should be returning lists of docker commands.

- **Dockerfile Setup:**

    Setup "Dockerfile" as mentioned [here]().

- **Build Docker Image:**

    To build docker image, use the following command in your terminal : 
    ```
    docker build -t house_price_app:v1.0 .
    ```
    To see whether docker image has been built or not, use the following command in your terminal : 
    ```
    docker images
    ```

- **Run Docker Image as a Container:**

    To run docker image as a container, type the following command in your terminal : 
    ```
    docker run -p 80:80 house_price_app:v1.0
    ```
    In Windows, basically, this url `http://0.0.0.0:80` usually doesn't work. Try running `http://localhost/` in your browser.

    To check whether the container is running, type the following command in your terminal : 
    ```
    docker ps
    ```
    To stop the container from running, type the following command in your terminal : 
    ```
    docker stop <container_id>
    ```

- **Push Docker Image to Docker Hub:**

    To push a Docker image to Docker Hub, follow these steps:

    1. **Login to Docker Hub**: 

        Before pushing the image, you need to authenticate yourself with your Docker Hub credentials. Use the following command:
    
        ```
        docker login
        ```

        After running this command, you'll be prompted to enter your Docker Hub username and password.

    2. **Tag the Docker Image**:

        Before pushing the image, you need to tag it with your Docker Hub username and the repository name. This is done using the following command:
        ```
        docker tag house_price_app:v1.0 umairsiddique3171/house_price_app:v1.0
        ```

    3. **Push the Docker Image**:

        Finally, push the tagged image to Docker Hub using the following command:
        ```
        docker push umairsiddique3171/house_price_app:v1.0
        ```
        This command will push the tagged image to your Docker Hub repository. Make sure you have appropriate permissions to push to the repository.

## License
This project is licensed under the [MIT License]().

## Author 
[@umairsiddique3171](https://github.com/umairsiddique3171)
