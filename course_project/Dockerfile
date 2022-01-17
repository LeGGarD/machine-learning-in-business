FROM python:3.8

# Install dependencies
RUN pip install requests==2.25.1
RUN pip install fastapi==0.63.0
RUN pip install uvicorn==0.13.3
RUN pip install injectable==3.4.4
RUN pip install Pillow==7.0.0
RUN pip install numpy==1.19.4
RUN pip install scipy==1.7.1
RUN pip install simplestr==0.4
RUN pip install pydantic==1.8.2
RUN pip install uuid==1.30
RUN pip install typing==3.7.4.3
RUN pip install pandas==1.3.4
RUN pip install sklearn

# Main app
COPY . /app
WORKDIR /app

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]