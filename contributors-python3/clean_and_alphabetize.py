import sys

def containsGitHub(line):
	# Check if line contains 'github'
	if line.find("github") != -1:
		return True
	else:
		return False

def containsGitLab(line):
	# Check if line contains 'gitlab'
	if line.find("gitlab") != -1:
		return True
	else:
		return False

def containsBitBucket(line):
	# Check if line contains 'bitbucket'
	if line.find("bitbucket") != -1:
		return True
	else:
		return False

def containsName(line):
	# Check if line contains the following format: "[text-here]"
	start = line.find("[")
	end = line.find("]")
	if start >= 0 and end > start + 1:
		return True
	else:
		return False

def getName(line):
	# Get text from brackets in string
	start = line.find("[")
	end = line.find("]")
	return line[start+1:end]

def containsLink(line):
	# Check if line contains the following format: "(text-here)"
	start = line.find("(")
	end = line.find(")")
	if start >= 0 and end > start + 1:
		return True
	else:
		return False

def getLink(line):
	# Get text from parentheses in string
	start = line.find("(")
	end = line.find(")")
	return line[start+1:end]

def containsMistypedGitHub(line):
	# Check if line contains a mistyped form of 'github'
	link = getLink(line)
	end = link.find(".com")
	if end == -1:
		return False
	count = 0
	for letter in "github":
		if letter in link[end-7:end]:
			count += 1
	if containsGitHub(line) or containsGitLab(line):
		return False
	elif count >= 4:
		return True
	else:
		return False

def containsUnsecureHttp(link):
	# Check if line contains 'old' http (rather than https)
	if link.startswith("http") and not link.startswith("https"):
		return True
	else:
		return False

def containsMistypedHttpsOrUnsecureHttp(link):
	# Check if line contains a mistyped form of 'https'
	end = link.find("://")
	if end == -1:
		return False
	if link[:end] == "https":
		return False
	else:
		return True

def rulesApply(line):
	# Check if line follows the following rules for 'acceptability'
	line = line.lower()
	return (
		containsGitHub(line) or
		containsMistypedGitHub(line) or
		containsGitLab(line) or
		containsBitBucket(line)
	)

# Reformats line to conform to a standard format: "[text-here](link-here)"
def formatLine(line):
	name_exists = containsName(line)
	link_exists = containsLink(line)

	if name_exists:
		# Get the name, remove any 'bold-ifier', remove beginning and trailing whitespace
		name = getName(line)
		name = name.replace("**", "")
		name = name.strip()

	if link_exists:
		# Get the link, correct mistyped 'github', correct mistyped https or unsecure http
		if name_exists:
			start = line.find("]") + 1
			link = getLink(line[start:])
		else:
			link = getLink(line)

		link = link.lower()
		if containsMistypedGitHub(link):
			end = link.find(".com")
			link = "https://github" + link[end:]
		if containsMistypedHttpsOrUnsecureHttp(link):
			index = link.find("://")
			link = link.replace(link[:index], "https")

	if name_exists and link_exists:
		# standardize formatting
		return "[" + name + "]" + "(" + link + ")" + "\r\n"
	elif name_exists:
		# find and standardize non-standard link, those not in the standard "(link-text)" format
		link = line[line.find("]")+1:]
		for symbol in ["(", ")", "[", "]"]:
			link = link.replace(symbol, "")
		link = link.strip()
		return "[" + name + "]" + "(" + link + ")" + "\r\n"
	elif link_exists:
		# find and standardize non-standard name, those not in the standard "(name-text)" format
		end = line.find("(")
		name = line[:end]
		if name.startswith("-"):
			name = name[1:]
		name = name.strip()
		return "[" + name + "]" + "(" + link + ")" + "\r\n"
	else:
		# this is for debugging purposes... (no standard name or link formatting exists)
		return line

def main(filename):
	# read in .md file and get content
	with open(filename, 'r', encoding='utf-8') as file:
		content = file.readlines()

	# reformat each line that is 'acceptable' according to our rules
	data = [formatLine(line) for line in content if rulesApply(line)]

	# rewrite .md file with standardized formating in alphabetical order
	with open(filename, 'w', encoding='utf-8') as file:
		file.write("# Contributors\r\n")
		file.writelines(sorted(data))

# Runs program
if __name__ == '__main__':
	print("Python " + ".".join([str(i) for i in sys.version_info[0:3]]))
	main("Contributors.md")
