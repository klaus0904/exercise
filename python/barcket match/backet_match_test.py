import backet_match
import sys

if __name__ == "__main__" :
    if len(sys.argv) < 2 :
        print "Pleae input check file "
        exit(0)
    test_file = open( sys.argv[1])
    line_no = 1
    for line in test_file :
                if not backet_match.is_match(line) :
                    print "Line "+str(line_no)+" not match!"
                line_no += 1