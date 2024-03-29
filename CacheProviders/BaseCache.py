class BaseCache:
    def set(self, key, value):
        raise NotImplementedError("Set method is not implemented")

    def get(self, key):
        raise NotImplementedError("Get method is not implemented")

    def delete(self, key):
        raise NotImplementedError("Delete method is not implemented")