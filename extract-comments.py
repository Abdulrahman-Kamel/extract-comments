#!/usr/bin/python3

# Developer By Abdulrahman Kamel
# Github: github.com/Abdulrahman-Kamel

#cat urls.txt | python3 extract-comments.py > all_comments.txt

import requests
import urllib3 
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from sys import exit,stdin
import re


def primary_checks():
	if stdin.isatty():
		print("Please read data as stdin and then use script")
		exit(1)

def basics():
	urllib3.disable_warnings()

def readStdin():
		data = []
		if not stdin.isatty():
			for line in stdin:
				data.append(line.strip())
		return data


class main():
	def __init__(self):
		primary_checks()
		basics()
		self.urls = readStdin()
		self.Poolex(100, self.urls, self.extractComments)

	def extractComments(self, url):
		try:
			response = requests.get(url)
			response_file = open('delme_response.txt','+a')
			response_file.writelines(response.text)
			response_file.close()
			match_html_comment = re.findall(r"<!--.*?-->", response.text)
			match_js_comment = re.findall(r"(// .*|\/\*.*\/\*)", response.text)
			
			global all_comments
			all_comments = match_html_comment + match_js_comment

		except Exception as error:
			pass


		if all_comments:
			print("Comments For: ",url)
			for comment in all_comments:
				print(comment)
			print("="*120)

	def Poolex(self, threads, wordlist, function):
		with PoolExecutor(max_workers=int(threads)) as executor:
		    for _ in executor.map(function, wordlist):
		        pass

if __name__ == '__main__':
	main()
