FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH=/app

# Install PDM
RUN pip install pdm==2.15.4

# Install dependencies
COPY ./pdm.lock ./
COPY ./pyproject.toml ./
RUN pdm install -G:all --no-self --check

# Install package
COPY ./tech_blogs_newsletter/ ./tech_blogs_newsletter/
COPY ./README.md ./
RUN pdm install --no-editable

ENTRYPOINT [ "pdm", "run" ]
CMD [ "tech_blogs_newsletter/main.py" ]
