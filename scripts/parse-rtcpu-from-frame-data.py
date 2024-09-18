#!/usr/bin/env python3
import re
import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt

pattern = re.compile('frame-num = (\d+),frame-rtcpu-timestamp = (\d+)')

frame_time_dict = {}

def parse_nvargus_logs(filename : str) -> None:
	"""
	Parse nvargus logs for Start of Frame(SoF) RTCPU timestamp in nanoseconds
	Read the interval between the number of frames processed per second and store as a dictionary
	"""
	try:
		with open(filename, 'r') as fp:
			lines = fp.readlines()
			diff = 0
			timestamp = 0
			framecount = 0
			for row in lines:
				if re.match(pattern, row):
					frameData = re.findall(r'\d+', row)
					res = list(frameData)
					frametimens = int(res[1])
					framecount = framecount + 1
					if frame_time_dict == {}:
						timestamp = int(frametimens)
						diff = 99997000 # Set the first timestamp
					else:
						prev = timestamp # previous time
						timestamp = int(frametimens) # fetch the current time
						diff = abs(prev - timestamp)
						print(diff)
					frame_time_dict[framecount] = (diff)
	except Exception:
		print(f"Unable to open file {filename}")
		raise

def gen_graph() -> None:
	"""
	Generate graph to plot the interval between frames for nvargus stream
	X-axis - time in seconds
	Y-axis - interval between Start of frame timestamp for each frame per second
	"""
	x1, y1 = frame_time_dict.keys(), frame_time_dict.values()
	plt.xlabel("Number of frames", fontsize=10)
	plt.ylabel("Interval between consecutive SoF RTCPU timestamp", fontsize=10)
	plt.title("Standard deviation of RTCPU timestamp")
	plt.plot(x1,y1)
	print(min(y1))
	print(max(y1))
	plt.tight_layout()
	plt.show()

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', '--logfile', help = "Provide nvargus log file for parsing")
	args = parser.parse_args()
	parse_nvargus_logs(args.logfile)
	gen_graph()

if __name__ == "__main__":
	try:
		main()
	except Exception as ex:
		print(f"Unhandled exception: {ex}.")
		sys.exit(-1)
