class Helper():

    def super_data(self,superlist):
        dict1 = {}

        for ele in superlist:

            dict1[int(ele.split(".")[0])] = [ele.split(".")[1].split(" (")[0].strip(),
                                             int(ele.split("(")[1].split(")")[0]),
                                             float(ele.split("(")[1].split(")")[1])]
        return dict1


    def write_into_file(self,filename,superlist):
        fo = open(filename, "w")
        for ele in superlist:
            fo.write(ele + "\n")
        fo.close()