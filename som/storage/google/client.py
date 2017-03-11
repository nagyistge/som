#!/usr/bin/env python

'''
client.py: simple clients for google storage. This first go uses
datastore for metadata, and Google Storage for images (objects) so
a client means a connection to both, with functions to interact with 
both. Both will look for the environment variable GOOGLE_APPLICATION_CREDENTIALS

'''

import datetime

from google.cloud import datastore
from som.storage.google.utils import (
    get_google_service, 
    get_bucket,
    upload_file
)

from som.logman import bot


class ClientBase(object):

    def __init__(self):
        self.datastore = self.datastore_client()
        self.storage = get_google_service('storage', 'v1')
        if self.bucket_name != None:
            self.get_bucket()

    def datastore_client(self):
        '''create a datastore client to work with'''
        return datastore.Client()
  
    def get_bucket(self):
        self.bucket = get_bucket(self.storage,self.bucket_name)

    def upload_object(self,bucket_folder,file_path,verbose=True):
        '''upload_object will upload a file to path bucket_path in storage
        '''
        return upload_file(self.storage,self.bucket,
                           bucket_folder=bucket_folder,
                           file_path=file_path,
                           verbose=verbose)
