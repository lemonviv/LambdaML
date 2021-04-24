import logging
import memcache
from botocore.exceptions import ClientError

class Memcached(Storage):

    def __init__(self, endpoint):
        endpoint += ":11211"
        try:
            self.client = memcache.Client([endpoint])
        except ClientError as e:
            # AllAccessDisabled error == endpoint not found
            logging.error(e)

    def list_objects(self, name):
        objects = self.client.get_multi(name)
        #print(objects)
        if bool(objects):
            return objects
        else:
            return None

    def get_object(self, name):
        try:
            # NOTE(milos) key is now key_field
            response = self.client.get(key=name)
        except ClientError as e:
            # AllAccessDisabled error == client lost
            logging.error(e)
            return None
        return response

    def set_object(self, name, data):
        if isinstance(data, bytes) or isinstance(data, str) or isinstance(data, int):
            object_data = data
        else:
            logging.error('Type of ' + str(type(data)) +
                        ' for the argument \'src_data\' is not supported.')
            
        try:
            response = self.client.set(name, object_data)
        except ClientError as e:
            logging.error(e)
            return False
        return response

    # TODO(milos) you can accept more than one key here
    def delete_object(self, name):
        try:
            self.client.delete_multi(name)
        except ClientError as e:
            # AllAccessDisabled error ==  client lost
            logging.error(e)
            return False

        return True

    def delete_all_objects(self):
        self.client.flust_all()
        return True
