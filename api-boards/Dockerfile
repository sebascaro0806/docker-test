FROM python:3.9
COPY ./ /api-boards
RUN pip install --no-cache-dir --upgrade -r /api-boards/requirements.txt
COPY ./ /api-boards
WORKDIR /api-boards
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3001"]