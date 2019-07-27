from databaseConnection import databaseConnection
from datetime import datetime, timedelta

"""
Computes the time difference between two datetime objects,
returns the total second difference
"""


def compareTime(datetimeOld, datetimeNew):
    """
    Tells pycharm what types everything is:

    :type datetimeOld: datetime
    :type datetimeNew: datetime
    """

    # convert years to days

    dayTotal = datetimeOld.year * 365
    oldTime = timedelta(days=(dayTotal + datetimeOld.day), hours=datetimeOld.hour, minutes=datetimeOld.minute,
                        seconds=datetimeOld.second).total_seconds()

    newTime = timedelta(days=(dayTotal + datetimeNew.day), hours=datetimeNew.hour, minutes=datetimeNew.minute,
                        seconds=datetimeNew.second).total_seconds()

    timeDifference = newTime - oldTime

    return timeDifference


"""
Stores a date time object in the database

Returns True on success
"""


def storeDateTime(dbConnection, id, current):
    """
    Tells pycharm what types everything is:
    :type dbConnection: databaseConnection
    :type current: datetime
    """

    try:
        # make a string, add on the year, tab, month, tab, day, tab, hour, tab, minute, tab, second
        toStore = current.strftime("%Y\t%m\t%d\t%H\t%M\t%S")

        # should be equivalent to:
        # current.year + "\t" + current.month + "\t" + current.day + "\t" + current.hour + "\t" +
        # current.minute + "\t" + current.second

        #split it into an array for storage
        dbConnection.profileUpdate({"id": id}, {"$set": {"dailytime": toStore.split("\t")}})

        return True
    except:
        # the user likely did not set up their profile
        return False


"""
Reconstructs a date time object from the database

Returns True on success
"""


def constructDateTime(user):
    # first parse the string, looking for tabs
    try:
        itemsToCreate = user["dailytime"]

        toReturn = datetime(year=int(itemsToCreate[0]), month= int(itemsToCreate[1]), day=int(itemsToCreate[2]),
                            hour=int(itemsToCreate[3]), minute = int(itemsToCreate[4]), second=int(itemsToCreate[5]),
                            microsecond=0)

        return toReturn
    except Exception:
        return None
