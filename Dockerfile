FROM python:3.12.7-alpine3.20

WORKDIR /usr/workspace

COPY ./ /usr/workspace

RUN pip install pytest selenium allure-pytest python-dotenv Faker

CMD ["pytest", "--alluredir=allure-results", "-m", "smokes"]
