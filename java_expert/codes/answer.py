# Parse input file and print fields relevant to answers
# (post id and owner id.

import sys
import xml.sax
import os

# To extract posts that are answers
answerId = "2"

class StackContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):

        if name != "row":
            return

        # Get post type from the input file
        ptype = "__none__"
        if "PostTypeId" in attrs:
            ptype = attrs.getValue("PostTypeId")

        # Check if the posts types are answers or not. If not answers, then skip.
        if ptype != answerId:
            return

        # Get post id and owner id
        id = "__none__"
        if "Id" in attrs:
            id = attrs.getValue("Id")
        owner = "__none__"
        if "OwnerUserId" in attrs:
            owner = attrs.getValue("OwnerUserId")

        line = []
        line.append(id)
        line.append(owner)
        print ("\t".join(line))

        # Write output in file
        with open("ans.txt", "a") as output:
            for row in line:
                output.write(str(row)+'\t')
            output.write('\n')

if __name__ == '__main__':

    # Delete previous output file "ans.txt", if it exists
    if os.path.exists("ans.txt"):
        os.remove("ans.txt")

    if len(sys.argv) < 2:
        print ("Usage: " + sys.argv[0] + " <file>")
        sys.exit(1)



    fname = sys.argv[1]

    f = open(fname, encoding = 'utf-8')
    xml.sax.parse(f, StackContentHandler())
