# Base the image on the built-in Azure Functions Linux image.
FROM microsoft/azure-functions-python3.6

# Limit packages to minimum needed
ADD requirements.txt /home/site/wwwroot/
RUN pip install -r /home/site/wwwroot/requirements.txt

ENV AzureWebJobsScriptRoot=/home/site/wwwroot

ENV AZURE_STORAGE_QUEUE_NAME=resource-jobs

# Add files from this repo to the root site folder
COPY ./AzureFunctions/ /home/site/wwwroot/
COPY ./Common/ /home/site/wwwroot/Common/
COPY ./Adapters/ /home/site/wwwroot/Adapters/
ADD ./host.json /home/site/wwwroot/

ENV PYTHONPATH = $PYTHONPATH:/home/site/wwwroot/