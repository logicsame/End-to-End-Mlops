FROM python:3.11-slim
WORKDIR /app
COPY . /app
# Run
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]