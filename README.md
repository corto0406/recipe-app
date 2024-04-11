# recipe-app

This web application is built with Python using the Django framework.

## Getting Started:

**Prerequisites:** You will need to work in a virtual environment with Django installed.

### Setting up a Virtual Environment:

If you haven't created a virtual environment on your machine yet:

1. Install virtualenvwrapper by running:
    ```
    pip install virtualenvwrapper
    ```

2. Create a virtual environment by running:
    ```
    mkvirtualenv test-environment
    ```

3. Activate the environment by running:
    ```
    workon a2-ve-recipeapp
    ```

4. Install Django in the environment by running:
    - For macOS:
        ```
        pip install django
        ```
    - For Windows:
        ```
        py -m pip install Django
        ```

### Running the Application:

1. Navigate to the root folder of the project in your terminal.

2. Run the following command:
    ```
    python manage.py runserver
    ```

3. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Features:

Users can perform the following actions:

- View all recipes in a list.
- Click on any recipe to view its details.

### Test Credentials:

Use the following credentials to test the app:

- **Username:** nemanja
- **Password:** samuel123

### Live Demo:

You can also access the app through the following link: [Recipe App](https://thawing-bayou-02420-bc484a50611f.herokuapp.com/).
