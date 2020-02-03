class Helper():

    def super_data(self,superlist):
        
        """
        Prepare the golden for all the movies 
        
        {<ranking>:[<movie_name>,<release_date>,<imdb_ratings>]}
        
        """
        dict1 = {}

        for ele in superlist:

            dict1[int(ele.split(".")[0])] = [ele.split(".")[1].split(" (")[0].strip(),
                                             int(ele.split("(")[1].split(")")[0]),
                                             float(ele.split("(")[1].split(")")[1])]
        return dict1


    def write_into_file(self,filename,superlist):
        
        """
        Function used to write the data into the file.
        
        parameters :-
            filename:- Name of the file in which you have to write
            superlist:- list of string that you have to write in the file
        """
        fo = open(filename, "w")
        for ele in superlist:
            fo.write(ele + "\n")
        fo.close()
