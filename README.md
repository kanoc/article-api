## Intro
A toy API for querying articles by keywords using GNews.


## How to run

1. Make sure you have Python 3.10 installed, and you are in the project root folder.

2. Create and activate a virtual environment

   With the builtin `venv` module
   ```bash
   python3 -m venv ~/venvs/article-api
   source ~/venvs/article-api/bin/activate
   ```

   or with `virtualenv`
   ```bash
   mkvirtualenv article-api
   workon article-api
   ```

3. Install the dependencies and the project:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the `env_example`:
   
5. Start the website status check collection, write and trigger as separate process:
   ```bash
   ./bin/run_server.sh
   ```

6. Run a sample API query, like:
   http://0.0.0.0:9000/api/articles?keywords=tech%20for%20startup

### Run code quality checks

```bash
inv check
```

### Run the tests

1. Install the dev requirements:
    ```bash
    inv deps
    ```
2. Run the tests with coverage report:
    ```bash
    inv test
    ```
3. Run the tests without coverage report:
    ```bash
    inv test --no-coverage
    ```