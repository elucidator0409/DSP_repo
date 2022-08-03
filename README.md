v# Movie recommendation website using content-based filtering with NLP and text embedding

> This project is a result of the course "Digital Systems Project" done by Tran Quoc Khanh

## Set up to run locally

### Set up installations
1. Install the corrent NodeJs for your OS: [installation guide](https://nodejs.org/en/download/)
2. Install python and virtualenv:
- Install python using [python homepage](https://www.python.org/downloads/)
- Install pipx using pip [pipx install guide](https://pypi.org/project/pipx)
- Install virtualenv via pipx [installation guide](https://virtualenv.pypa.io/en/latest/installation.html)
- Note: In case virtualenv command not found error -> add virtualenv to PATH [guide](https://www.java.com/en/download/help/path.html)
3. Initialize virtualenv [guide](https://pythonbasics.org/virtualenv/) - short guide:
```bash
virtualenv -p python3 testproject
```
Then activate the virtualenv

```
source testproject/Scripts/activate
```

4. Use `git bash`

### Set up virtualenv on my laptop (Windows) (use powershell)
1. Use pip : pip install virtualenv
2. Create folder myenv: virtualenv myenv
3. Go into env : myenv\Scripts\activate (only for backend)
4. cd to backend folder 

### Set up the project

> Start the Django backend first before running the frontend

#### Start the React frontend
0. Use a different git bash window starting at `/DSP_REPO`
1. Switch to the frontend folder: `cd frontend`
2. Install the needed dependencies: `npm install --legacy-peer-deps`
3. Start the frontend: `npm start`
4. The frontend will be hosted on `localhost:3000`

#### Start the Django backend
0. Use a different git bash window starting at `/DSP_REPO`
1. Start the virtualenv, for Windows, assume that you created the virtualenv folder at the top level of `/DSP_REPO` and the terminal is currently pointing to it: `source yourvirtualevnname/Scripts/activate`
2. Switch to the backend folder: `cd backend`
3. Install the necessary modules: `pip install -r requirements.txt`
4. Migrate to use sqlite database: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

### Working on the project
- For the Django backend, remember to freeze the requirements into requirement.txt before pushing the code to Github: `pip freeze > requirements.txt`




