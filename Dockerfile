FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN apt-get update && apt-get install -y \
	curl \
	gnupg2 apt-transport-https && \
	curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
	install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ && \
	curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
	apt-get update && \
	ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* microsoft.gpg
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["gunicorn", "-b", "0.0.0.0:8006", "run:app"]
