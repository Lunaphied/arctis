import hid
# import enum

SIDETONE_OFF = bytes.fromhex("06350000000000000000000000000000000000000000000000000000000000")
SIDETONE_LOW = bytes.fromhex("06350100040000000000000000000000000000000000000000000000000000")
SIDETONE_MEDIUM = bytes.fromhex("063501000a0000000000000000000000000000000000000000000000000000")
SIDETONE_HIGH = bytes.fromhex("06350100120000000000000000000000000000000000000000000000000000")

vid = 0x1038	# Artis 1 wireless
pid = 0x12b3	

# TODO: Make this not be garbage
# @enum.unique
# class SidetoneStrength(enum.Enum):
# 	OFF = bytes.fromhex(""
# class AcrtisOne:
# 	def __init__(self, vid, pid):
# 		self.device = hid.Device(vid, pid)
# 	def 

if __name__ == "__main__":
	with hid.Device(vid, pid) as h:
		print(f'Device manufacturer: {h.manufacturer}')
		print(f'Product: {h.product}')
		print(f'Serial Number: {h.serial}')
		# Should set sidetone off
		h.write(SIDETONE_OFF)
