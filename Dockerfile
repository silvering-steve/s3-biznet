FROM python:latest
LABEL authors="Silvering Steve"

#  No interaction in install
ARG DEBIAN_FRONTEND=noninteractive

# Install base utils
RUN apt-get update \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*


# Change workdir
WORKDIR /app

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy context
COPY . .

# Run the program
CMD ["python", "main.py"]