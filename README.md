# ShiftMaker

This is a tool for making shiftplans for Analog, written in Python. 
This Readme functions as a brief documentation of the tool and the process of planning shifts in analog.
It is assumed that the reader is the current shiftplanning manager, and that they have access to [the google drive folder](https://drive.google.com/drive/folders/0B8T6GhF4leciM3dPRG10MjdUN3c?resourcekey=0-NUPQpVTPTkN4R_9Xg7aprw).


## Shift Planning
The process for planning shifts is as follows:
1. Ask the current Chairperson of Analog if there is anything to consider for next semesters shift plan
2. Send out the survey for shift availability on Basecamp. The form template can be found on drive. Try to set the deadline so that you will be able to realease the schedule a week before the semester starts.
3. Wait until your deadline for submitting availability has passed. Remind people to fill it out in the days up to the deadline
4. In the form, go to results, press "view in sheets" and download the sheets file as a CSV file.
5. Save this file in the data folder.
6. In `fileparser.py` find the path variable on line 6, and edit it so that it points to the CSV file.
7. Run `shiftmake.py` and optionally save the results to a txt file.
8. Fill these results into the shiftplan template.
9. Adjust the schedule as needed, based on any wished people have made to you. `statistics.py` offers a variety of helpful information.
10. Confirm the schedule with the chairperson. 
11. Publish the schedule on Basecamp. Make sure to tell people that it is tentative, and might change.
12. Expect a ludicrous amount of people to write to you to say that something came up and they can't take their shift anymore.
13. Just before the semester starts, fill the shift information into [the online shiftplan](https://shiftplanning.cafeanalog.dk/shifts). The username is manager@analogio.dk and the password is Latte@2204.

## The Code - this will likely only make sense if you have taken the Master's course Algorithm Design 
The code used for shiftmaker is a weird hack modelling it as a bipartite matching problem reduced to the maximum flow problem, and solved with Ford fulkerson.
Some changes have been made to accommodate that people should be distributed evenly on shifts, and people should preferably be on their preferred shifts.
Specifically, it distributes baristas by first only giving a capacity of 1 to every edge, runs the algorithm, adds 1 capacity
and repeats this until the desired amount of people on a shift is reached. 
People are put on their preferred shifts by initially assuming they can only be assigned to their preferred shifts. The algorithm is mostly stable, so it should not
reassign people unless it has to. 

If you have any bright ideas for how to improve the code, go right ahead. Here are some ideas for improving:
* Add a filepicker to the fileparser, so you don't have to change code.
* Make shiftmaker output the data in the shiftplan on drive. 
* Figure out a way to make the algorithm put people together with other people the wish to be on shift with (this might be NP-hard).