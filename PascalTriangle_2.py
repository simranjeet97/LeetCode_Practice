class Solution(object):
    def getRow(self, rowIndex):
        def getdata(rowIndex):
            currow = []
     
            # 1st element of every row is 1
            currow.append(1)

            # Check if the row that has to
            # be returned is the first row
            if (rowIndex == 0) :

                return currow

            # Generate the previous row
            prev = getdata(rowIndex - 1)

            for i in range(1, len(prev)) :

                # Generate the elements
                # of the current row
                # by the help of the
                # previous row
                curr = prev[i - 1] + prev[i]
                currow.append(curr)

            currow.append(1)

            # Return the row
            return currow
        return getdata(rowIndex)
