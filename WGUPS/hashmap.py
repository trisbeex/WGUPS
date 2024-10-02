#creates a hash table of all the packages
class HashTable:
    def __init__(self):
        self.size = 40
        self.table = [None] * self.size

    #the bucket is determined using modulo 40
    def _get_hash(self, key):
        hash_key = (int(key) % 40)
        return hash_key

    #checks the bucket the key would be located in for the package and returns if found
    def _get_package(self, key):
        hash_key = self._get_hash(key)
        if self.table[hash_key] is None:
            return None
        else:
            for package in self.table[hash_key]:
                if package[0] == key:
                    return package

    #takes package information and adds it to the bucket if empty
    #otherwise updates the value if it exists or appends to the bucket otherwise
    def add_package(self, key, value):
        hash_key = self._get_hash(key)
        package = [key, value]
        if self.table[hash_key] is not None:

            for package in self.table[hash_key]:
                if package[0] == key:
                    package[1] = value
                    return True
            self.table[hash_key].append(package)
        else:
            self.table[hash_key] = list([package])
            return True

    #finds the bucket the package would be in, and if it exists, removes it
    def remove_package(self, key):
        hash_key = self._get_hash(key)

        if self.table[hash_key] is None:
            return False
        for i in range(len(self.table[hash_key])):
            if self.table[hash_key][i][0] == key:
                self.table[hash_key].pop(i)
                return True

    #retrieves package details when given the key if it exists
    def packageLookup(self, key):
        hash_key = self._get_hash(key)
        if self.table[hash_key] is None:
            print("not found")
            return None
        else:
            for package in self.table[hash_key]:
                if package[0] == key:
                    print("Package Details")
                    print(f"ID: {package[1].key}, Deadline: {package[1].deadline}, Address: {package[1].address},"
                          f"City: {package[1].city}, Zip: {package[1].zip}, Weight: {package[1].weight}, "
                          f"Status: {package[1].status}")