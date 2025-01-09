# Step 1: Use an official Python runtime as the base image
FROM python:3.9

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Step 4: Install pipenv and the project dependencies
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

# Step 5: Copy the rest of the app's files
COPY app.py /app/
COPY churn_model.pkl /app/

# Step 6: Expose the Flask app's port
EXPOSE 8501

# Step 7: Set the command to run the Flask app
CMD ["pipenv", "run", "python", "app.py"]
