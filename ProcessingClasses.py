#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Maricha Friedman, 9/3/21, updated for assignment, TODOs
# Maricha Friedman 9/5/21, updated with help from solution
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to be run by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.

        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # Used solution for help
        try:
            cd_idx = int(cd_idx) # inputted cd ID must be integer
        except ValueError as e:
            print('ID must be integer')
            print(e.__doc__)
        for row in table: # table should be listOfCDObjects, this loops through table checking if ID matches
            if row.cd_id == cd_idx:
                return row # will this return string?
        raise Exception('This CD or Album does not exist in the inventory')

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd

        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the track gets added to.

        Raises:
            Exception: raised in case position is not an integer.

        Returns:
            None:
        """
        tr_position, tr_title, tr_length = track_info # can't use same names as attributes? Got errors when I used same names
        try:
            tr_position = int(tr_position)
        except:
            raise Exception('Position must be an integer.')
        track = DC.Track(tr_position, tr_title, tr_length)
        cd.add_track(track) # Why not DC.CD.add track? Because of the argument cd: DC.CD?
        


