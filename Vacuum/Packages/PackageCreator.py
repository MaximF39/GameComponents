import struct

class PackageCreator:
    def __init__(self, PackageNumber):
        self.PackageNumber = PackageNumber
        self.data = bytearray()

    def get_package(self) -> bytearray:
        pack = self.converter(self.PackageNumber, "i")
        pack = self.byte_writer(pack, self.converter(len(self.data), "i"))
        return self.byte_writer(pack, self.data)

    def converter(self, Value, BytesType):
        return bytearray(struct.pack(BytesType, Value))

    def write_utf(self, string):
        self.data = self.byte_writer(self.data, self.byte_writer(bytearray([len(bytes(string, 'utf-8')), 0]),
                                                                 bytes(string, 'utf-8')))

    def write_double(self, double):
        self.data = self.byte_writer(self.data, self.converter(double, "d"))

    def write_int(self, int_):
        self.data = self.byte_writer(self.data, self.converter(int_, "i"))

    def write_float(self, float_):
        self.data = self.byte_writer(self.data, self.converter(float_, "f"))

    def write_short(self, short):
        self.data = self.byte_writer(self.data, self.converter(short, "h"))

    def write_unsigned_byte(self, byte):
        self.data = self.byte_writer(self.data, bytearray([byte]))

    def write_bool(self, bool_):
        self.data = self.byte_writer(self.data, self.converter(bool_, "?"))

    def write_bytes(self, ByteArray):
        self.data = self.byte_writer(self.data, ByteArray)

    def byte_writer(self, oneByteArray, twoByteArray):
        res = bytearray(oneByteArray)
        for i in twoByteArray:
            res.append(i)
        return res
